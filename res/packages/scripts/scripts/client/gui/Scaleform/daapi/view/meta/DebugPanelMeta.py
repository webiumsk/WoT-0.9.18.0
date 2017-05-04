# 2017.05.04 15:24:23 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DebugPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DebugPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_updatePingInfoS(self, pingValue):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePingInfo(pingValue)

    def as_updateFPSInfoS(self, fpsValue):
        if self._isDAAPIInited():
            return self.flashObject.as_updateFPSInfo(fpsValue)

    def as_updateLagInfoS(self, isLagging):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLagInfo(isLagging)

    def as_updatePingFPSInfoS(self, pingValue, fpsValue):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePingFPSInfo(pingValue, fpsValue)

    def as_updatePingFPSLagInfoS(self, pingValue, fpsValue, isLagging):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePingFPSLagInfo(pingValue, fpsValue, isLagging)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\DebugPanelMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:23 Støední Evropa (letní èas)
