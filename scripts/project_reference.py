"""Record/check immutable AgentWorkflows references; generate a focused CI adapter."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import re
import subprocess
import sys

REPOSITORY = 'https://github.com/OpenTechnology14/AgentWorkflows'
RECORD = '.agent-workflows.json'
CI_PATH = '.github/workflows/agent-workflows-reference.yml'
UPSTREAM = 'refs/heads/main'

class ReferenceError(ValueError):
    pass

def git(library, *args):
    return subprocess.check_output(['git','-C',str(library),*args],text=True,stderr=subprocess.PIPE,timeout=20).strip()

def file_at(root, relative):
    if not isinstance(relative,str):
        raise ReferenceError('A relative file path is required')
    path=PurePosixPath(relative)
    if path.is_absolute() or '..' in path.parts or '\\' in relative or path.as_posix()!=relative:
        raise ReferenceError('Unsafe relative path')
    target=root/relative
    if not target.resolve().is_relative_to(root.resolve()):
        raise ReferenceError('Path escapes root')
    current=root
    for part in path.parts:
        current=current/part
        if current.is_symlink():
            raise ReferenceError('Symlink reference is not accepted')
    return target

def source_files(library):
    manifest=json.loads(file_at(library,'packaging/manifest.json').read_text())
    references=manifest['references']
    if not isinstance(references,list) or len(references)!=len(set(references)):
        raise ReferenceError('Invalid source reference list')
    if any(not re.fullmatch(r'(workflows|templates)/[A-Z_]+\.md',p) for p in references):
        raise ReferenceError('Only generic workflow/template references are accepted')
    return sorted(['packaging/manifest.json','packaging/ENTRYPOINT.md','scripts/project_reference.py',*references])

def load_record(project):
    lock=json.loads(file_at(project,RECORD).read_text())
    if set(lock)!= {'schema','repository','revision','upstream','guide','files'}:
        raise ReferenceError('Unexpected fields in reference record')
    if lock.get('schema')!=1 or lock.get('repository')!=REPOSITORY or lock.get('upstream')!=UPSTREAM:
        raise ReferenceError('Unsupported reference schema/repository/upstream')
    if not re.fullmatch(r'[0-9a-f]{40}',lock.get('revision','')):
        raise ReferenceError('Immutable 40-character Git revision required')
    if not isinstance(lock.get('files'),dict) or not lock['files']:
        raise ReferenceError('Nonempty source hashes required')
    for path,digest in lock['files'].items():
        if path not in ('packaging/manifest.json','packaging/ENTRYPOINT.md','scripts/project_reference.py') and not re.fullmatch(r'(workflows|templates)/[A-Z_]+\.md',path):
            raise ReferenceError('Unexpected source path in reference record')
        if not isinstance(digest,str) or not re.fullmatch(r'[0-9a-f]{64}',digest):
            raise ReferenceError('SHA-256 source hash required')
    if not file_at(project,lock.get('guide')).is_file():
        raise ReferenceError('Project guide is missing')
    return lock

def inspect(project,library,upstream_revision=None):
    project=project.resolve();library=library.resolve()
    lock=load_record(project)
    if git(library,'remote','get-url','origin').removesuffix('.git').rstrip('/')!=REPOSITORY:
        raise ReferenceError('Library checkout does not point to the public source repository')
    actual_revision=git(library,'rev-parse','HEAD')
    changed=[]
    if sorted(lock['files'])!=source_files(library):
        changed.append('source-file-list')
    for relative,expected in lock['files'].items():
        path=file_at(library,relative)
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
            changed.append(relative)
    result={'state':'current-local','acceptedRevision':lock['revision'],'libraryRevision':actual_revision,'upstream':'not-checked','changed':changed}
    if changed:
        result['state']='content-drift'
    elif actual_revision!=lock['revision']:
        result['state']='revision-drift'
    if upstream_revision is not None:
        if not re.fullmatch(r'[0-9a-f]{40}',upstream_revision):
            raise ReferenceError('Invalid upstream revision')
        result['upstreamRevision']=upstream_revision
        result['upstream']='current' if upstream_revision==lock['revision'] else 'different'
        if result['state']=='current-local':
            result['state']='current' if result['upstream']=='current' else 'upstream-drift'
    return result

def record(project,library,guide):
    project=project.resolve();library=library.resolve()
    if not file_at(project,guide).is_file():
        raise ReferenceError('Read the existing project guide before recording adoption')
    if git(library,'remote','get-url','origin').removesuffix('.git').rstrip('/')!=REPOSITORY:
        raise ReferenceError('Unexpected library repository')
    revision=git(library,'rev-parse','HEAD')
    sources=source_files(library)
    hashes={}
    for path in sources:
        data=file_at(library,path).read_bytes()
        committed=subprocess.check_output(['git','-C',str(library),'show',f'{revision}:{path}'],stderr=subprocess.PIPE,timeout=20)
        if data!=committed:
            raise ReferenceError(f'Uncommitted source: {path}')
        hashes[path]=hashlib.sha256(data).hexdigest()
    target=file_at(project,RECORD)
    if target.exists():
        load_record(project)  # Preserve unrelated/foreign configuration rather than replacing it.
    value={'schema':1,'repository':REPOSITORY,'revision':revision,'upstream':UPSTREAM,'guide':guide,'files':hashes}
    target.write_text(json.dumps(value,indent=2)+'\n')
    return value

def workflow(lock):
    sha=lock['revision']
    return f'''# Generated by AgentWorkflows scripts/project_reference.py ci; update with the reference record.
name: Agent workflow reference
on:
  push:
  pull_request:
  workflow_dispatch:
permissions:
  contents: read
jobs:
  reference:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262
      - uses: actions/checkout@11d5960a326750d5838078e36cf38b85af677262
        with:
          repository: OpenTechnology14/AgentWorkflows
          ref: {sha}
          path: .agent-workflows-library
          persist-credentials: false
      - run: python3 .agent-workflows-library/scripts/project_reference.py check --project . --library .agent-workflows-library --upstream
'''

def check_ci(project,lock):
    path=file_at(project,CI_PATH)
    if path.exists() and path.read_text()!=workflow(lock):
        raise ReferenceError('Generated reference CI differs; regenerate it with ci')

def read_upstream():
    completed=subprocess.run(['git','ls-remote','--exit-code',REPOSITORY+'.git',UPSTREAM],check=True,capture_output=True,text=True,timeout=20)
    result=completed.stdout.split()
    if len(result)!=2 or result[1]!=UPSTREAM:
        raise ReferenceError('Upstream response is unavailable or malformed')
    return result[0]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['record','check','ci'])
    parser.add_argument('--project',type=Path,required=True)
    parser.add_argument('--library',type=Path,required=True)
    parser.add_argument('--guide')
    parser.add_argument('--upstream',action='store_true')
    args=parser.parse_args()
    try:
        if args.command=='record':
            if not args.guide:
                raise ReferenceError('record requires --guide')
            lock=record(args.project,args.library,args.guide)
            result={'state':'recorded','revision':lock['revision']}
        elif args.command=='ci':
            lock=load_record(args.project)
            result=inspect(args.project,args.library)
            if result['state']!='current-local':
                raise ReferenceError('Check the accepted local library before generating CI')
            target=file_at(args.project,CI_PATH)
            if target.exists() and not target.read_text().startswith('# Generated by AgentWorkflows scripts/project_reference.py ci;'):
                raise ReferenceError('Existing CI file is not owned by this generator')
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(workflow(lock))
            result={'state':'ci-recorded','revision':lock['revision']}
        else:
            result=inspect(args.project,args.library)
            check_ci(args.project,load_record(args.project))
            if args.upstream:
                try:
                    latest=read_upstream()
                except (subprocess.SubprocessError,OSError,ReferenceError):
                    result['upstream']='unavailable'
                    print(json.dumps(result,sort_keys=True))
                    return 2
                result=inspect(args.project,args.library,latest)
            print(json.dumps(result,sort_keys=True))
            return 0 if result['state'] in ('current','current-local') else 1
        print(json.dumps(result,sort_keys=True))
        return 0
    except (ReferenceError,KeyError,TypeError,OSError,json.JSONDecodeError,subprocess.SubprocessError) as e:
        print(json.dumps({'state':'invalid-or-unavailable','detail':str(e)}))
        return 2

if __name__=='__main__':
    sys.exit(main())
