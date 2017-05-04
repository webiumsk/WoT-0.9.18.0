# 2017.05.04 15:24:16 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AmmunitionPanelMeta.py
from gui.Scaleform.daapi.view.meta.ModulesPanelMeta import ModulesPanelMeta

class AmmunitionPanelMeta(ModulesPanelMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ModulesPanelMeta
    """

    def showTechnicalMaintenance(self):
        self._printOverrideError('showTechnicalMaintenance')

    def showCustomization(self):
        self._printOverrideError('showCustomization')

    def toRentContinue(self):
        self._printOverrideError('toRentContinue')

    def as_setAmmoS(self, shells, stateWarning):
        """
        :param shells: Represented by Vector.<ShellButtonVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setAmmo(shells, stateWarning)

    def as_updateVehicleStatusS(self, data):
        """
        :param data: Represented by VehicleMessageVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\AmmunitionPanelMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:16 Støední Evropa (letní èas)
