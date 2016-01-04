# cmpcodesize/csvutils.py - Transform dicts to CSV -*- python -*-
#
# This source file is part of the Swift.org open source project
#
# Copyright (c) 2014 - 2015 Apple Inc. and the Swift project authors
# Licensed under Apache License v2.0 with Runtime Library Exception
#
# See http://swift.org/LICENSE.txt for license information
# See http://swift.org/CONTRIBUTORS.txt for the list of Swift project authors

import csv


def write_csv(dicts, out):
    """
    Write an iterable series of dicts, as CSV, to the specified 'out'.
    The field names of the CSV are inferred from the first dict in the series.
    If the series is empty, output nothing.
    """
    try:
        first = next(dicts)
    except StopIteration:
        return

    writer = csv.DictWriter(out, fieldnames=sorted(first.keys()))
    writer.writeheader()
    writer.writerow(first)
    writer.writerows(dicts)
