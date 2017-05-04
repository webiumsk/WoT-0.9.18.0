# 2017.05.04 15:33:10 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_basestring.py
"""Fixer for basestring -> str."""
from .. import fixer_base
from ..fixer_util import Name

class FixBasestring(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "'basestring'"

    def transform(self, node, results):
        return Name(u'str', prefix=node.prefix)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\fixes\fix_basestring.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:10 Støední Evropa (letní èas)
