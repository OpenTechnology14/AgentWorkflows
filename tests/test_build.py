"""Observable packaging invariants; no paid model calls or live installations."""
from pathlib import Path
import io
import json
import posixpath
import re
import shutil
import sys
import tempfile
import unittest
import zipfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build import ROOT, render, synchronize, SKILL

class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name).resolve()
        for directory in ('packaging','workflows','templates'):
            shutil.copytree(ROOT/directory,self.root/directory)
        for file in ('LICENSE','CLAUDE.md'):
            shutil.copy2(ROOT/file,self.root/file)
    def tearDown(self):
        self.temp.cleanup()
    def edit_manifest(self,edit):
        p=self.root/'packaging/manifest.json';m=json.loads(p.read_text());edit(m);p.write_text(json.dumps(m))
    def test_repeated_builds_are_identical(self):
        self.assertEqual(render(self.root),render(self.root))
        synchronize(self.root)
        self.assertEqual(render(self.root),{p:(self.root/p).read_bytes() for p in render(self.root)})
    def test_undeclared_records_are_not_exported(self):
        (self.root/'workflows/PRIVATE.md').write_text('DO_NOT_EXPORT_PRIVATE_RECORD')
        for data in render(self.root).values():self.assertNotIn(b'DO_NOT_EXPORT_PRIVATE_RECORD',data)
    def test_reference_change_reaches_all_formats(self):
        p=self.root/'workflows/BUGS.md';p.write_text(p.read_text()+'\nSYNTHETIC_CHANGED_CONTENT\n')
        out=render(self.root)
        self.assertIn(b'SYNTHETIC_CHANGED_CONTENT',out[SKILL+'/references/workflows/BUGS.md'])
        self.assertIn(b'SYNTHETIC_CHANGED_CONTENT',out['dist/chatgpt/KNOWLEDGE.md'])
        with zipfile.ZipFile(io.BytesIO(out['dist/agent-workflows-skill.zip'])) as z:
            self.assertIn(b'SYNTHETIC_CHANGED_CONTENT',z.read('agent-workflows/references/workflows/BUGS.md'))
    def test_traversal_is_rejected(self):
        self.edit_manifest(lambda m:m['references'].append('workflows/../../outside.md'))
        with self.assertRaises(ValueError):render(self.root)
    def test_duplicate_is_rejected(self):
        self.edit_manifest(lambda m:m['references'].append(m['references'][0]))
        with self.assertRaises(ValueError):render(self.root)
    def test_missing_input_is_rejected(self):
        (self.root/'workflows/BUGS.md').unlink()
        with self.assertRaises(ValueError):render(self.root)
    def test_symlink_input_is_rejected(self):
        p=self.root/'workflows/BUGS.md';p.unlink();p.symlink_to(self.root/'workflows/DESIGN.md')
        with self.assertRaises(ValueError):render(self.root)
    def test_check_detects_drift_without_writing(self):
        synchronize(self.root);p=self.root/(SKILL+'/SKILL.md');p.write_text('edited generated file')
        with self.assertRaises(ValueError):synchronize(self.root,check=True)
        self.assertEqual(p.read_text(),'edited generated file')
    def test_unknown_output_is_preserved_and_rejected(self):
        synchronize(self.root);p=self.root/'dist/keep.txt';p.write_text('preserve')
        with self.assertRaises(ValueError):synchronize(self.root)
        self.assertEqual(p.read_text(),'preserve')
    def test_output_symlink_is_rejected(self):
        outside=self.root/'outside';outside.mkdir();(self.root/'dist').symlink_to(outside,target_is_directory=True)
        with self.assertRaises(ValueError):synchronize(self.root)
        self.assertEqual(list(outside.iterdir()),[])
    def test_archives_have_portable_roots_and_license(self):
        out=render(self.root)
        with zipfile.ZipFile(io.BytesIO(out['dist/agent-workflows-plugin.zip'])) as z:
            self.assertIn('plugin.json',z.namelist());self.assertIn('LICENSE',z.namelist())
            self.assertIn('skills/agent-workflows/SKILL.md',z.namelist())
            self.assertTrue(all(not p.startswith('/') and '..' not in Path(p).parts for p in z.namelist()))
    def test_skill_archive_references_are_self_contained(self):
        out=render(self.root)
        with zipfile.ZipFile(io.BytesIO(out['dist/agent-workflows-skill.zip'])) as z:
            names=set(z.namelist())
            for name in names:
                if not name.endswith('.md'):continue
                for target in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)',z.read(name).decode()):
                    if '://' in target:continue
                    target=target.split('#')[0]
                    resolved=posixpath.normpath(posixpath.join(posixpath.dirname(name),target))
                    self.assertIn(resolved,names)
    def test_chat_pack_contains_no_host_filesystem_links(self):
        out=render(self.root)
        for name in ('INSTRUCTIONS.md','KNOWLEDGE.md'):
            text=out['dist/chatgpt/'+name].decode()
            for target in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)',text):
                self.assertTrue(target.startswith(('https://','http://')))
    def test_check_without_dist_supports_fresh_checkout(self):
        synchronize(self.root);shutil.rmtree(self.root/'dist')
        synchronize(self.root,check=True,include_dist=False)
        self.assertFalse((self.root/'dist').exists())

if __name__=='__main__':unittest.main()
