# 2017.05.04 15:24:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleInfoMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleInfoMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def getVehicleInfo(self):
        self._printOverrideError('getVehicleInfo')

    def onCancelClick(self):
        self._printOverrideError('onCancelClick')

    def addToCompare(self):
        self._printOverrideError('addToCompare')

    def as_setVehicleInfoS(self, data):
        """
        :param data: Represented by VehicleInfoDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleInfo(data)

    def as_setCompareButtonDataS(self, data):
        """
        :param data: Represented by VehCompareButtonDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCompareButtonData(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\VehicleInfoMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:41 Støední Evropa (letní èas)
