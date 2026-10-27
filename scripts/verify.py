"""Validate public source boundaries, package parity and local Markdown links."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re
import sys
from build import ROOT, synchronize

def verify(root=ROOT):
    synchronize(root, check=True, include_dist=(root/'dist').exists())
    problems = []
    count = 0
    files = [p for p in root.rglob('*') if p.is_file() and not any(part in ('.git','dist','__pycache__') for part in p.relative_to(root).parts)]
    for p in files:
        if p.suffix not in ('.md','.json','.yaml','.yml'):
            continue
        text = p.read_text()
        if re.search(r'/Users/[^\s/]+/|/home/[^\s/]+/|\b(?:ghp_|github_pat_|hf_)[A-Za-z0-9]{25,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',text):
            problems.append(f'Private/credential-shaped content: {p.relative_to(root)}')
        for owner,repo in re.findall(r'https://github.com/([^/\s]+)/([^/\s)#]+)',text):
            if owner=='OpenTechnology14' and repo!='AgentWorkflows':
                problems.append(f'Project-specific source URL: {p.relative_to(root)}')
        if p.suffix!='.md':
            continue
        # Fenced examples are data, not documentation navigation.
        prose=re.sub(r'^```.*?^```[^\n]*$', '', text,flags=re.M|re.S)
        for target in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)',prose):
            u=urlsplit(target)
            if u.scheme or u.netloc:
                continue
            destination=(p.parent/unquote(u.path)).resolve() if u.path else p
            count+=1
            if not destination.is_relative_to(root.resolve()) or not destination.is_file():
                problems.append(f'Broken/escaping link: {p.relative_to(root)} -> {target}')
    marketplace=json.loads((root/'.agents/plugins/marketplace.json').read_text())
    plugin=(root/marketplace['plugins'][0]['source']['path']).resolve()
    if not plugin.is_relative_to(root.resolve()) or not (plugin/'plugin.json').is_file():
        problems.append('Marketplace plugin path is invalid')
    if problems:
        raise ValueError('\n'.join(problems))
    return count

if __name__=='__main__':
    try:
        links=verify()
    except (ValueError,KeyError) as e:
        sys.exit(str(e))
    print(f'PASS: generated packages, public content indicators and {links} local links')
