# 2017.05.04 15:24:10 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_fitting_popover.py
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.view.lobby.shared import fitting_select_popover as fitting
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.shared.ItemsCache import g_itemsCache
from gui.shared.formatters import text_styles, icons
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA as _RC
_NOT_AFFECTED_TEXT = text_styles.alert(VEH_COMPARE.VEHCONF_DOESNTAFFECT)

class VehCmpConfigSelectPopover(fitting.CommonFittingSelectPopover):

    def __init__(self, ctx = None):
        data_ = ctx['data']
        slotType = data_.slotType
        slotIndex = data_.slotIndex
        cmpVeh = cmp_helpers.getCmpConfiguratorMainView().getCurrentVehicle()
        if self.__isEquipment(slotType):
            logicProvider = _CmpVehEquipmentLogicProvider(slotType, slotIndex, cmpVeh)
        elif self.__isOptioanlDevice(slotType):
            logicProvider = _CmpVehOptDevicesLogicProvider(slotType, slotIndex, cmpVeh)
        else:
            logicProvider = None
            LOG_ERROR('Unsupported slotType: {}'.format(slotType))
        super(VehCmpConfigSelectPopover, self).__init__(cmpVeh, logicProvider, ctx)
        return

    def _getCommonData(self):
        if self.__isEquipment(self._slotType):
            return (FITTING_TYPES.OPTIONAL_DEVICE_FITTING_ITEM_RENDERER,
             FITTING_TYPES.OPTIONAL_DEVICE_RENDERER_DATA_CLASS_NAME,
             FITTING_TYPES.LARGE_POPOVER_WIDTH,
             MENU.EQUIPMENTFITS_TITLE)
        else:
            return super(VehCmpConfigSelectPopover, self)._getCommonData()

    @staticmethod
    def __isEquipment(slotType):
        return slotType == cmp_helpers.EQUIPMENT_TYPE_NAME

    @staticmethod
    def __isOptioanlDevice(slotType):
        return slotType == cmp_helpers.OPTIONAL_DEVICE_TYPE_NAME


class _CmpVehArtefactLogicProvider(fitting.PopoverLogicProvider):

    def __init__(self, slotType, slotIndex, vehicle, notAffectedArtefacts):
        super(_CmpVehArtefactLogicProvider, self).__init__(slotType, slotIndex, vehicle)
        self._notAffectedArtefacts = notAffectedArtefacts

    def setModule(self, newId, oldId, isRemove):
        cmp_config_view = cmp_helpers.getCmpConfiguratorMainView()
        if isRemove:
            self._removeArtifact(cmp_config_view, self._slotIndex)
        else:
            self._installArtifact(cmp_config_view, newId, self._slotIndex)

    def _removeArtifact(self, cmp_config_view, slotIndex):
        pass

    def _installArtifact(self, cmp_config_view, newId, slotIndex):
        pass

    def _sortNotAffected(self, artefacts):

        def sortByAffectedVal(item):
            return item.name in self._notAffectedArtefacts

        return sorted(artefacts, key=sortByAffectedVal)

    def _isNotAffected(self, module):
        return module.name in self._notAffectedArtefacts

    def _buildModuleData(self, module, isInstalledInSlot, stats):
        isFit, reason = module.mayInstall(self._vehicle, self._slotIndex)
        moduleData = self._buildCommonModuleData(module, reason)
        fitting.extendByArtefactData(moduleData, module, self._slotIndex)
        isNotAffected = self._isNotAffected(module)
        isInstalled = module.isInstalled(self._vehicle)
        disabled = False
        if isInstalled:
            if not isInstalledInSlot:
                disabled = True
        else:
            disabled = not isFit
        moduleData['disabled'] = disabled
        moduleData['isSelected'] = isInstalledInSlot
        moduleData['targetVisible'] = isInstalled
        moduleData['removable'] = True
        moduleData['removeButtonLabel'] = VEH_COMPARE.VEHCONF_BTNCLEANUP
        moduleData['removeButtonTooltip'] = VEH_COMPARE.VEHCONF_TOOLTIPS_BTNCLEANUP
        moduleData['notAffectedTTC'] = isNotAffected
        if isNotAffected:
            moduleData['status'] = icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ALERTICON)
            moduleData['notAffectedTTCTooltip'] = makeTooltip(module.userName, attention=VEH_COMPARE.VEHCONF_TOOLTIPS_DEVICENOTAFFECTEDTTC)
        return moduleData


class _CmpVehOptDevicesLogicProvider(_CmpVehArtefactLogicProvider):

    def __init__(self, slotType, slotIndex, vehicle):
        super(_CmpVehOptDevicesLogicProvider, self).__init__(slotType, slotIndex, vehicle, cmp_helpers.NOT_AFFECTED_DEVICES)
        self._tooltipType = TOOLTIPS_CONSTANTS.COMPARE_MODULE

    def _getSuitableItems(self, typeId):
        return self._sortNotAffected(super(_CmpVehOptDevicesLogicProvider, self)._getSuitableItems(typeId))

    def _removeArtifact(self, cmp_config_view, slotIndex):
        cmp_config_view.removeOptionalDevice(slotIndex)

    def _installArtifact(self, cmp_config_view, newId, slotIndex):
        cmp_config_view.installOptionalDevice(newId, slotIndex)


class _CmpVehEquipmentLogicProvider(_CmpVehArtefactLogicProvider):

    def __init__(self, slotType, slotIndex, vehicle):
        super(_CmpVehEquipmentLogicProvider, self).__init__(slotType, slotIndex, vehicle, cmp_helpers.NOT_AFFECTED_EQUIPMENTS)
        self._tooltipType = TOOLTIPS_CONSTANTS.COMPARE_MODULE

    def _getSuitableItems(self, typeId):
        equipments = g_itemsCache.items.getItems(typeId, ~_RC.HIDDEN | _RC.VEHICLE.SUITABLE([self._vehicle], [typeId])).values()
        equipments.sort(reverse=True)
        return self._sortNotAffected(equipments)

    def _removeArtifact(self, cmp_config_view, slotIndex):
        cmp_config_view.removeEquipment(slotIndex)

    def _installArtifact(self, cmp_config_view, newId, slotIndex):
        cmp_config_view.installEquipment(newId, slotIndex)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\vehicle_compare\cmp_fitting_popover.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:10 St�edn� Evropa (letn� �as)
