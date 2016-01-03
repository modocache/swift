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
        raise ValueError(
            'Unrecognized format option: {}'.format(format_option))
