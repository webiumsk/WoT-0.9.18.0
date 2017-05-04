# 2017.05.04 15:33:12 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_input.py
"""Fixer that changes input(...) into eval(input(...))."""
from .. import fixer_base
from ..fixer_util import Call, Name
from .. import patcomp
context = patcomp.compile_pattern("power< 'eval' trailer< '(' any ')' > >")

class FixInput(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              power< 'input' args=trailer< '(' [any] ')' > >\n              "

    def transform(self, node, results):
        if context.match(node.parent.parent):
            return
        new = node.clone()
        new.prefix = u''
        return Call(Name(u'eval'), [new], prefix=node.prefix)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\fixes\fix_input.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:12 Støední Evropa (letní èas)
