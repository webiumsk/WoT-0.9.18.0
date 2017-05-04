# 2017.05.04 15:24:09 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_configurator_view.py
from collections import defaultdict
from adisp import process
from debug_utils import LOG_WARNING, LOG_DEBUG, LOG_ERROR
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hangar.AmmunitionPanel import getFittingSlotsData, getAmmo, FITTING_SLOTS, ARTEFACTS_SLOTS, OPTIONAL_DEVICE_SLOTS_COUNT, FITTING_MODULES
from gui.Scaleform.daapi.view.lobby.shared.fitting_slot_vo import FittingSlotVO
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_base import VehicleCompareConfiguratorBaseView
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_parameters import VehicleCompareParameters
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_helpers import getSuitableCamouflage
from gui.Scaleform.daapi.view.meta.VehicleCompareConfiguratorMainMeta import VehicleCompareConfiguratorMainMeta
from gui.Scaleform.daapi.view.meta.VehicleCompareConfiguratorViewMeta import VehicleCompareConfiguratorViewMeta
from gui.Scaleform.framework import g_entitiesFactories
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.genConsts.VEHICLE_COMPARE_CONSTANTS import VEHICLE_COMPARE_CONSTANTS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.game_control.veh_comparison_basket import CREW_TYPES, PARAMS_AFFECTED_TANKMEN_SKILLS
from gui.shared.ItemsCache import g_itemsCache
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles
from gui.shared.gui_items import Tankman, GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.gui_items.items_actions.actions import processMsg
from gui.shared.gui_items.processors import module as installer_module
from gui.shared.gui_items.processors.module import ModuleProcessor
from gui.shared.utils.functions import makeTooltip
from helpers import dependency
from helpers.i18n import makeString as _ms
from items import tankmen
from shared_utils import findFirst
from skeletons.gui.game_control import IVehicleComparisonBasket

@process
def _installModulesSet(vehicle, modules, notFitted):
    UNDEFINED_INDEX = -1

    def __findModuleIndex(mList, moduleTypeID):
        for i in xrange(len(mList)):
            if mList[i].itemTypeID == moduleTypeID:
                return i
        else:
            return UNDEFINED_INDEX

    def __updateVehicleModule(vehicle, module):
        typeID = module.itemTypeID
        if typeID == GUI_ITEM_TYPE.CHASSIS:
            vehicle.chassis = module
        elif typeID == GUI_ITEM_TYPE.ENGINE:
            vehicle.engine = module
        elif typeID == GUI_ITEM_TYPE.RADIO:
            vehicle.radio = module
        elif typeID == GUI_ITEM_TYPE.TURRET:
            vehicle.turret = module
        elif typeID == GUI_ITEM_TYPE.GUN:
            vehicle.gun = module

    if modules:
        while modules:
            module = modules.pop()
            isFit, notFitReason = module.mayInstall(vehicle)
            if isFit:
                yield installer_module.getPreviewInstallerProcessor(vehicle, module).request()
                __updateVehicleModule(vehicle, module)
            elif notFitReason == 'need turret':
                turretIndex = __findModuleIndex(modules, GUI_ITEM_TYPE.TURRET)
                if turretIndex != UNDEFINED_INDEX:
                    modules.append(module)
                    modules.append(modules.pop(turretIndex))
                    _installModulesSet(vehicle, modules, notFitted)
                    break
                else:
                    notFitted.append(notFitReason)
            elif notFitReason == 'need gun':
                gunIndex = __findModuleIndex(modules, GUI_ITEM_TYPE.GUN)
                if gunIndex != UNDEFINED_INDEX:
                    modules.append(module)
                    modules.append(modules.pop(gunIndex))
                    _installModulesSet(vehicle, modules, notFitted)
                    break
                else:
                    notFitted.append(notFitReason)
            elif notFitReason == 'too heavy':
                chassisIndex = __findModuleIndex(modules, GUI_ITEM_TYPE.CHASSIS)
                if chassisIndex != UNDEFINED_INDEX:
                    modules.append(module)
                    modules.append(modules.pop(chassisIndex))
                    _installModulesSet(vehicle, modules, notFitted)
                    break
                else:
                    notFitted.append(notFitReason)
            elif notFitReason == 'too heavy chassis':
                modules.insert(0, module)
                _installModulesSet(vehicle, modules, notFitted)
                break


def _getSlotDataIndexes(slots):
    """
    Provides list of tuples that contains indexes for slots data
    :param slots: the range of slots gui.shared.gui_items.GUI_ITEM_TYPE_NAMES
    :return: list , [(1,), (2,) ... [8,9,10]]
    """
    index = 0
    indexes = []
    for slot in slots:
        if slot in ARTEFACTS_SLOTS:
            indexes.append(range(index, index + OPTIONAL_DEVICE_SLOTS_COUNT))
            index += OPTIONAL_DEVICE_SLOTS_COUNT
        else:
            indexes.append((index,))
            index += 1

    return indexes


_SLOT_DATA_INDEXES = _getSlotDataIndexes(FITTING_SLOTS)

class _CmpOptDeviceRemover(ModuleProcessor):

    def __init__(self, vehicle, item, slotIndex, plugs = tuple()):
        super(_CmpOptDeviceRemover, self).__init__(item, 'remove', plugs)
        self.__vehicle = vehicle
        self.__slotIndex = slotIndex

    def _request(self, callback):
        mayRemove, reason = self.__vehicle.descriptor.mayRemoveOptionalDevice(self.__slotIndex)
        if mayRemove:
            self.__vehicle.descriptor.removeOptionalDevice(self.__slotIndex)
            self.__vehicle.optDevices[self.__slotIndex] = None
            super(_CmpOptDeviceRemover, self)._request(callback)
        else:
            callback(self._errorHandler(0, reason))
        return

    def _errorHandler(self, code, errStr = '', ctx = None):
        if errStr == 'too heavy':
            errStr = 'error_too_heavy'
        return super(_CmpOptDeviceRemover, self)._errorHandler(code, errStr, ctx)

    def _getMsgCtx(self):
        return {'name': self.item.userName,
         'kind': self.item.userType,
         'money': 0}


class _ConfigFittingSlotVO(FittingSlotVO):

    def __init__(self, modulesData, vehicle, slotType, slotId = None, tooltipType = None):
        super(_ConfigFittingSlotVO, self).__init__(modulesData, vehicle, slotType, slotId, tooltipType)
        slotEmpty = self['id'] == -1
        self['showRemoveBtn'] = not slotEmpty
        if slotEmpty:
            self['tooltipType'] = TOOLTIPS_CONSTANTS.COMPLEX
            self['tooltip'] = VEH_COMPARE.VEHCONF_TOOLTIPS_EMPTYEQSLOT if slotType == 'equipment' else VEH_COMPARE.VEHCONF_TOOLTIPS_EMPTYOPTDEVICESLOT
        elif slotType == FITTING_TYPES.VEHICLE_TURRET and not vehicle.hasTurrets:
            self['tooltipType'] = ''
        else:
            self['tooltipType'] = TOOLTIPS_CONSTANTS.COMPARE_MODULE


class _DefaultSkillCompletenessChecker(object):

    def isCompleted(self, levels, crew):
        """
        Checks if all members of crew have 100% skill level
        :param levels: skill levels array
        :param crew: vehicle crew
        :return:
        """
        for lvl in levels:
            if lvl < tankmen.MAX_SKILL_LEVEL:
                return False

        return True


class _FullCrewSkillsCompletenessChecker(_DefaultSkillCompletenessChecker):

    def isCompleted(self, levels, crew):
        isAllSkillsAre100 = super(_FullCrewSkillsCompletenessChecker, self).isCompleted(levels, crew)
        if isAllSkillsAre100:
            return len(levels) == len(crew)
        else:
            return False


class _CurrentCrewMonitor(object):
    _DEF_SKILL_CHECKER = _DefaultSkillCompletenessChecker()
    _FULL_CREW_SKILL_CHECKER = _FullCrewSkillsCompletenessChecker()

    def __init__(self, container):
        super(_CurrentCrewMonitor, self).__init__()
        self.__container = container
        self.__increasedTo100Skills = set()
        skillsCheckerStorage = defaultdict(lambda : self._DEF_SKILL_CHECKER)
        skillsCheckerStorage[PARAMS_AFFECTED_TANKMEN_SKILLS[0]] = self._FULL_CREW_SKILL_CHECKER
        skillsCheckerStorage[PARAMS_AFFECTED_TANKMEN_SKILLS[1]] = self._FULL_CREW_SKILL_CHECKER
        vehicleCrew = g_itemsCache.items.getItemByCD(self.__container.getCurrentVehicle().intCD).crew
        levelsBySkills = defaultdict(list)
        for roleIndex, tankman in vehicleCrew:
            if tankman is not None:
                for skill in tankman.skills:
                    if skill.name in PARAMS_AFFECTED_TANKMEN_SKILLS:
                        levelsBySkills[skill.name].append(skill.level)

        for skillName, levels in levelsBySkills.iteritems():
            if not skillsCheckerStorage[skillName].isCompleted(levels, vehicleCrew):
                self.__increasedTo100Skills.add(skillName)

        return

    def isIncreasedSkillsSelected(self):
        """
        Checks is some of selected skill has been increased to 100% for comparison functionality
        :return: True if some of selected skills has been increased to 100%
        """
        if self.__container.getCurrentCrewSkillLevel() != CREW_TYPES.CURRENT:
            return False
        if self.__container.getCurrentCrewSkills().intersection(self.__increasedTo100Skills):
            return True
        return False

    def dispose(self):
        self.__container = None
        return


class _CrewSkillsManager(object):

    def __init__(self, vehicle, crewSkillLevel, selectedSkills):
        super(_CrewSkillsManager, self).__init__()
        self.__vehicle = vehicle
        self.__crewSkillLevel = None
        self.__selectedSkills = selectedSkills
        crewSkills = cmp_helpers.getVehicleCrewSkills(self.__vehicle)
        self.__rolesBySkills = defaultdict(set)
        self.__skillsByRoles = {}
        for idx, (role, skillsSet) in enumerate(crewSkills):
            for skill in skillsSet:
                self.__rolesBySkills[skill].add((idx, role))
                self.__skillsByRoles[role] = skillsSet

        self.changeCrewSkillLevel(crewSkillLevel)
        return

    def toggleSkill(self, skillName):
        """
        Apply or decline skill for particular crew members
        :param skillName: the name (id) of skill (must be from cmp_helpers.PARAMS_AFFECTED_TANKMEN_SKILLS)
        :return: bool, True if skill have been successfully applied / declined, otherwise False
        """
        if skillName not in PARAMS_AFFECTED_TANKMEN_SKILLS:
            LOG_WARNING('Attempt to set skill not affected on the vehicle parameters: {}'.format(skillName))
            return False
        if self.__crewSkillLevel != CREW_TYPES.SKILL_100 and self.__crewSkillLevel != CREW_TYPES.CURRENT:
            LOG_WARNING('It is forbidden to set skill for {}% level crew!'.format(self.__crewSkillLevel))
            return False
        if skillName not in self.__selectedSkills:
            self.__selectedSkills.add(skillName)
        else:
            self.__selectedSkills.remove(skillName)
        return self._applyTankmanSkill(self.__vehicle, self.__getAffectedTankmens((skillName,)), self.__skillsByRoles, self.__selectedSkills)

    def applySkillForTheSameVehicle(self, vehicle, skillName):
        """
        Applies current skills configuration on the same vehicle
        :param vehicle: target vehicle
        :param skillName: str - skill name from PARAMS_AFFECTED_TANKMEN_SKILLS
        :return:
        """
        if vehicle.intCD != self.__vehicle.intCD:
            LOG_DEBUG('Target vehicle is not the same as current vehicle! Expected {}, received {}'.format(self.__vehicle.intCD, vehicle.intCD))
            return False
        if skillName not in PARAMS_AFFECTED_TANKMEN_SKILLS:
            LOG_WARNING('Attempt to set skill not affected on the vehicle parameters: {}'.format(skillName))
            return False
        selectedSkills = self.__selectedSkills.copy()
        selectedSkills.add(skillName)
        return self._applyTankmanSkill(vehicle, self.__getAffectedTankmens((skillName,)), self.__skillsByRoles, selectedSkills)

    def changeCrewSkillLevel(self, newSkillsLevel):
        success = False
        if self.__crewSkillLevel != newSkillsLevel:
            self.__crewSkillLevel = newSkillsLevel
            skillsByRoles = {}
            if self.__crewSkillLevel == CREW_TYPES.SKILL_100 or self.__crewSkillLevel == CREW_TYPES.CURRENT:
                affectedTankmens = self.__getAffectedTankmens(self.__selectedSkills)
                for idx, role in affectedTankmens:
                    skillsByRoles[idx] = self.__skillsByRoles[role].intersection(self.__selectedSkills)

            if self.__crewSkillLevel == CREW_TYPES.CURRENT:
                levelsByIndexes, nativeVehiclesByIndexes = cmp_helpers.getVehCrewInfo(self.__vehicle.intCD)
                defRoleLevel = None
            else:
                nativeVehiclesByIndexes = None
                levelsByIndexes = None
                defRoleLevel = self.__crewSkillLevel
            self.__vehicle.crew = self.__vehicle.getCrewBySkillLevels(defRoleLevel, skillsByRoles, levelsByIndexes, nativeVehiclesByIndexes)
            success = True
        return success

    def getSelectedSkills(self):
        return self.__selectedSkills.copy()

    def getCrewSkillLevel(self):
        return self.__crewSkillLevel

    def dispose(self):
        self.__vehicle = None
        return

    @classmethod
    def _applyTankmanSkill(cls, vehicle, affectedTankmens, skillsByRoles, selectedSkills):
        """
        Creates tankmens with particular roles and set of skills and applies it on the Vehicle
        :param vehicle: target Vehicle
        :param affectedTankmens: The set of tankmens roles that have to be recreated
        :param skillsByRoles: dict, the set of skills available for particular tankmen role
        :param selectedSkills: currently selected set of skills
        :return: bool, True if some of tankmens has been recreated
        """
        nationID, vehicleTypeID = vehicle.descriptor.type.id
        success = False
        for roleIdx, role in affectedTankmens:
            skills = skillsByRoles[role]
            veh_crew = vehicle.crew
            for idx, (vehCrewRoleIdx, _) in enumerate(veh_crew):
                if vehCrewRoleIdx == roleIdx:
                    veh_crew[idx] = (roleIdx, cmp_helpers.createTankman(nationID, vehicleTypeID, role, tankmen.MAX_SKILL_LEVEL, skills.intersection(selectedSkills)))
                    success = True
                    break
            else:
                LOG_WARNING('Tankmen with role index {} has not been found'.format(roleIdx))

        return success

    def __getAffectedTankmens(self, skills):
        """
        Provides the set of tankmens roles which supported skills
        :param skills: the set of skills
        :return: set of tankmens roles
        """
        tankmens = set()
        for skill in skills:
            tankmens |= self.__rolesBySkills[skill]

        return tankmens


class VehicleCompareConfiguratorView(LobbySubView, VehicleCompareConfiguratorViewMeta):

    def __init__(self, ctx = None):
        self.__parametersView = None
        super(VehicleCompareConfiguratorView, self).__init__(ctx)
        self.__slotsVoData = [None] * (_SLOT_DATA_INDEXES[-1][-1] + 1)
        self.__currentCrewMonitor = None
        return

    def onCloseView(self):
        self._container.closeView()

    def onCamouflageUpdated(self):
        self.as_setCamoS(self._container.isCamouflageSet())
        self.__updateParametersView()

    def onOptDeviceUpdated(self):
        self.__updateOptDevicesData()

    def onEquipmentUpdated(self):
        self.__updateEquipmentData()

    def onModulesUpdated(self):
        self.__updateSlotsData(FITTING_MODULES)
        self.__updateParametersView()
        self.as_setTopModulesSelectedS(self._container.isTopModulesSelected())

    def onCrewSkillUpdated(self):
        self.__updateParametersView()
        self.__updateCrewAttentionIcon()

    def onCrewLevelUpdated(self, newLvl):
        self.__updateParametersView()
        self.__updateCrewSelectionAvailability(newLvl)
        self.__updateCrewAttentionIcon()

    def onResetToDefault(self):
        self.__updateSkillsData()
        self.__parametersView.init(self._container.getCurrentVehicle())
        self.__updateSlotsData(FITTING_SLOTS)
        self.as_setTopModulesSelectedS(self._container.isTopModulesSelected())
        self.__updateCrewLvl()
        self.__updateCrewAttentionIcon()

    def onShellsUpdated(self, updateShells = False, selectedIndex = -1):
        if selectedIndex != -1:
            self.as_setSelectedAmmoIndexS(selectedIndex)
            self.__updateParametersView()
        if updateShells:
            self.__updateShellSlots()
            self.__updateControlBtns()

    def resetConfig(self):
        self._container.resetToDefault()

    def applyConfig(self):
        self._container.applyNewParameters()
        self.onCloseView()

    def selectShell(self, shellId, slotIndex):
        self._container.selectShell(slotIndex)

    def camoSelected(self, selected):
        self._container.selectCamouflage(selected)

    def installDevice(self, newId, slotType, slotIndex):
        if slotType == cmp_helpers.OPTIONAL_DEVICE_TYPE_NAME:
            self._container.installOptionalDevice(newId, slotIndex)
        elif slotType == cmp_helpers.EQUIPMENT_TYPE_NAME:
            self._container.installEquipment(newId, slotIndex)
        else:
            LOG_ERROR('{} installDevice. Unsupported slotType: {}'.format(self, slotType))

    def removeDevice(self, slotType, slotIndex):
        """
        Remove type from provided index slot
        :param slotType: type of module from GUI_ITEM_TYPE_NAMES.*
        :param slotIndex: there are 3 available indexes: (0,1,2)
        """
        if slotType == cmp_helpers.OPTIONAL_DEVICE_TYPE_NAME:
            self._container.removeOptionalDevice(slotIndex)
        elif slotType == cmp_helpers.EQUIPMENT_TYPE_NAME:
            self._container.removeEquipment(slotIndex)
        else:
            LOG_ERROR('{} removeDevice. Unsupported slotType: {}'.format(self, slotType))

    def toggleTopModules(self, value):
        self._container.selectTopModules(value)

    def showModules(self):
        self._container.as_showViewS(VEHICLE_COMPARE_CONSTANTS.VEHICLE_MODULES_VIEW)

    def skillSelect(self, skillType, slotIndex, selected):
        self._container.selectCrewSkill(skillType, selected)

    def changeCrewLevel(self, crewLevelId):
        self._container.selectCrewLevel(crewLevelId)

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(VehicleCompareConfiguratorView, self)._onRegisterFlashComponent(viewPy, alias)
        if isinstance(viewPy, VehicleCompareParameters):
            self.__parametersView = viewPy

    def _init(self):
        super(VehicleCompareConfiguratorView, self)._init()
        currentVehicle = self._container.getCurrentVehicle()
        enableCamo = bool(getSuitableCamouflage(currentVehicle)[0])
        topModulesFromStock = self._container.isTopModulesFromStock()
        enableTopModules = not (currentVehicle.isPremium or topModulesFromStock)
        isInInventory = self._container.getBasketVehCmpData().isInInventory()
        if isInInventory:
            self.__currentCrewMonitor = _CurrentCrewMonitor(self._container)
        self.as_setInitDataS({'title': text_styles.promoSubTitle(_ms(VEH_COMPARE.VEHCONF_HEADER, vehName=currentVehicle.userName)),
         'resetBtnLabel': VEH_COMPARE.VEHCONF_RESETBTNLABEL,
         'cancelBtnLabel': VEH_COMPARE.VEHCONF_CANCELBTNLABEL,
         'applyBtnLabel': VEH_COMPARE.VEHCONF_APPLYBTNLABEL,
         'resetBtnTooltip': VEH_COMPARE.VEHCONF_RESETBTNLABEL_TOOLTIP,
         'cancelBtnTooltip': VEH_COMPARE.VEHCONF_CANCELBTNLABEL_TOOLTIP,
         'applyBtnTooltip': VEH_COMPARE.VEHCONF_COMPAREBTNLABEL_TOOLTIP,
         'crewLevels': self.__getCrewLevels(isInInventory),
         'enableTopModules': enableTopModules,
         'enableCamo': enableCamo})
        self.__updateCrewLvl()
        self.__updateShellSlots()
        self.as_setSelectedAmmoIndexS(self._container.getCurrentShellIndex())
        self.as_setCamoS(self._container.isCamouflageSet())
        self.__updateControlBtns()
        topModulesSelected = topModulesFromStock or self._container.isTopModulesSelected()
        self.as_setTopModulesSelectedS(topModulesSelected)
        self.__updateCrewAttentionIcon()
        self.__updateSkillsData()
        self.__updateSlotsData(FITTING_SLOTS)
        initialVehicle, _ = self._container.getInitialVehicleData()
        self.__parametersView.init(currentVehicle, initialVehicle)

    def _dispose(self):
        if self.__currentCrewMonitor:
            self.__currentCrewMonitor.dispose()
        self.__parametersView = None
        super(VehicleCompareConfiguratorView, self)._dispose()
        return

    def __updateOptDevicesData(self):
        self.__updateSlotsData((cmp_helpers.OPTIONAL_DEVICE_TYPE_NAME,))

    def __updateEquipmentData(self):
        self.__updateSlotsData((cmp_helpers.EQUIPMENT_TYPE_NAME,))

    def __updateSlotsData(self, slotsTypes):
        """
        Creates VO data only for provided slot types
        :param slotsTypes: *.GUI_ITEM_TYPE_NAMES
        """
        newVoData = getFittingSlotsData(self._container.getCurrentVehicle(), slotsTypes, _ConfigFittingSlotVO)
        for slotType in slotsTypes:
            indexesRange = _SLOT_DATA_INDEXES[FITTING_SLOTS.index(slotType)]
            for idx in indexesRange:
                newSlotData = newVoData.pop(0)
                slotDataID = newSlotData.get('id', 0)
                if slotDataID > 0:
                    moduleItem = g_itemsCache.items.getItemByCD(slotDataID)
                    itemTypeID = moduleItem.itemTypeID
                    itemName = moduleItem.name
                    if itemTypeID == GUI_ITEM_TYPE.EQUIPMENT:
                        if itemName in cmp_helpers.NOT_AFFECTED_EQUIPMENTS:
                            newSlotData['affectsAtTTC'] = False
                            newSlotData['tooltipType'] = 'complex'
                            newSlotData['tooltip'] = makeTooltip(moduleItem.userName, attention=VEH_COMPARE.VEHCONF_TOOLTIPS_DEVICENOTAFFECTEDTTC)
                self.__slotsVoData[idx] = newSlotData

        self.as_setDevicesDataS(self.__slotsVoData)
        self.__updateParametersView()

    def __updateParametersView(self):
        if self.__parametersView is not None:
            self.__parametersView.update()
            self.__updateControlBtns()
        return

    def __updateCrewSelectionAvailability(self, newLvl):
        self.as_setSkillsBlockedS(newLvl != CREW_TYPES.SKILL_100 and newLvl != CREW_TYPES.CURRENT)

    def __updateControlBtns(self):
        self.as_setResetEnabledS(self._container.isDifferentWithInitialBasketVeh())
        self.as_setApplyEnabledS(self._container.isCurrentVehicleModified())

    def __updateSkillsData(self):
        skills = map(lambda skillType: {'icon': Tankman.getSkillBigIconPath(skillType),
         'label': Tankman.getSkillUserName(skillType),
         'skillType': skillType,
         'isForAll': skillType in tankmen.COMMON_SKILLS,
         'selected': skillType in self._container.getCurrentCrewSkills()}, PARAMS_AFFECTED_TANKMEN_SKILLS)
        self.as_setSkillsS(skills)

    @staticmethod
    def __getCrewLevels(isInHangar):
        items = [{'label': VEH_COMPARE.VEHICLECOMPAREVIEW_CREW_SKILL100,
          'id': CREW_TYPES.SKILL_100,
          'showAlert': False,
          'tooltip': None}, {'label': VEH_COMPARE.VEHICLECOMPAREVIEW_CREW_SKILL75,
          'id': CREW_TYPES.SKILL_75}, {'label': VEH_COMPARE.VEHICLECOMPAREVIEW_CREW_SKILL50,
          'id': CREW_TYPES.SKILL_50}]
        if isInHangar:
            items.append({'label': VEH_COMPARE.VEHICLECOMPAREVIEW_CREW_CURRENT,
             'id': CREW_TYPES.CURRENT})
        return items

    def __updateCrewLvl(self):
        crewLevel = self._container.getCurrentCrewSkillLevel()
        self.as_setCrewLevelIndexS(CREW_TYPES.ALL.index(crewLevel))
        self.__updateCrewSelectionAvailability(crewLevel)

    def __updateShellSlots(self):
        shells = map(lambda shot: g_itemsCache.items.getItemByCD(shot['shell']['compactDescr']), self._container.getCurrentVehicle().descriptor.gun['shots'])
        self.as_setAmmoS(getAmmo(shells))

    def __updateCrewAttentionIcon(self):
        """
        Show alert icon if current interface has selected tankmen skills
        which has been increased to 100% specially for vehicle comparison basket functionality
        """
        isVisible = False
        if self.__currentCrewMonitor:
            isVisible = self.__currentCrewMonitor.isIncreasedSkillsSelected()
        self.as_setCrewAttentionIconVisibleS(isVisible)


class VehicleCompareConfiguratorMain(LobbySubView, VehicleCompareConfiguratorMainMeta):
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)

    def __init__(self, ctx = None):
        super(VehicleCompareConfiguratorMain, self).__init__(ctx)
        self.__vehIndex = ctx.get('index')
        raise isinstance(self.__vehIndex, int) or AssertionError
        raise 0 <= self.__vehIndex < self.comparisonBasket.getVehiclesCount() or AssertionError
        self.__backAlias = ctx.get('previewAlias', VIEW_ALIAS.VEHICLE_COMPARE)
        self.__vehicle = None
        self.__crewSkillsManager = None
        self.__views = {}
        self.__topModules = None
        self.__stockModules = None
        self.__selectedShellIndex = None
        return

    def as_showViewS(self, alias):
        result = super(VehicleCompareConfiguratorMain, self).as_showViewS(alias)
        if alias in self.__views:
            self.__views[alias].onShow()
        return result

    def getCurrentVehicle(self):
        return self.__vehicle

    def getInitialVehicleData(self):
        """
        Provides vehicle corresponded to the vehicle if it is in hanger otherwise provides stock vehicle
        :return: Vehicle.Vehicle, _CrewSkillsManager;
        _CrewSkillsManager required to properly initialize and apply crew on vehicle
        """
        basketVehicle = self.getBasketVehCmpData()
        if basketVehicle.isInInventory():
            strCD = basketVehicle.getInvVehStrCD()
            crewLvl, crewSkills = basketVehicle.getInventoryCrewData()
            equipment = basketVehicle.getInvEquipment()
        else:
            strCD = basketVehicle.getStockVehStrCD()
            crewLvl = basketVehicle.getStockCrewLvl()
            crewSkills = basketVehicle.getStockCrewSkills()
            equipment = basketVehicle.getStockEquipment()
        vehicle = Vehicle(strCD)
        for slotIndex in xrange(len(equipment)):
            cmp_helpers.installEquipmentOnVehicle(vehicle, equipment[slotIndex], slotIndex)

        cmp_helpers.applyCamouflage(vehicle, basketVehicle.invHasCamouflage())
        return (vehicle, _CrewSkillsManager(vehicle, crewLvl, crewSkills))

    def getCurrentCrewSkills(self):
        return self.__crewSkillsManager.getSelectedSkills()

    def getCurrentCrewSkillLevel(self):
        return self.__crewSkillsManager.getCrewSkillLevel()

    def getBasketVehCmpData(self):
        return self.comparisonBasket.getVehicleAt(self.__vehIndex)

    def getVehicleWithAppliedSkill(self, skillName):
        vehicle = self._getCurrentVehicleCopy()
        if self.__crewSkillsManager.applySkillForTheSameVehicle(vehicle, skillName):
            return vehicle
        else:
            return None

    def getCurrentShellIndex(self):
        return self.__selectedShellIndex

    def isTopModulesFromStock(self):
        topModules = self.__getTopModules()
        stockModules = self.__getStockModules()
        return all(map(lambda item: item in stockModules, topModules))

    def isTopModulesSelected(self):
        topModules = self.__getTopModules()
        selectedModules = cmp_helpers.getVehicleModules(self.__vehicle)
        return all(map(lambda item: item in selectedModules, topModules))

    def isCamouflageSet(self):
        return cmp_helpers.isCamouflageSet(self.__vehicle)

    def applyNewParameters(self):
        """
        Transfers new selected parameters to comparison basket (save parameters)
        """
        self.comparisonBasket.applyNewParameters(self.__vehIndex, self.__vehicle, self.getCurrentCrewSkillLevel(), self.getCurrentCrewSkills(), self.getCurrentShellIndex())

    def isDifferentWithInitialBasketVeh(self):
        basketVehicle = self.getBasketVehCmpData()
        if basketVehicle.isInInventory():
            basketVehCrewLvl, basketVehCrewSkills = basketVehicle.getInventoryCrewData()
            equipment = basketVehicle.getInvEquipment()
            strCD = basketVehicle.getInvVehStrCD()
        else:
            basketVehCrewLvl = basketVehicle.getStockCrewLvl()
            basketVehCrewSkills = basketVehicle.getStockCrewSkills()
            equipment = basketVehicle.getStockEquipment()
            strCD = basketVehicle.getStockVehStrCD()
        return self.__isHasDifferences(strCD, equipment, basketVehCrewLvl, basketVehCrewSkills, basketVehicle.getInventoryShellIndex(), basketVehicle.invHasCamouflage())

    def isCurrentVehicleModified(self):
        basketVehicle = self.getBasketVehCmpData()
        crewLvl, crewSkills = basketVehicle.getCrewData()
        return self.__isHasDifferences(basketVehicle.getVehicleStrCD(), basketVehicle.getEquipment(), crewLvl, crewSkills, basketVehicle.getSelectedShellIndex(), basketVehicle.hasCamouflage())

    def __isHasDifferences(self, strCD, equipment, basketVehCrewLvl, basketVehCrewSkills, selShellIndex, hasCamouflage):
        if basketVehCrewLvl != self.getCurrentCrewSkillLevel():
            return True
        elif basketVehCrewSkills != self.getCurrentCrewSkills():
            return True
        elif not cmp_helpers.isEquipmentSame(equipment, [ (eq.intCD if eq else None) for eq in self.__vehicle.eqs ]):
            return True
        elif selShellIndex != self.__selectedShellIndex:
            return True
        currVehHasCamouflage = cmp_helpers.isCamouflageSet(self.__vehicle)
        if hasCamouflage != currVehHasCamouflage:
            return True
        if currVehHasCamouflage:
            targetVehicle = Vehicle(self.__vehicle.descriptor.makeCompactDescr())
            cmp_helpers.removeVehicleCamouflages(targetVehicle)
        else:
            targetVehicle = self.__vehicle
        if strCD != targetVehicle.descriptor.makeCompactDescr():
            return True
        else:
            return False

    def setModules(self, modules):
        if modules:
            notFittedReasons = []
            oldGunIntCD = self.__vehicle.gun.intCD
            _installModulesSet(self.__vehicle, list(modules[:]), notFittedReasons)
            if notFittedReasons:
                for notFitReason in notFittedReasons:
                    LOG_DEBUG('Module has not been installed properly, reason: {}'.format(notFitReason))

            if oldGunIntCD != self.__vehicle.gun.intCD:
                firstShellIndex = 0
                newShellIndex = -1
                if self.__updateSelectedShell(firstShellIndex):
                    newShellIndex = firstShellIndex
                self.__notifyViews('onShellsUpdated', updateShells=True, selectedIndex=newShellIndex)
            else:
                newGunToInstall = findFirst(lambda module: module.itemTypeID == GUI_ITEM_TYPE.GUN, modules, None)
                if newGunToInstall is not None:
                    self.__vehicle.descriptor.activeGunShotIndex = self.__selectedShellIndex
            self.__notifyViews('onModulesUpdated')
        return

    def selectTopModules(self, select):
        if select:
            modules = self.__getTopModules()
        else:
            modules = self.__getStockModules()
        self.setModules(modules)

    def selectShell(self, slotIndex):
        if self.__updateSelectedShell(slotIndex):
            self.__notifyViews('onShellsUpdated', selectedIndex=slotIndex)

    def selectCamouflage(self, select):
        cmp_helpers.applyCamouflage(self.__vehicle, select)
        self.__notifyViews('onCamouflageUpdated')

    def resetToDefault(self):
        self.__vehicle, self.__crewSkillsManager = self.getInitialVehicleData()
        basketShellIndex = self.getBasketVehCmpData().getInventoryShellIndex()
        newShellIndex = -1
        if self.__updateSelectedShell(basketShellIndex):
            newShellIndex = basketShellIndex
        self.__notifyViews('onShellsUpdated', updateShells=True, selectedIndex=newShellIndex)
        self.__notifyViews('onResetToDefault')
        self.__notifyViews('onCamouflageUpdated')

    def installOptionalDevice(self, newId, slotIndex):
        newId = int(newId)
        optDev = g_itemsCache.items.getItemByCD(newId)
        itemTypeID = optDev.itemTypeID
        mayInstall, reason = optDev.mayInstall(self.__vehicle, slotIndex)
        if mayInstall:
            self.__vehicle.descriptor.installOptionalDevice(optDev.intCD, slotIndex)
            self.__vehicle.optDevices[slotIndex] = optDev
            self.__notifyViews('onOptDeviceUpdated')
        else:
            LOG_WARNING('Component "{}" has not been installed. Reason: {}.'.format(itemTypeID, reason))

    def removeOptionalDevice(self, slotIndex):
        installedDevice = self.__vehicle.optDevices[slotIndex]
        if installedDevice is not None:
            self.__launchOptDeviceRemoving(installedDevice, slotIndex)
        else:
            LOG_WARNING("Couldn't remove optional device from slot {} because slot is already empty!".format(slotIndex))
        return

    def installEquipment(self, newId, slotIndex):
        self.__installEquipment(newId, slotIndex)
        self.__notifyViews('onEquipmentUpdated')

    def removeEquipment(self, slotIndex):
        self.__installEquipment(None, slotIndex)
        self.__notifyViews('onEquipmentUpdated')
        return

    def selectCrewSkill(self, skillType, selected):
        if not skillType in PARAMS_AFFECTED_TANKMEN_SKILLS:
            raise AssertionError
            savedValue = skillType in self.__crewSkillsManager.getSelectedSkills()
            if selected != savedValue:
                self.__crewSkillsManager.toggleSkill(skillType) and self.__notifyViews('onCrewSkillUpdated')
        else:
            LOG_WARNING('Attempt to apply the same value for {} = {}'.format(skillType, selected))

    def selectCrewLevel(self, crewLevelId):
        if self.__crewSkillsManager.changeCrewSkillLevel(crewLevelId):
            self.__notifyViews('onCrewLevelUpdated', crewLevelId)

    def closeView(self, forcedBackAliace = None):
        event = g_entitiesFactories.makeLoadEvent(forcedBackAliace or self.__backAlias)
        self.fireEvent(event, scope=EVENT_BUS_SCOPE.LOBBY)

    def _getCurrentVehicleCopy(self):
        vehicle = Vehicle(strCompactDescr=self.__vehicle.descriptor.makeCompactDescr())
        vehicle.crew = self.__vehicle.crew[:]
        for i, equipment in enumerate(self.__vehicle.eqs):
            cmp_helpers.installEquipmentOnVehicle(vehicle, equipment.intCD if equipment else None, i)

        vehicle.descriptor.activeGunShotIndex = self.__vehicle.descriptor.activeGunShotIndex
        return vehicle

    def _populate(self):
        super(VehicleCompareConfiguratorMain, self)._populate()
        self.comparisonBasket.onSwitchChange += self.__onBasketStateChanged
        basketVehcileData = self.getBasketVehCmpData()
        basketVehCrewLvl, basketVehCrewSkills = basketVehcileData.getCrewData()
        self.__vehicle = Vehicle(basketVehcileData.getVehicleStrCD())
        self.__crewSkillsManager = _CrewSkillsManager(self.__vehicle, basketVehCrewLvl, basketVehCrewSkills)
        equipment = basketVehcileData.getEquipment()
        for slotIndex in xrange(len(equipment)):
            self.__installEquipment(equipment[slotIndex], slotIndex)

        cmp_helpers.applyCamouflage(self.__vehicle, basketVehcileData.hasCamouflage())
        self.__updateSelectedShell(basketVehcileData.getSelectedShellIndex())
        self.as_showViewS(VEHICLE_COMPARE_CONSTANTS.VEHICLE_CONFIGURATOR_VIEW)
        self.comparisonBasket.isLocked = True

    def _dispose(self):
        self.comparisonBasket.onSwitchChange -= self.__onBasketStateChanged
        self.__views = None
        self.comparisonBasket.isLocked = False
        super(VehicleCompareConfiguratorMain, self)._dispose()
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(VehicleCompareConfiguratorMain, self)._onRegisterFlashComponent(viewPy, alias)
        if isinstance(viewPy, VehicleCompareConfiguratorBaseView):
            self.__views[alias] = viewPy
            viewPy.setContainer(self)

    @process
    def __launchOptDeviceRemoving(self, installedDevice, slotIndex):
        result = yield _CmpOptDeviceRemover(self.__vehicle, installedDevice, slotIndex).request()
        if result.success:
            self.__notifyViews('onOptDeviceUpdated')
        else:
            processMsg(result)

    def __getTopModules(self):
        if self.__topModules is None:
            self.__topModules = cmp_helpers.getVehicleTopModules(self.__vehicle)
        return self.__topModules

    def __getStockModules(self):
        if self.__stockModules is None:
            self.__stockModules = tuple(reversed(cmp_helpers.getVehicleModules(Vehicle(self.getBasketVehCmpData().getStockVehStrCD()))))
        return self.__stockModules

    def __installEquipment(self, intCD, slotIndex):
        cmp_helpers.installEquipmentOnVehicle(self.__vehicle, intCD, slotIndex)

    def __updateSelectedShell(self, slotIndex):
        """
        Updates vehicle and interanal selectedShellIndex property
        :param slotIndex: new index to select
        :return: True if index has been successfully changed
        """
        slotIndex = int(slotIndex)
        if self.__selectedShellIndex != slotIndex:
            self.__vehicle.descriptor.activeGunShotIndex = slotIndex
            self.__selectedShellIndex = slotIndex
            return True
        return False

    def __onBasketStateChanged(self):
        if not self.comparisonBasket.isEnabled():
            self.closeView(VIEW_ALIAS.LOBBY_HANGAR)

    def __notifyViews(self, event, *args, **kwargs):
        for component in self.__views.itervalues():
            notifier = getattr(component, event)
            if notifier and callable(notifier):
                notifier(*args, **kwargs)
            else:
                self.closeView(VIEW_ALIAS.LOBBY_HANGAR)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\vehicle_compare\cmp_configurator_view.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:10 St�edn� Evropa (letn� �as)
