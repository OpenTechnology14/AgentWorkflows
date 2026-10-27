"""Compile declared public text into deterministic, self-contained packages."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import io
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = 'plugins/agent-workflows'
SKILL = PLUGIN + '/skills/agent-workflows'

def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode()

def safe_file(root, relative):
    p = PurePosixPath(relative)
    if p.is_absolute() or '..' in p.parts or '\\' in relative or p.as_posix() != relative:
        raise ValueError(f'Noncanonical input path: {relative}')
    candidate = root / relative
    if not candidate.resolve().is_relative_to(root.resolve()):
        raise ValueError(f'Input escapes source root: {relative}')
    if any(parent.is_symlink() for parent in [candidate, *candidate.parents] if parent != root.parent):
        raise ValueError(f'Symlink input: {relative}')
    if not candidate.is_file():
        raise ValueError(f'Missing input: {relative}')
    return candidate.read_bytes()

def archive(files):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_STORED) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    return stream.getvalue()

def render(root=ROOT):
    manifest_bytes = safe_file(root, 'packaging/manifest.json')
    m = json.loads(manifest_bytes)
    if m['name'] != 'agent-workflows' or not re.fullmatch(r'\d+\.\d+\.\d+', m['version']):
        raise ValueError('Invalid package identity/version')
    if m['entrypoint'] != 'packaging/ENTRYPOINT.md':
        raise ValueError('Entrypoint must be packaging/ENTRYPOINT.md')
    refs = m['references']
    if not isinstance(refs, list) or not refs or len(refs) != len(set(refs)):
        raise ValueError('References must be nonempty and unique')
    inputs = {'packaging/manifest.json': manifest_bytes}
    for path in [m['entrypoint'], 'packaging/openai.yaml', 'LICENSE', 'CLAUDE.md', *refs]:
        if path in refs and not re.fullmatch(r'(workflows|templates)/[A-Z_]+\.md', path):
            raise ValueError(f'Not a generic reference: {path}')
        inputs[path] = safe_file(root, path)
    if any(not isinstance(v, str) or '\n' in v for v in [m['name'], m['description']]):
        raise ValueError('Skill metadata must be single-line text')
    entry = inputs[m['entrypoint']].decode().replace('](../', '](references/')
    skill = ('---\nname: ' + m['name'] + '\ndescription: ' + json.dumps(m['description']) + '\n---\n\n' + entry).encode()
    output = {
        SKILL + '/SKILL.md': skill,
        SKILL + '/agents/openai.yaml': inputs['packaging/openai.yaml'],
        SKILL + '/LICENSE': inputs['LICENSE'],
        PLUGIN + '/LICENSE': inputs['LICENSE'],
        PLUGIN + '/plugin.json': encoded({'$schema':'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json','name':m['name'],'version':m['version'],'description':m['description']}),
        'AGENTS.md': inputs['CLAUDE.md'],
    }
    for ref in refs:
        output[SKILL + '/references/' + ref] = inputs[ref]
    instructions = re.sub(r'\[([^\]]+)\]\(references/[^)]+\)', r'\1 (see the bundled knowledge)', entry)
    instructions += '\nUse the supplied KNOWLEDGE.md as reference. If a needed source/tool is unavailable, state the limitation. Never claim persistent updates or handoffs without evidence.\n'
    knowledge = '# Agent Workflows knowledge\n\nGeneric reference only. Actual project rules and authorized scope govern.\n'
    for ref in refs:
        text = inputs[ref].decode()
        # The knowledge pack is one document, so relative file links become section names.
        text = re.sub(r'\[([^\]]+)\]\((?!https?://)[^)]+\)', r'\1 (reference section)', text)
        knowledge += '\n\n---\n\n## Source: ' + ref + '\n\n' + text
    output['dist/chatgpt/INSTRUCTIONS.md'] = instructions.encode()
    output['dist/chatgpt/KNOWLEDGE.md'] = knowledge.encode()
    output['dist/chatgpt/STARTERS.md'] = b'# Conversation starters\n\n- Review existing proposal work and show only the decisions you need from me.\n- The save button does nothing. Investigate and prepare the next prompt.\n- Smallest version, no notifications. Update the scope and next agent prompt.\n'
    output['dist/chatgpt/LICENSE'] = inputs['LICENSE']
    output['dist/agent-workflows-plugin.zip'] = archive({p[len(PLUGIN)+1:]: data for p, data in output.items() if p.startswith(PLUGIN + '/')})
    output['dist/agent-workflows-skill.zip'] = archive({'agent-workflows/' + p[len(SKILL)+1:]: data for p, data in output.items() if p.startswith(SKILL + '/')})
    output['dist/agent-workflows-chatgpt.zip'] = archive({p[len('dist/chatgpt/'):]: data for p, data in output.items() if p.startswith('dist/chatgpt/')})
    output['dist/manifest.json'] = encoded({'name':m['name'],'version':m['version'],'sources':{p:hashlib.sha256(b).hexdigest() for p,b in sorted(inputs.items())},'outputs':{p:hashlib.sha256(b).hexdigest() for p,b in sorted(output.items())}})
    return output

def synchronize(root=ROOT, check=False, include_dist=True):
    output = render(root)
    if not include_dist:
        output = {p:b for p,b in output.items() if not p.startswith('dist/')}
    for rel in output:
        p = root / rel
        if not p.resolve().is_relative_to(root.resolve()) or any(x.is_symlink() for x in [p,*p.parents]):
            raise ValueError(f'Unsafe output path: {rel}')
    for directory in [PLUGIN] + (['dist'] if include_dist else []):
        for p in (root / directory).rglob('*'):
            if p.is_symlink() or p.is_file() and p.relative_to(root).as_posix() not in output:
                raise ValueError(f'Unexpected generated file; inspect before removing: {p.relative_to(root)}')
    drift = [p for p,b in output.items() if not (root/p).is_file() or (root/p).read_bytes() != b]
    if check and drift:
        raise ValueError('Generated files differ: ' + ', '.join(drift))
    if not check:
        for p,b in output.items():
            target = root/p
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(b)
    return len(output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check committed plugin/AGENTS parity without writing; also check dist if it exists')
    args = parser.parse_args()
    try:
        count = synchronize(check=args.check, include_dist=not args.check or (ROOT/'dist').exists())
    except (ValueError, KeyError, TypeError) as error:
        parser.exit(1, f'{error}\n')
    print(f'PASS: {count} generated files {"checked" if args.check else "built"}')
