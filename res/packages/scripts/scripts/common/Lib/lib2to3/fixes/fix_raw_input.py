# 2017.05.04 15:33:14 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_raw_input.py
"""Fixer that changes raw_input(...) into input(...)."""
from .. import fixer_base
from ..fixer_util import Name

class FixRawInput(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              power< name='raw_input' trailer< '(' [any] ')' > any* >\n              "

    def transform(self, node, results):
        name = results['name']
        name.replace(Name(u'input', prefix=name.prefix))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\fixes\fix_raw_input.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:15 Støední Evropa (letní èas)
