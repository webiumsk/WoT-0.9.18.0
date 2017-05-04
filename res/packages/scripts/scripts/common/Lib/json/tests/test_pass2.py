# 2017.05.04 15:32:49 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/json/tests/test_pass2.py
from json.tests import PyTest, CTest
JSON = '\n[[[[[[[[[[[[[[[[[[["Not too deep"]]]]]]]]]]]]]]]]]]]\n'

class TestPass2(object):

    def test_parse(self):
        res = self.loads(JSON)
        out = self.dumps(res)
        self.assertEqual(res, self.loads(out))


class TestPyPass2(TestPass2, PyTest):
    pass


class TestCPass2(TestPass2, CTest):
    pass
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\json\tests\test_pass2.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:49 Støední Evropa (letní èas)
