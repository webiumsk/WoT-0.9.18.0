# 2017.05.04 15:24:41 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleCompareViewMeta.py
from gui.Scaleform.daapi.view.meta.VehicleCompareCommonViewMeta import VehicleCompareCommonViewMeta

class VehicleCompareViewMeta(VehicleCompareCommonViewMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends VehicleCompareCommonViewMeta
    """

    def onBackClick(self):
        self._printOverrideError('onBackClick')

    def onGoToPreviewClick(self, vehicleID):
        self._printOverrideError('onGoToPreviewClick')

    def onGoToHangarClick(self, vehicleID):
        self._printOverrideError('onGoToHangarClick')

    def onSelectModulesClick(self, vehicleID, index):
        self._printOverrideError('onSelectModulesClick')

    def onParamDeltaRequested(self, index, paramID):
        self._printOverrideError('onParamDeltaRequested')

    def onCrewLevelChanged(self, index, crewLevelID):
        self._printOverrideError('onCrewLevelChanged')

    def onRemoveVehicle(self, index):
        self._printOverrideError('onRemoveVehicle')

    def onRevertVehicle(self, index):
        self._printOverrideError('onRevertVehicle')

    def onRemoveAllVehicles(self):
        self._printOverrideError('onRemoveAllVehicles')

    def as_setStaticDataS(self, data):
        """
        :param data: Represented by VehCompareStaticDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setParamsDeltaS(self, data):
        """
        :param data: Represented by VehCompareParamsDeltaVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setParamsDelta(data)

    def as_setVehicleParamsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleParamsData(data)

    def as_getVehiclesDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getVehiclesDP()

    def as_setVehiclesCountTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesCountText(text)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\VehicleCompareViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:41 St�edn� Evropa (letn� �as)
