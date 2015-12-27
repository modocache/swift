# swift_build_support/cmake.py - Detect host machine's CMake -*- python -*-
#
# This source file is part of the Swift.org open source project
#
# Copyright (c) 2014 - 2015 Apple Inc. and the Swift project authors
# Licensed under Apache License v2.0 with Runtime Library Exception
#
# See http://swift.org/LICENSE.txt for license information
# See http://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
#
# ----------------------------------------------------------------------------
#
# Find the path to a CMake executable on the host machine.
#
# ----------------------------------------------------------------------------

import os
import platform

from . import xcrun
from .which import which


def host_cmake(xcrun_toolchain):
    """
    If the 'CMAKE' environment variable is set, return that. Otherwise, find
    the path to `cmake`, using tools provided by the host platform.
    If `cmake` cannot be found, return None.
    """
    cmake = os.getenv('CMAKE', None)
    if cmake:
        return cmake

    if platform.system() == 'Darwin':
        return xcrun.find(xcrun_toolchain, 'cmake')
    else:
        cmake = which('cmake')
        if cmake:
            return cmake
        else:
            return '/usr/local/bin/cmake'
