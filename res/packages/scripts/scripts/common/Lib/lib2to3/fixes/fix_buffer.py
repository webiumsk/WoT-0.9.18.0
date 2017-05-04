# 2017.05.04 15:33:10 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_buffer.py
"""Fixer that changes buffer(...) into memoryview(...)."""
from .. import fixer_base
from ..fixer_util import Name

class FixBuffer(fixer_base.BaseFix):
    BM_compatible = True
    explicit = True
    PATTERN = "\n              power< name='buffer' trailer< '(' [any] ')' > any* >\n              "

    def transform(self, node, results):
        name = results['name']
        name.replace(Name(u'memoryview', prefix=name.prefix))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\fixes\fix_buffer.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:11 Støední Evropa (letní èas)
