# 2017.05.04 15:24:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RepairPointTimerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RepairPointTimerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(state)

    def as_setTimeInSecondsS(self, seconds):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeInSeconds(seconds)

    def as_setTimeStringS(self, timeStr):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeString(timeStr)

    def as_useActionScriptTimerS(self, isASTimer):
        if self._isDAAPIInited():
            return self.flashObject.as_useActionScriptTimer(isASTimer)

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\RepairPointTimerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:36 Støední Evropa (letní èas)
