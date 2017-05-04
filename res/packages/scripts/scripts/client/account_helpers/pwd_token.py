# 2017.05.04 15:20:18 Støední Evropa (letní èas)
# Embedded file name: scripts/client/account_helpers/pwd_token.py
from constants import DEFAULT_LANGUAGE
import hashlib
__all__ = ['generate']

def _generateMd5Hash(pwd):
    md = hashlib.md5()
    md.update(pwd)
    return md.hexdigest()


_BY_LANG = {'cn': _generateMd5Hash,
 'vn': _generateMd5Hash}

def generate(pwd):
    return pwd


if DEFAULT_LANGUAGE in _BY_LANG:
    generate = _BY_LANG[DEFAULT_LANGUAGE]
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\account_helpers\pwd_token.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:18 Støední Evropa (letní èas)
