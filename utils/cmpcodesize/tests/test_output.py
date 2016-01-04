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

from cmpcodesize.output import (
    Format,
    print_compare_function_sizes,
    print_listed_function_sizes,
    print_plaintext,
)


class PrintCompareFunctionSizesTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO.StringIO()

    def tearDown(self):
        self.out.close()

    def test_when_format_is_plaintext_but_input_is_none_raises(self):
        with self.assertRaises(TypeError):
            print_compare_function_sizes(None, Format.PLAINTEXT, out=self.out)

    def test_when_format_is_plaintext_but_input_is_empty_prints_zeros(self):
        print_compare_function_sizes([], Format.PLAINTEXT, out=self.out)
        self.assertEqual(self.out.getvalue().splitlines(), [
            '     old      new     diff',
            'Total size of functions with the same size in both files: 0',
            'Total size of functions that got smaller: 0',
            'Total size of functions that got bigger: 0',
            'Total size change of functions present in both files: 0',
        ])

    def test_when_format_is_plaintext_and_input_is_not_empty_prints(self):
        print_compare_function_sizes([
            ('foo', 4, 10),
            ('bar', 10, 4),
            ('baz', 4, 4),
        ], Format.PLAINTEXT, out=self.out)
        self.assertEqual(self.out.getvalue().splitlines(), [
            '     old      new     diff',
            '      10        4       -6 bar',
            '       4        4        0 baz',
            '       4       10        6 foo',
            'Total size of functions with the same size in both files: 4',
            'Total size of functions that got smaller: 6',
            'Total size of functions that got bigger: 6',
            'Total size change of functions present in both files: 0',
        ])

    def test_when_format_is_csv_but_input_is_none_raises(self):
        with self.assertRaises(TypeError):
            print_compare_function_sizes(None, Format.CSV, out=self.out)

    def test_when_format_is_csv_but_input_is_empty_does_not_print(self):
        print_compare_function_sizes([], Format.CSV, out=self.out)
        self.assertEqual(self.out.getvalue(), '')

    def test_when_format_is_csv_and_input_is_not_empty_prints(self):
        print_compare_function_sizes([
            ('foo', 4, 10),
            ('bar', 10, 4),
            ('baz', 4, 4),
        ], Format.CSV, out=self.out)
        self.assertEqual(self.out.getvalue().splitlines(), [
            'diff,name,new,old',
            '6,foo,10,4',
            '-6,bar,4,10',
            '0,baz,4,4'
        ])


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


class PrintPlaintextTestCase(unittest.TestCase):
    def setUp(self):
        self.out = StringIO.StringIO()

    def tearDown(self):
        self.out.close()

    def test_when_format_is_plaintext_prints(self):
        print_plaintext('foo', Format.PLAINTEXT, self.out)
        self.assertEqual(self.out.getvalue(), 'foo\n')

    def test_when_format_is_not_plaintext_does_not_print(self):
        print_plaintext('bar', Format.CSV, self.out)
        self.assertEqual(self.out.getvalue(), '')

if __name__ == '__main__':
    unittest.main()
