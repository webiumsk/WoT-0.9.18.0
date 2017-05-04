# 2017.05.04 15:24:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleModulesViewMeta.py
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_base import VehicleCompareConfiguratorBaseView

class VehicleModulesViewMeta(VehicleCompareConfiguratorBaseView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends VehicleCompareConfiguratorBaseView
    """

    def onModuleHover(self, id):
        self._printOverrideError('onModuleHover')

    def onModuleClick(self, id):
        self._printOverrideError('onModuleClick')

    def as_setItemS(self, nation, raw):
        if self._isDAAPIInited():
            return self.flashObject.as_setItem(nation, raw)

    def as_setNodesStatesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNodesStates(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\VehicleModulesViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:41 Støední Evropa (letní èas)
