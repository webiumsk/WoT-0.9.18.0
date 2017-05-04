# 2017.05.04 15:33:15 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_reduce.py
"""Fixer for reduce().

Makes sure reduce() is imported from the functools module if reduce is
used in that module.
"""
from lib2to3 import fixer_base
from lib2to3.fixer_util import touch_import

class FixReduce(fixer_base.BaseFix):
    BM_compatible = True
    order = 'pre'
    PATTERN = "\n    power< 'reduce'\n        trailer< '('\n            arglist< (\n                (not(argument<any '=' any>) any ','\n                 not(argument<any '=' any>) any) |\n                (not(argument<any '=' any>) any ','\n                 not(argument<any '=' any>) any ','\n                 not(argument<any '=' any>) any)\n            ) >\n        ')' >\n    >\n    "

    def transform(self, node, results):
        touch_import(u'functools', u'reduce', node)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib2to3\fixes\fix_reduce.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:15 Støední Evropa (letní èas)
