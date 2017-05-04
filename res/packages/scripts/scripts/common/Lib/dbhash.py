# 2017.05.04 15:29:34 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/dbhash.py
"""Provide a (g)dbm-compatible interface to bsddb.hashopen."""
import sys
import warnings
warnings.warnpy3k('in 3.x, the dbhash module has been removed', stacklevel=2)
try:
    import bsddb
except ImportError:
    del sys.modules[__name__]
    raise

__all__ = ['error', 'open']
error = bsddb.error

def open(file, flag = 'r', mode = 438):
    return bsddb.hashopen(file, flag, mode)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\dbhash.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:29:34 Støední Evropa (letní èas)
