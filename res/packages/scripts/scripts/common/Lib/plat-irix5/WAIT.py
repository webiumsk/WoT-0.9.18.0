# 2017.05.04 15:33:50 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/plat-irix5/WAIT.py
from warnings import warnpy3k
warnpy3k('the WAIT module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
_WSTOPPED = 127
WNOHANG = 64
WEXITED = 1
WTRAPPED = 2
WSTOPPED = 4
WCONTINUED = 8
WNOWAIT = 128
WOPTMASK = WEXITED | WTRAPPED | WSTOPPED | WCONTINUED | WNOHANG | WNOWAIT
WSTOPFLG = 127
WCONTFLG = 65535
WCOREFLAG = 128
WSIGMASK = 127
WUNTRACED = 4
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\plat-irix5\WAIT.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:33:50 Støední Evropa (letní èas)
