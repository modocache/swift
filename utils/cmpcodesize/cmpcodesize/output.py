# cmpcodesize/output.py - Printing options for cmpcodesize -*- python -*-
#
# This source file is part of the Swift.org open source project
#
# Copyright (c) 2014 - 2015 Apple Inc. and the Swift project authors
# Licensed under Apache License v2.0 with Runtime Library Exception
#
# See http://swift.org/LICENSE.txt for license information
# See http://swift.org/CONTRIBUTORS.txt for the list of Swift project authors


from __future__ import absolute_import, print_function

import sys

from . import csvutils


class Format:
    """
    A class-based enum for output format options.
    """
    PLAINTEXT = 'plaintext'  # Plain text with no particular format.
    CSV = 'csv'


def _raise_unrecognized_format(format_option):
    """
    Raise an exception indicating the format option string provided
    is not valid.
    """
    raise ValueError('Unrecognized format option: {}'.format(format_option))


def print_plaintext(message, format_option, out=sys.stdout):
    """Print iff the format is plaintext."""
    if format_option == Format.CSV:
        pass
    elif format_option == Format.PLAINTEXT:
        print(message, file=out)
    else:
        _raise_unrecognized_format(format_option)


def print_listed_function_sizes(sizes, format_option, out=sys.stdout):
    """
    Prints the return value of cmpcodesize.compare.list_function_sizes to the
    designated output, based on the given formatting option.
    """
    if format_option == Format.CSV:
        csvutils.write_csv(sizes, out=out)
    elif format_option == Format.PLAINTEXT:
        for size in sizes:
            print('{:>8} {}'.format(size['size'], size['name']), file=out)
    else:
        _raise_unrecognized_format(format_option)


def print_compare_function_sizes(inBoth, format_option, out=sys.stdout):
    """
    TODO, inBoth is an array of triples: function name, old size, new size.
    """
    if format_option == Format.PLAINTEXT:
        sizeIncrease = 0
        sizeDecrease = 0
        inBothSize = 0
        print('%8s %8s %8s' % ('old', 'new', 'diff'), file=out)
        for triple in sorted(inBoth, key=lambda tup: (tup[2] - tup[1], tup[1])):
            func = triple[0]
            oldSize = triple[1]
            newSize = triple[2]
            diff = newSize - oldSize
            if diff > 0:
                sizeIncrease += diff
            else:
                sizeDecrease -= diff
            if diff == 0:
                inBothSize += newSize
            print('%8d %8d %8d %s' % (oldSize, newSize, newSize - oldSize, func),
                  file=out)

        print('Total size of functions with the same size in both '
              'files: {}'.format(inBothSize), file=out)
        print('Total size of functions that got smaller: '
              '{}'.format(sizeDecrease), file=out)
        print('Total size of functions that got bigger: '
              '{}'.format(sizeIncrease), file=out)
        print('Total size change of functions present in both files: '
              '{}'.format(sizeIncrease - sizeDecrease), file=out)
    elif format_option == Format.CSV:
        diffs = []
        for diff in inBoth:
            diffs.append({
                'name': diff[0],
                'old': diff[1],
                'new': diff[2],
                'diff': diff[2] - diff[1],
            })
        csvutils.write_csv(iter(diffs), out)
    else:
        _raise_unrecognized_format(format_option)
