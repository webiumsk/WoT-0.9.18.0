# 2017.05.04 15:24:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SiegeModeIndicatorMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SiegeModeIndicatorMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_switchSiegeStateS(self, totalTime, leftTime, siegeState, engineState, isSmooth):
        if self._isDAAPIInited():
            return self.flashObject.as_switchSiegeState(totalTime, leftTime, siegeState, engineState, isSmooth)

    def as_switchSiegeStateSnapshotS(self, totalTime, leftTime, siegeState, engineState, isSmooth):
        if self._isDAAPIInited():
            return self.flashObject.as_switchSiegeStateSnapshot(totalTime, leftTime, siegeState, engineState, isSmooth)

    def as_updateDeviceStateS(self, deviceName, deviceState):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDeviceState(deviceName, deviceState)

    def as_updateLayoutS(self, x, y):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLayout(x, y)

    def as_setVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(visible)

    def as_showHintS(self, buttonName, messageLeft, messageRight):
        if self._isDAAPIInited():
            return self.flashObject.as_showHint(buttonName, messageLeft, messageRight)

    def as_hideHintS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideHint()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\SiegeModeIndicatorMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:37 St�edn� Evropa (letn� �as)
