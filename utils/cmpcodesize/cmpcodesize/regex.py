import re


# Cache the compiled regular expressions into global objects.
_ARCHITECTURE_REGEX = re.compile('architecture\s(\S+)')
_SECTION_REGEX = re.compile('\s+sectname\s(\S+)')
_SIZE_REGEX = re.compile('\s+size\s([\da-fA-Fx]+)')
_ADDRESS_REGEX = re.compile('^([\da-fA-F]+)\s')
_LABEL_REGEX = re.compile('^((\-*\[[^\]]*\])|[^\/\s]+):$')


def architecture(fat_headers):
    """
    Given a string representing fat headers from an executable,
    returns one of the following:

    1. arm64, if that is one of the architectures listed.
    2. If arm64 us not listed, the first architecture that is listed.
    3. None, if no architectures are listed.
    """
    result = None
    for line in fat_headers.splitlines():
        match = _ARCHITECTURE_REGEX.match(line)
        if match:
            arch = match.group(1)
            if arch == 'arm64':
                return arch
            elif result is None:
                result = match.group(1)
    return result


def section(line):
    """
    Given a string representing a line from a series of load commands,
    returns the section name if specified. For example, the line
    '  sectname __common' returns '__common'. If the line does not contain
    a section name, returns None.
    """
    match = _SECTION_REGEX.match(line)
    if match:
        return match.group(1)
    else:
        return None


def size(line):
    """
    Given a string representing a line from a series of load commands,
    returns an integer representing the size, if the size appears in the line.
    For example, the line '      size 0x0000000000000810' returns 2064.
    If no size appears in the line, returns None.
    """
    match = _SIZE_REGEX.match(line)
    if match:
        return int(match.group(1), 16)
    else:
        return None


def address(line):
    """
    Given a string representing a line from a series of load commands,
    returns an integer representing the address of the command, if the address
    appears in the line. For example, the line
    '0000000000051e0a    movq    -0xe8(%rbp), %r10' returns 335370.
    If no address appears in the line, returns None.
    """
    match = _ADDRESS_REGEX.match(line)
    if match:
        return int(match.group(1), 16)
    else:
        return None


def label(line):
    """
    Given a string representing a line from a series of load commands,
    returns the label marking the beginning of a section of commands, if the
    label appears in the line. For example, the line
    '_swift_stdlib_readLine_stdin:' returns '_swift_stdlib_readLine_stdin'.
    If no label appears in the line, returns None.
    """
    match = _LABEL_REGEX.match(line)
    if match:
        return match.group(1)
    else:
        return None
