# 2017.05.04 15:33:16 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_zip.py
"""
Fixer that changes zip(seq0, seq1, ...) into list(zip(seq0, seq1, ...)
unless there exists a 'from future_builtins import zip' statement in the
top-level namespace.

We avoid the transformation if the zip() call is directly contained in
iter(<>), list(<>), tuple(<>), sorted(<>), ...join(<>), or for V in <>:.
"""
from .. import fixer_base
from ..fixer_util import Name, Call, in_special_context

class FixZip(fixer_base.ConditionalFix):
    BM_compatible = True
    PATTERN = "\n    power< 'zip' args=trailer< '(' [any] ')' >\n    >\n    "
    skip_on = 'future_builtins.zip'

    def transform(self, node, results):
        if self.should_skip(node):
            return None
        elif in_special_context(node):
            return None
        else:
            new = node.clone()
            new.prefix = u''
            new = Call(Name(u'list'), [new])
            new.prefix = node.prefix
            return new
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\fixes\fix_zip.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:16 Støední Evropa (letní èas)
