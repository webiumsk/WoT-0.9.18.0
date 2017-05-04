# 2017.05.04 15:24:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleSelectorPopupMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleSelectorPopupMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onFiltersUpdate(self, nation, vehicleType, isMain, level, compatibleOnly):
        self._printOverrideError('onFiltersUpdate')

    def onSelectVehicles(self, items):
        self._printOverrideError('onSelectVehicles')

    def as_setFiltersDataS(self, data):
        """
        :param data: Represented by VehicleSelectorFilterVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFiltersData(data)

    def as_setListDataS(self, listData, selectedItems):
        """
        :param listData: Represented by DataProvider (AS)
        :param selectedItems: Represented by Array (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setListData(listData, selectedItems)

    def as_setListModeS(self, isMultipleSelect):
        if self._isDAAPIInited():
            return self.flashObject.as_setListMode(isMultipleSelect)

    def as_setInfoTextS(self, text, componentsOffset):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfoText(text, componentsOffset)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\VehicleSelectorPopupMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:41 Støední Evropa (letní èas)
