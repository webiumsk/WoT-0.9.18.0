# 2017.05.04 15:33:14 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_paren.py
"""Fixer that addes parentheses where they are required

This converts ``[x for x in 1, 2]`` to ``[x for x in (1, 2)]``."""
from .. import fixer_base
from ..fixer_util import LParen, RParen

class FixParen(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n        atom< ('[' | '(')\n            (listmaker< any\n                comp_for<\n                    'for' NAME 'in'\n                    target=testlist_safe< any (',' any)+ [',']\n                     >\n                    [any]\n                >\n            >\n            |\n            testlist_gexp< any\n                comp_for<\n                    'for' NAME 'in'\n                    target=testlist_safe< any (',' any)+ [',']\n                     >\n                    [any]\n                >\n            >)\n        (']' | ')') >\n    "

    def transform(self, node, results):
        target = results['target']
        lparen = LParen()
        lparen.prefix = target.prefix
        target.prefix = u''
        target.insert_child(0, lparen)
        target.append_child(RParen())
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\fixes\fix_paren.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:14 St�edn� Evropa (letn� �as)
