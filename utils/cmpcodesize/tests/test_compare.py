# test_compare.py - Unit tests for cmpcodesize.compare -*- python -*-
#
# This source file is part of the Swift.org open source project
#
# Copyright (c) 2014 - 2016 Apple Inc. and the Swift project authors
# Licensed under Apache License v2.0 with Runtime Library Exception
#
# See http://swift.org/LICENSE.txt for license information
# See http://swift.org/CONTRIBUTORS.txt for the list of Swift project authors

import unittest

from cmpcodesize.compare import list_function_sizes


class ListFunctionSizesTestCase(unittest.TestCase):
    def test_when_sizes_is_none_raises(self):
        with self.assertRaises(TypeError):
            list(list_function_sizes(None))

    def test_when_sizes_is_empty_returns_empty(self):
        self.assertEqual(list(list_function_sizes([])), [])

    def test_lists_each_entry(self):
        sizes = {
            'foo': 1,
            'bar': 10,
            'baz': 100,
        }
        self.assertEqual(list(list_function_sizes(sizes.items())), [
            {'size': 1, 'name': 'foo'},
            {'size': 10, 'name': 'bar'},
            {'size': 100, 'name': 'baz'},
        ])


class OutputCompareFunctionSizesTestCase(unittest.TestCase):
    def test_when_format_is_plaintext_(self):
        pass

    def test_when_format_is_csv_(self):
        pass

if __name__ == '__main__':
    unittest.main()
