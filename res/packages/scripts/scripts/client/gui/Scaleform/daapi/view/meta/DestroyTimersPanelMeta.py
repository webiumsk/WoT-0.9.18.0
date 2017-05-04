# 2017.05.04 15:24:24 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DestroyTimersPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DestroyTimersPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_showS(self, timerTypeID, timerViewTypeID, isBubble):
        if self._isDAAPIInited():
            return self.flashObject.as_show(timerTypeID, timerViewTypeID, isBubble)

    def as_showStunS(self, totalSeconds, currentTime):
        if self._isDAAPIInited():
            return self.flashObject.as_showStun(totalSeconds, currentTime)

    def as_hideS(self, timerTypeID):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(timerTypeID)

    def as_hideStunS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideStun()

    def as_setTimeInSecondsS(self, timerTypeID, totalSeconds, currentTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeInSeconds(timerTypeID, totalSeconds, currentTime)

    def as_setTimeSnapshotS(self, timerTypeID, totalSeconds, timeLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeSnapshot(timerTypeID, totalSeconds, timeLeft)

    def as_setStunTimeSnapshotS(self, totalSeconds, timeLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_setStunTimeSnapshot(totalSeconds, timeLeft)

    def as_setSpeedS(self, speed):
        if self._isDAAPIInited():
            return self.flashObject.as_setSpeed(speed)

    def as_turnOnStackViewS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_turnOnStackView(value)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\DestroyTimersPanelMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:24 Støední Evropa (letní èas)
