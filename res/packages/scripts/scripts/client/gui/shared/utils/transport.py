# 2017.05.04 15:26:25 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/utils/transport.py
import zlib
import cPickle
from debug_utils import LOG_ERROR

def z_dumps(obj, protocol = -1, level = 1):
    return zlib.compress(cPickle.dumps(obj, protocol), level)


def z_loads(value):
    try:
        result = zlib.decompress(value)
    except zlib.error:
        LOG_ERROR('Can not decompress value', value)
        return

    try:
        result = cPickle.loads(result)
    except cPickle.PickleError:
        LOG_ERROR('Can not unpickle value', value)
        result = None

    return result
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\utils\transport.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:25 Støední Evropa (letní èas)
