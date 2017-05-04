# 2017.05.04 15:32:39 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/idlelib/RstripExtension.py
"""Provides "Strip trailing whitespace" under the "Format" menu."""

class RstripExtension:
    menudefs = [('format', [None, ('Strip trailing whitespace', '<<do-rstrip>>')])]

    def __init__(self, editwin):
        self.editwin = editwin
        self.editwin.text.bind('<<do-rstrip>>', self.do_rstrip)

    def do_rstrip(self, event = None):
        text = self.editwin.text
        undo = self.editwin.undo
        undo.undo_block_start()
        end_line = int(float(text.index('end')))
        for cur in range(1, end_line):
            txt = text.get('%i.0' % cur, '%i.end' % cur)
            raw = len(txt)
            cut = len(txt.rstrip())
            if cut < raw:
                text.delete('%i.%i' % (cur, cut), '%i.end' % cur)

        undo.undo_block_stop()


if __name__ == '__main__':
    import unittest
    unittest.main('idlelib.idle_test.test_rstrip', verbosity=2, exit=False)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\idlelib\RstripExtension.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:39 Støední Evropa (letní èas)
