# 2017.05.04 15:24:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RoleChangeMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class RoleChangeMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onVehicleSelected(self, vehicleId):
        self._printOverrideError('onVehicleSelected')

    def changeRole(self, role, vehicleId):
        self._printOverrideError('changeRole')

    def as_setCommonDataS(self, data):
        """
        :param data: Represented by RoleChangeVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCommonData(data)

    def as_setRolesS(self, roles):
        """
        :param roles: Represented by Array (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRoles(roles)

    def as_setPriceS(self, priceString, enoughGold):
        if self._isDAAPIInited():
            return self.flashObject.as_setPrice(priceString, enoughGold)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\RoleChangeMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:37 Støední Evropa (letní èas)
