# 2017.05.04 15:34:27 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/plat-riscos/riscosenviron.py
"""A more or less complete dictionary like interface for the RISC OS environment."""
import riscos

class _Environ:

    def __init__(self, initial = None):
        pass

    def __repr__(self):
        return repr(riscos.getenvdict())

    def __cmp__(self, dict):
        return cmp(riscos.getenvdict(), dict)

    def __len__(self):
        return len(riscos.getenvdict())

    def __getitem__(self, key):
        ret = riscos.getenv(key)
        if ret != None:
            return ret
        else:
            raise KeyError
            return

    def __setitem__(self, key, item):
        riscos.putenv(key, item)

    def __delitem__(self, key):
        riscos.delenv(key)

    def clear(self):
        pass

    def copy(self):
        return riscos.getenvdict()

    def keys(self):
        return riscos.getenvdict().keys()

    def items(self):
        return riscos.getenvdict().items()

    def values(self):
        return riscos.getenvdict().values()

    def has_key(self, key):
        value = riscos.getenv(key)
        return value != None

    def __contains__(self, key):
        return riscos.getenv(key) is not None

    def update(self, dict):
        for k, v in dict.items():
            riscos.putenv(k, v)

    def get(self, key, failobj = None):
        value = riscos.getenv(key)
        if value != None:
            return value
        else:
            return failobj
            return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\plat-riscos\riscosenviron.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:34:27 St�edn� Evropa (letn� �as)
