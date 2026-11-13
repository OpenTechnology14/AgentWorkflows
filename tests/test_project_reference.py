"""Reference checks use isolated Git fixtures and no live network/model calls."""
from pathlib import Path
import contextlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import project_reference as ref
ROOT=Path(__file__).resolve().parents[1]

class ReferenceTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        root=Path(self.temp.name).resolve();self.library=root/'library';self.project=root/'project'
        self.library.mkdir();self.project.mkdir()
        for directory in ['workflows','templates','packaging','docs']:
            shutil.copytree(ROOT/directory,self.library/directory)
        (self.library/'scripts').mkdir();shutil.copy2(ROOT/'scripts/project_reference.py',self.library/'scripts/project_reference.py')
        (self.project/'GUIDE.md').write_text('Synthetic guide with project authority.')
        def git(*args):return subprocess.check_output(['git','-C',str(self.library),*args],stderr=subprocess.PIPE,text=True).strip()
        self.git=git
        git('init','-b','main');git('config','user.name','Fixture');git('config','user.email','fixture@example.invalid')
        git('remote','add','origin',ref.REPOSITORY+'.git');git('add','.');git('commit','-qm','fixture')
        self.lock=ref.record(self.project,self.library,'GUIDE.md')
    def tearDown(self):self.temp.cleanup()
    def test_current_reference_uses_exact_source_revision_and_hashes(self):
        self.assertEqual(ref.inspect(self.project,self.library,self.lock['revision'])['state'],'current')
        self.assertNotIn(str(self.library),(self.project/ref.RECORD).read_text())
    def test_changed_source_is_reported(self):
        (self.library/'workflows/BUGS.md').write_text('Changed behavior')
        self.assertEqual(ref.inspect(self.project,self.library)['state'],'content-drift')
    def test_missing_source_is_reported(self):
        (self.library/'workflows/BUGS.md').unlink()
        self.assertIn('workflows/BUGS.md',ref.inspect(self.project,self.library)['changed'])
    def test_different_revision_is_not_current_even_when_content_matches(self):
        self.git('commit','--allow-empty','-qm','new commit')
        self.assertEqual(ref.inspect(self.project,self.library)['state'],'revision-drift')
    def test_upstream_change_is_not_silently_adopted(self):
        (self.library/'workflows/BUGS.md').write_text('Changed upstream source')
        self.git('add','.');self.git('commit','-qm','upstream change')
        upstream=self.git('rev-parse','HEAD');self.git('checkout','--detach',self.lock['revision'])
        result=ref.inspect(self.project,self.library,upstream)
        self.assertEqual(result['state'],'upstream-drift')
        self.assertEqual(ref.load_record(self.project)['revision'],self.lock['revision'])
    def test_merge_or_unrelated_upstream_commit_with_identical_sources_is_current(self):
        self.git('commit','--allow-empty','-qm','merge-equivalent metadata')
        upstream=self.git('rev-parse','HEAD');self.git('checkout','--detach',self.lock['revision'])
        result=ref.inspect(self.project,self.library,upstream)
        self.assertEqual(result['state'],'current')
        self.assertNotEqual(result['acceptedRevision'],result['upstreamRevision'])
    def test_unavailable_upstream_object_is_not_current(self):
        with self.assertRaises(ref.ReferenceError):ref.inspect(self.project,self.library,'1'*40)
    def test_cannot_record_dirty_source(self):
        (self.library/'workflows/BUGS.md').write_text('uncommitted')
        with self.assertRaises(ref.ReferenceError):ref.record(self.project,self.library,'GUIDE.md')
    def test_guide_escape_is_rejected(self):
        with self.assertRaises(ref.ReferenceError):ref.record(self.project,self.library,'../outside.md')
    def test_source_symlink_is_rejected(self):
        p=self.library/'workflows/BUGS.md';p.unlink();p.symlink_to(self.library/'workflows/DESIGN.md')
        with self.assertRaises(ref.ReferenceError):ref.inspect(self.project,self.library)
    def test_foreign_repository_is_rejected(self):
        self.git('remote','set-url','origin','https://example.invalid/other.git')
        with self.assertRaises(ref.ReferenceError):ref.inspect(self.project,self.library)
    def test_record_injection_is_rejected(self):
        p=self.project/ref.RECORD;d=json.loads(p.read_text());d['files']['../outside.md']='1'*64;p.write_text(json.dumps(d))
        with self.assertRaises(ref.ReferenceError):ref.load_record(self.project)
    def test_generated_ci_pins_source_and_detects_revision_drift(self):
        p=self.project/ref.CI_PATH;p.parent.mkdir(parents=True);p.write_text(ref.workflow(self.lock))
        ref.check_ci(self.project,self.lock)
        changed={**self.lock,'revision':'2'*40}
        with self.assertRaises(ref.ReferenceError):ref.check_ci(self.project,changed)
    def test_upstream_unavailability_is_reported_and_record_is_preserved(self):
        before=(self.project/ref.RECORD).read_bytes();stdout=io.StringIO()
        argv=['project_reference.py','check','--project',str(self.project),'--library',str(self.library),'--upstream']
        with patch.object(sys,'argv',argv),patch.object(ref,'read_upstream',side_effect=subprocess.TimeoutExpired('git',20)),contextlib.redirect_stdout(stdout):
            self.assertEqual(ref.main(),2)
        self.assertEqual(json.loads(stdout.getvalue())['upstream'],'unavailable')
        self.assertEqual((self.project/ref.RECORD).read_bytes(),before)

if __name__=='__main__':unittest.main()
