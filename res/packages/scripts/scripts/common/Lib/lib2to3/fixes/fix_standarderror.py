# 2017.05.04 15:33:15 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_standarderror.py
"""Fixer for StandardError -> Exception."""
from .. import fixer_base
from ..fixer_util import Name

class FixStandarderror(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              'StandardError'\n              "

    def transform(self, node, results):
        return Name(u'Exception', prefix=node.prefix)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\fixes\fix_standarderror.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:15 Støední Evropa (letní èas)
