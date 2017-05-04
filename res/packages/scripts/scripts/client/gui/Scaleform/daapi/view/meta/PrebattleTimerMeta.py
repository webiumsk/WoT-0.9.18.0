# 2017.05.04 15:24:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PrebattleTimerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PrebattleTimerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setTimerS(self, totalTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(totalTime)

    def as_setMessageS(self, msg):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessage(msg)

    def as_hideTimerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideTimer()

    def as_hideAllS(self, speed):
        if self._isDAAPIInited():
            return self.flashObject.as_hideAll(speed)

    def as_setWinConditionTextS(self, msg):
        if self._isDAAPIInited():
            return self.flashObject.as_setWinConditionText(msg)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\PrebattleTimerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:33 Støední Evropa (letní èas)
