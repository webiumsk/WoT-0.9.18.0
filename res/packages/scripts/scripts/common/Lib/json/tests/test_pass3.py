# 2017.05.04 15:32:49 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/json/tests/test_pass3.py
from json.tests import PyTest, CTest
JSON = '\n{\n    "JSON Test Pattern pass3": {\n        "The outermost value": "must be an object or array.",\n        "In this test": "It is an object."\n    }\n}\n'

class TestPass3(object):

    def test_parse(self):
        res = self.loads(JSON)
        out = self.dumps(res)
        self.assertEqual(res, self.loads(out))


class TestPyPass3(TestPass3, PyTest):
    pass


class TestCPass3(TestPass3, CTest):
    pass
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\json\tests\test_pass3.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:49 Støední Evropa (letní èas)
