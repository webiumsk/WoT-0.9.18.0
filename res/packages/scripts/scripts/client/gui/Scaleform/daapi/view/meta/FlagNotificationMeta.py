# 2017.05.04 15:24:25 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FlagNotificationMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FlagNotificationMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(state)

    def as_setActiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setActive(value)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FlagNotificationMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:25 Støední Evropa (letní èas)
