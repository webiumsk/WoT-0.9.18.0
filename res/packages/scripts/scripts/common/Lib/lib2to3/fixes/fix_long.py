# 2017.05.04 15:33:13 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_long.py
"""Fixer that turns 'long' into 'int' everywhere.
"""
from lib2to3 import fixer_base
from lib2to3.fixer_util import is_probably_builtin

class FixLong(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "'long'"

    def transform(self, node, results):
        if is_probably_builtin(node):
            node.value = u'int'
            node.changed()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\fixes\fix_long.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:13 Støední Evropa (letní èas)
