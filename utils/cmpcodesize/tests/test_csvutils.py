# test_csvutils.py - Unit tests for cmpcodesize.csvutils -*- python -*-
#
# This source file is part of the Swift.org open source project
#
# Copyright (c) 2014 - 2015 Apple Inc. and the Swift project authors
# Licensed under Apache License v2.0 with Runtime Library Exception
#
# See http://swift.org/LICENSE.txt for license information
# See http://swift.org/CONTRIBUTORS.txt for the list of Swift project authors

import StringIO
import unittest

from cmpcodesize.csvutils import write_csv


class WriteCsvTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO.StringIO()

    def tearDown(self):
        self.out.close()

    def test_when_dicts_is_empty_writes_nothing(self):
        write_csv(iter([]), out=self.out)
        self.assertEqual(self.out.getvalue(), '')

    def test_when_dicts_is_not_empty_writes_csv(self):
        dicts = [
            {'foo': 0, 'bar': 1, 'baz': 2},
            {'foo': 3, 'bar': 4, 'baz': 5},
            {'foo': 6, 'bar': 7, 'baz': 8},
        ]
        write_csv(iter(dicts), out=self.out)
        self.assertEqual(self.out.getvalue().splitlines(), [
            'bar,baz,foo',
            '1,2,0',
            '4,5,3',
            '7,8,6',
        ])


if __name__ == '__main__':
    unittest.main()
