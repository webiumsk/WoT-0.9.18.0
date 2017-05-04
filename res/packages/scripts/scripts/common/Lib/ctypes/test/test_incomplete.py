# 2017.05.04 15:31:25 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/ctypes/test/test_incomplete.py
import unittest
from ctypes import *

class MyTestCase(unittest.TestCase):

    def test_incomplete_example(self):
        lpcell = POINTER('cell')

        class cell(Structure):
            _fields_ = [('name', c_char_p), ('next', lpcell)]

        SetPointerType(lpcell, cell)
        c1 = cell()
        c1.name = 'foo'
        c2 = cell()
        c2.name = 'bar'
        c1.next = pointer(c2)
        c2.next = pointer(c1)
        p = c1
        result = []
        for i in range(8):
            result.append(p.name)
            p = p.next[0]

        self.assertEqual(result, ['foo', 'bar'] * 4)
        from ctypes import _pointer_type_cache
        del _pointer_type_cache[cell]


if __name__ == '__main__':
    unittest.main()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\ctypes\test\test_incomplete.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:31:25 St�edn� Evropa (letn� �as)
