import os
import unittest

from cmpcodesize.parser import parse


class ParseTestCase(unittest.TestCase):
    def setUp(self):
        self.fixtures_dir = os.path.join(os.path.dirname(__file__), 'fixtures')

    def test_fixture(self):
        fixture = os.path.join(
            self.fixtures_dir, 'test_parser_test_fixture.txt')
        with open(fixture) as f:
            regions = list(parse(f.read()))

            self.assertEqual(regions[0].name, '__text')
            self.assertEqual(regions[0].size, 5036917)

            self.assertEqual(regions[1].name, '__stubs')
            self.assertEqual(regions[1].size, 1194)

            self.assertEqual(regions[2].name, '__TFs10minElementuRxs12__')
            self.assertEqual(regions[2].start_address, 10768)
            self.assertEqual(regions[2].end_address, 10975)

            self.assertEqual(regions[3].name, '__TFSSCfT21_builtinString')
            self.assertEqual(regions[3].start_address, 11152)
            self.assertEqual(regions[3].end_address, 11807)

            self.assertEqual(regions[4].name, '__bss')
            self.assertEqual(regions[4].size, 1896)
