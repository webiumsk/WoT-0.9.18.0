# 2017.05.04 15:26:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/wgnc/wgnc_helpers.py
from debug_utils import LOG_ERROR

def parseSize(sizeStr):
    if sizeStr:
        try:
            size = map(int, sizeStr.split('x'))
            if len(size) != 2:
                raise ValueError
        except ValueError:
            LOG_ERROR('Failed to parse size: %s' % sizeStr)
            size = None

    else:
        size = None
    return size
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\wgnc\wgnc_helpers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:35 Støední Evropa (letní èas)
