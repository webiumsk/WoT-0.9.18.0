# 2017.05.04 15:32:48 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/json/tests/test_float.py
import math
from json.tests import PyTest, CTest

class TestFloat(object):

    def test_floats(self):
        for num in [1617161771.765,
         math.pi,
         math.pi ** 100,
         math.pi ** (-100),
         3.1]:
            self.assertEqual(float(self.dumps(num)), num)
            self.assertEqual(self.loads(self.dumps(num)), num)
            self.assertEqual(self.loads(unicode(self.dumps(num))), num)

    def test_ints(self):
        for num in [1,
         1L,
         4294967296L,
         18446744073709551616L]:
            self.assertEqual(self.dumps(num), str(num))
            self.assertEqual(int(self.dumps(num)), num)
            self.assertEqual(self.loads(self.dumps(num)), num)
            self.assertEqual(self.loads(unicode(self.dumps(num))), num)

    def test_out_of_range(self):
        self.assertEqual(self.loads('[23456789012E666]'), [float('inf')])
        self.assertEqual(self.loads('[-23456789012E666]'), [float('-inf')])

    def test_allow_nan(self):
        for val in (float('inf'), float('-inf'), float('nan')):
            out = self.dumps([val])
            if val == val:
                self.assertEqual(self.loads(out), [val])
            else:
                res = self.loads(out)
                self.assertEqual(len(res), 1)
                self.assertNotEqual(res[0], res[0])
            self.assertRaises(ValueError, self.dumps, [val], allow_nan=False)


class TestPyFloat(TestFloat, PyTest):
    pass


class TestCFloat(TestFloat, CTest):
    pass
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\json\tests\test_float.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:49 St�edn� Evropa (letn� �as)
