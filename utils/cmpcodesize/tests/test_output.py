# test_output.py - Unit tests for cmpcodesize.output -*- python -*-
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

from cmpcodesize.output import Format, print_listed_function_sizes


class PrintListedFunctionSizesTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO.StringIO()

    def tearDown(self):
        self.out.close()

    def test_when_format_is_plaintext_outputs_plaintext(self):
        sizes = [
            {'size': 1, 'name': 'foo'},
            {'size': 10, 'name': 'bar'},
            {'size': 100, 'name': 'baz'},
        ]
        print_listed_function_sizes(sizes, Format.PLAINTEXT, out=self.out)
        self.assertEqual(self.out.getvalue().splitlines(), [
            '       1 foo',
            '      10 bar',
            '     100 baz',
        ])

if __name__ == '__main__':
    unittest.main()
