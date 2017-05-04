# 2017.05.04 15:30:24 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/sha.py
import warnings
warnings.warn('the sha module is deprecated; use the hashlib module instead', DeprecationWarning, 2)
from hashlib import sha1 as sha
new = sha
blocksize = 1
digest_size = 20
digestsize = 20
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\sha.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:30:24 Støední Evropa (letní èas)
