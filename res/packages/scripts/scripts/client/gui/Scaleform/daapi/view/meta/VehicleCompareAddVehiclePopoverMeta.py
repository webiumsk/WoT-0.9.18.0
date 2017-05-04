# 2017.05.04 15:24:40 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleCompareAddVehiclePopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class VehicleCompareAddVehiclePopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def setVehicleSelected(self, dbID):
        self._printOverrideError('setVehicleSelected')

    def applyFilters(self, nation, vehicleType, level, isMain, hangarOnly):
        self._printOverrideError('applyFilters')

    def addButtonClicked(self):
        self._printOverrideError('addButtonClicked')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by VehicleCompareAddVehiclePopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_getTableDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getTableDP()

    def as_setAddButtonStateS(self, data):
        """
        :param data: Represented by ButtonPropertiesVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setAddButtonState(data)

    def as_updateTableSortFieldS(self, sortField, sortDirection):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTableSortField(sortField, sortDirection)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\VehicleCompareAddVehiclePopoverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:40 Støední Evropa (letní èas)
