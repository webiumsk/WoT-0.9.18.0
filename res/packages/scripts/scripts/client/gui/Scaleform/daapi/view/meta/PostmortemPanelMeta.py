# 2017.05.04 15:24:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PostmortemPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PostmortemPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setDeadReasonInfoS(self, reason, showVehicle, vehicleLevel, vehicleImg, vehicleType, vehicleName):
        if self._isDAAPIInited():
            return self.flashObject.as_setDeadReasonInfo(reason, showVehicle, vehicleLevel, vehicleImg, vehicleType, vehicleName)

    def as_showDeadReasonS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showDeadReason()

    def as_setPlayerInfoS(self, playerInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerInfo(playerInfo)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\PostmortemPanelMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:33 Støední Evropa (letní èas)
