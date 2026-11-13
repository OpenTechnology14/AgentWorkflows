"""One list of intake Kinds: every file that lists them lists the same ones, in the same order."""
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
KINDS = ['idea', 'bug', 'simple change', 'proposal remainder', 'review finding', 'audit finding', 'housekeeping']

# Each place that lists the Kinds, with a pattern whose one group is the list text.
LISTS = [
    ('workflows/WORK_TYPES.md', r'^Kinds: (.+)$'),
    ('templates/INTAKE.md', r'^- Kind[^:\n]*: (.+)$'),
    ('workflows/PROMPT_TRANSLATION.md', r'^Kind: (.+)$'),
    ('packaging/ENTRYPOINT.md', r'exactly one Kind from \[work types\]\([^)]*\): ([^.(]+)'),
    ('README.md', r'^- \*\*One intake, one list of Kinds:\*\* (.+)$'),
]


def read(relative):
    return (ROOT / relative).read_text(encoding='utf-8')


def tokens(text):
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'[`*_.]', '', text)
    parts = re.split(r'\s*(?:/|\||,)\s*|\s+(?:and|or)\s+', text.strip())
    return [p.strip() for p in parts if p.strip()]


class WorkTypeTests(unittest.TestCase):
    def test_every_list_is_the_same_list(self):
        for relative, pattern in LISTS:
            with self.subTest(file=relative):
                match = re.search(pattern, read(relative), re.M)
                self.assertIsNotNone(match, f'{relative}: no Kind list found')
                self.assertEqual(tokens(match.group(1)), KINDS)

    def test_no_other_file_starts_its_own_list(self):
        known = {relative for relative, _ in LISTS}
        found = set()
        for folder in ('workflows', 'templates'):
            for path in sorted((ROOT / folder).glob('*.md')):
                relative = path.relative_to(ROOT).as_posix()
                if re.search(r'^\s*(?:- )?Kinds?\b[^:\n]*:', path.read_text(encoding='utf-8'), re.M):
                    found.add(relative)
        self.assertEqual(found - known, set(), 'a file lists Kinds that the test does not check')

    def test_each_kind_is_defined_once_in_the_table(self):
        text = read('workflows/WORK_TYPES.md')
        for kind in KINDS:
            with self.subTest(kind=kind):
                self.assertEqual(len(re.findall(rf'^\| {re.escape(kind)} \|', text, re.M)), 1)

    def test_types_and_gate_are_packaged_and_reachable(self):
        refs = json.loads(read('packaging/manifest.json'))['references']
        linked_from = ('workflows/README.md', 'packaging/ENTRYPOINT.md', 'workflows/INTAKE.md', 'workflows/STARTUP.md')
        for name in ('WORK_TYPES.md', 'ENTRY_GATE.md'):
            with self.subTest(workflow=name):
                self.assertIn('workflows/' + name, refs)
                for index in linked_from:
                    self.assertIn(name, read(index), f'{index} does not link {name}')

if __name__ == '__main__':
    unittest.main()
