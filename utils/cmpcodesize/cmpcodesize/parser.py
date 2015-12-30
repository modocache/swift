from __future__ import absolute_import

import collections

from . import regex


MachOLabel = collections.namedtuple('MachOLabel',
                                    'name start_address end_address')
MachOSection = collections.namedtuple('MachOSection', 'name size')


def parse(content):
    """
    Enumerates each line of the content, yielding objects that represent the
    span of assembly for sections and labels.
    """
    # We enumerate each line of the content, yielding objects
    # that represent the span of assembly for sections...
    current_section_name = None
    current_section_size = 0
    # ...as well as for labels.
    current_label_name = None
    current_label_start_address = None
    # Throughout the process we'll keep track of our current address.
    current_address = None

    for line in content.splitlines():
        # Each line falls into one of these four categories.
        address = regex.address(line)
        label = regex.label(line)
        size = regex.size(line)
        section = regex.section(line)

        if address is not None:
            # We're reading more assembly for the current label or section.
            # Update our current address.
            current_address = address
            # If we haven't yet recorded a start address for this label,
            # use the current address.
            if current_label_start_address is None:
                current_label_start_address = address

        elif section is not None:
            # We're entering a new section. If we're currently measuring the
            # span of a section, we may yield that measurement.
            if current_section_name is not None:
                yield MachOSection(
                    name=current_section_name,
                    size=current_section_size)
            # Now that we've yielded the previous section, we update
            # the current section name and reset its start address.
            current_section_name = section
            current_section_size = 0

        elif size is not None:
            # We're reading more sizes for our current section.
            current_section_size += size

        elif label is not None:
            # We've encountered a new label. If we're currently measuring the
            # span of a label, we may yield that measurement.
            if (current_label_name is not None and
                    current_label_start_address is not None and
                    current_address is not None):
                yield MachOLabel(
                    name=current_label_name,
                    start_address=current_label_start_address,
                    end_address=current_address)
            # Now that we've yielded the previous label, we update
            # the current label name and reset its start address.
            current_label_name = label
            current_label_start_address = None

    # Finally, we yield the last region we were parsing when we reached the
    # end of the lines.
    if (current_label_name is not None and
            current_label_start_address is not None and
            current_address is not None):
        yield MachOLabel(
            name=current_label_name,
            start_address=current_label_start_address,
            end_address=current_address)
    if current_section_name is not None:
        yield MachOSection(
            name=current_section_name,
            size=current_section_size)
