# 2017.05.04 15:31:25 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/ctypes/test/test_libc.py
import unittest
from ctypes import *
import _ctypes_test
lib = CDLL(_ctypes_test.__file__)

class LibTest(unittest.TestCase):

    def test_sqrt(self):
        lib.my_sqrt.argtypes = (c_double,)
        lib.my_sqrt.restype = c_double
        self.assertEqual(lib.my_sqrt(4.0), 2.0)
        import math
        self.assertEqual(lib.my_sqrt(2.0), math.sqrt(2.0))

    def test_qsort(self):
        comparefunc = CFUNCTYPE(c_int, POINTER(c_char), POINTER(c_char))
        lib.my_qsort.argtypes = (c_void_p,
         c_size_t,
         c_size_t,
         comparefunc)
        lib.my_qsort.restype = None

        def sort(a, b):
            return cmp(a[0], b[0])

        chars = create_string_buffer('spam, spam, and spam')
        lib.my_qsort(chars, len(chars) - 1, sizeof(c_char), comparefunc(sort))
        self.assertEqual(chars.raw, '   ,,aaaadmmmnpppsss\x00')
        return


if __name__ == '__main__':
    unittest.main()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\ctypes\test\test_libc.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:31:25 St�edn� Evropa (letn� �as)
