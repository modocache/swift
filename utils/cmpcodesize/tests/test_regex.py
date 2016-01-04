import unittest

from cmpcodesize import regex


class ArchitectureTestCase(unittest.TestCase):
    def test_no_architectures_listed_returns_none(self):
        headers = 'Fat headers\n' + \
                  '    cputype CPU_TYPE_X86_64\n'
        self.assertIsNone(regex.architecture(headers))

    def test_arm64_listed_returns_arm64(self):
        headers = 'Fat headers\n' + \
                  'architecture x86_64\n' + \
                  '    cputype CPU_TYPE_X86_64\n' + \
                  'architecture arm64\n' + \
                  '    cputype CPU_TYPE_ARM64\n'
        self.assertEqual(regex.architecture(headers), 'arm64')

    def test_arm64_not_listed_returns_first(self):
        headers = 'Fat headers\n' + \
                  'architecture x86_64\n' + \
                  '    cputype CPU_TYPE_X86_64\n' + \
                  'architecture i386\n' + \
                  '    cputype CPU_TYPE_I386\n'
        self.assertEqual(regex.architecture(headers), 'x86_64')

    def test_libswiftcore_x86_64(self):
        # These are the headers for libswiftCore.dylib when built
        # for a Darwin x86_64 target.
        headers = 'Fat headers\n' + \
                  'fat_magic FAT_MAGIC\n' + \
                  'nfat_arch 1\n' + \
                  'architecture x86_64\n' + \
                  '    cputype CPU_TYPE_X86_64\n' + \
                  '    cpusubtype CPU_SUBTYPE_X86_64_ALL\n' + \
                  '    capabilities 0x0\n' + \
                  '    offset 4096\n' + \
                  '    size 9029488\n' + \
                  '    align 2^12 (4096)\n'
        self.assertEqual(regex.architecture(headers), 'x86_64')


class SectionTestCase(unittest.TestCase):
    def test_no_section_included_returns_none(self):
        self.assertIsNone(regex.section('size 0x0001'))

    def test_section_included_returns_section(self):
        self.assertEqual(regex.section('  sectname __data'), '__data')


class SizeTestCase(unittest.TestCase):
    def test_no_size_included_returns_none(self):
        self.assertIsNone(regex.size('  sectname __objc_data'))

    def test_size_included_returns_section(self):
        self.assertEqual(regex.size('      size 0x0000000000000768'),
                         1896)


class AddressTestCase(unittest.TestCase):
    def test_no_address_included_returns_none(self):
        self.assertIsNone(regex.address('size 0x0001'))

    def test_address_included_returns_section(self):
        self.assertEqual(regex.address('00000000001fa370    callq   0x47a8c0'),
                         2073456)


class LabelTestCase(unittest.TestCase):
    def test_no_label_included_returns_none(self):
        self.assertIsNone(regex.label('size 0x0001'))

    def test_label_included_returns_section(self):
        self.assertEqual(regex.label('__ZNK4llvm9StringRef5splitEc:'),
                         '__ZNK4llvm9StringRef5splitEc')
