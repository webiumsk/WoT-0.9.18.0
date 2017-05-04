# 2017.05.04 15:28:09 Støední Evropa (letní èas)
# Embedded file name: scripts/client/VOIP/__init__.py
import BigWorld

def getVOIPManager():
    if not globals().has_key('__handler'):
        from VOIPManager import VOIPManager
        globals()['__handler'] = VOIPManager()
        BigWorld.VOIP.setHandler(__handler)
    return __handler
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\VOIP\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:09 Støední Evropa (letní èas)
