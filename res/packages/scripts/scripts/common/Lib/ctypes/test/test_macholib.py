# 2017.05.04 15:31:26 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/ctypes/test/test_macholib.py
import os
import sys
import unittest
from ctypes.macholib.dyld import dyld_find

def find_lib(name):
    possible = ['lib' + name + '.dylib', name + '.dylib', name + '.framework/' + name]
    for dylib in possible:
        try:
            return os.path.realpath(dyld_find(dylib))
        except ValueError:
            pass

    raise ValueError('%s not found' % (name,))


class MachOTest(unittest.TestCase):
    if sys.platform == 'darwin':

        def test_find(self):
            self.assertEqual(find_lib('pthread'), '/usr/lib/libSystem.B.dylib')
            result = find_lib('z')
            self.assertRegexpMatches(result, '.*/lib/libz\\..*.*\\.dylib')
            self.assertEqual(find_lib('IOKit'), '/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit')


if __name__ == '__main__':
    unittest.main()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\ctypes\test\test_macholib.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:31:26 St�edn� Evropa (letn� �as)
