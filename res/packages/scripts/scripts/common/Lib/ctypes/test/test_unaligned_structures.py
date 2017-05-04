# 2017.05.04 15:31:30 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/ctypes/test/test_unaligned_structures.py
import sys, unittest
from ctypes import *
structures = []
byteswapped_structures = []
if sys.byteorder == 'little':
    SwappedStructure = BigEndianStructure
else:
    SwappedStructure = LittleEndianStructure
for typ in [c_short,
 c_int,
 c_long,
 c_longlong,
 c_float,
 c_double,
 c_ushort,
 c_uint,
 c_ulong,
 c_ulonglong]:

    class X(Structure):
        _pack_ = 1
        _fields_ = [('pad', c_byte), ('value', typ)]


    class Y(SwappedStructure):
        _pack_ = 1
        _fields_ = [('pad', c_byte), ('value', typ)]


    structures.append(X)
    byteswapped_structures.append(Y)

class TestStructures(unittest.TestCase):

    def test_native(self):
        for typ in structures:
            self.assertEqual(typ.value.offset, 1)
            o = typ()
            o.value = 4
            self.assertEqual(o.value, 4)

    def test_swapped(self):
        for typ in byteswapped_structures:
            self.assertEqual(typ.value.offset, 1)
            o = typ()
            o.value = 4
            self.assertEqual(o.value, 4)


if __name__ == '__main__':
    unittest.main()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\ctypes\test\test_unaligned_structures.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:31:30 Støední Evropa (letní èas)
