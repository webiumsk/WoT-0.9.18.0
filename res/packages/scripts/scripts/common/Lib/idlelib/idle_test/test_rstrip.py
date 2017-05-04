# 2017.05.04 15:32:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/idlelib/idle_test/test_rstrip.py
import unittest
import idlelib.RstripExtension as rs
from idlelib.idle_test.mock_idle import Editor

class rstripTest(unittest.TestCase):

    def test_rstrip_line(self):
        editor = Editor()
        text = editor.text
        do_rstrip = rs.RstripExtension(editor).do_rstrip
        do_rstrip()
        self.assertEqual(text.get('1.0', 'insert'), '')
        text.insert('1.0', '     ')
        do_rstrip()
        self.assertEqual(text.get('1.0', 'insert'), '')
        text.insert('1.0', '     \n')
        do_rstrip()
        self.assertEqual(text.get('1.0', 'insert'), '\n')

    def test_rstrip_multiple(self):
        editor = Editor()
        text = editor.text
        do_rstrip = rs.RstripExtension(editor).do_rstrip
        original = 'Line with an ending tab    \nLine ending in 5 spaces     \nLinewithnospaces\n    indented line\n    indented line with trailing space \n    '
        stripped = 'Line with an ending tab\nLine ending in 5 spaces\nLinewithnospaces\n    indented line\n    indented line with trailing space\n'
        text.insert('1.0', original)
        do_rstrip()
        self.assertEqual(text.get('1.0', 'insert'), stripped)


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\idlelib\idle_test\test_rstrip.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:45 St�edn� Evropa (letn� �as)
