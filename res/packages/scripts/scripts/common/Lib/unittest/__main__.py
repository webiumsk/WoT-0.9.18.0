# 2017.05.04 15:34:36 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/unittest/__main__.py
"""Main entry point"""
import sys
if sys.argv[0].endswith('__main__.py'):
    sys.argv[0] = 'python -m unittest'
__unittest = True
from .main import main, TestProgram, USAGE_AS_MAIN
TestProgram.USAGE = USAGE_AS_MAIN
main(module=None)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\unittest\__main__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:34:36 Støední Evropa (letní èas)
