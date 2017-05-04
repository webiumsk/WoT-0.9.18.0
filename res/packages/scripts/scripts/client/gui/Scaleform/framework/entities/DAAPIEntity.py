# 2017.05.04 15:24:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/DAAPIEntity.py
from debug_utils import LOG_DEBUG
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
__author__ = 'd_dichkovsky'

class DAAPIEntity(EventSystemEntity):

    def __init__(self):
        super(DAAPIEntity, self).__init__()
        self.__flashObject = None
        self.__isDAAPIInited = False
        return

    @property
    def flashObject(self):
        return self.__flashObject

    def turnDAAPIon(self, setScript, movieClip):
        if not self.__isDAAPIInited:
            self.__flashObject = movieClip
            if setScript:
                self.__flashObject.script = self
                self.__isDAAPIInited = True

    def turnDAAPIoff(self, isScriptSet):
        if isScriptSet:
            self.__flashObject.script = None
            self.__isDAAPIInited = False
        self.__flashObject = None
        return

    def _isDAAPIInited(self):
        return self.__isDAAPIInited
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\DAAPIEntity.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:45 St�edn� Evropa (letn� �as)
