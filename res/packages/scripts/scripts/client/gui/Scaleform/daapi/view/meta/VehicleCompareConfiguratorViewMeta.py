# 2017.05.04 15:24:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleCompareConfiguratorViewMeta.py
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_base import VehicleCompareConfiguratorBaseView

class VehicleCompareConfiguratorViewMeta(VehicleCompareConfiguratorBaseView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends VehicleCompareConfiguratorBaseView
    """

    def removeDevice(self, slotType, slotIndex):
        self._printOverrideError('removeDevice')

    def selectShell(self, shellId, slotIndex):
        self._printOverrideError('selectShell')

    def camoSelected(self, selected):
        self._printOverrideError('camoSelected')

    def showModules(self):
        self._printOverrideError('showModules')

    def toggleTopModules(self, value):
        self._printOverrideError('toggleTopModules')

    def skillSelect(self, skillType, slotIndex, selected):
        self._printOverrideError('skillSelect')

    def changeCrewLevel(self, crewLevelId):
        self._printOverrideError('changeCrewLevel')

    def as_setDevicesDataS(self, data):
        """
        :param data: Represented by Vector.<DeviceSlotVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDevicesData(data)

    def as_setAmmoS(self, shells):
        """
        :param shells: Represented by Vector.<ShellButtonVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setAmmo(shells)

    def as_setSelectedAmmoIndexS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedAmmoIndex(index)

    def as_setCamoS(self, selected):
        if self._isDAAPIInited():
            return self.flashObject.as_setCamo(selected)

    def as_setSkillsBlockedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSkillsBlocked(value)

    def as_setCrewAttentionIconVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewAttentionIconVisible(value)

    def as_setSkillsS(self, skills):
        """
        :param skills: Represented by Vector.<VehConfSkillVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSkills(skills)

    def as_setTopModulesSelectedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTopModulesSelected(value)

    def as_setCrewLevelIndexS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewLevelIndex(value)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\VehicleCompareConfiguratorViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:41 Støední Evropa (letní èas)
