# 2017.05.04 15:33:15 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_repr.py
"""Fixer that transforms `xyzzy` into repr(xyzzy)."""
from .. import fixer_base
from ..fixer_util import Call, Name, parenthesize

class FixRepr(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              atom < '`' expr=any '`' >\n              "

    def transform(self, node, results):
        expr = results['expr'].clone()
        if expr.type == self.syms.testlist1:
            expr = parenthesize(expr)
        return Call(Name(u'repr'), [expr], prefix=node.prefix)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\fixes\fix_repr.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:15 St�edn� Evropa (letn� �as)
