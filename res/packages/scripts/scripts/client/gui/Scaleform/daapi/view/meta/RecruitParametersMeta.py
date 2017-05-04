# 2017.05.04 15:24:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RecruitParametersMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RecruitParametersMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onNationChanged(self, nationID):
        self._printOverrideError('onNationChanged')

    def onVehicleClassChanged(self, vehClass):
        self._printOverrideError('onVehicleClassChanged')

    def onVehicleChanged(self, vehID):
        self._printOverrideError('onVehicleChanged')

    def onTankmanRoleChanged(self, roleID):
        self._printOverrideError('onTankmanRoleChanged')

    def as_setVehicleClassDataS(self, data):
        """
        :param data: Represented by RecruitParametersVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleClassData(data)

    def as_setVehicleDataS(self, data):
        """
        :param data: Represented by RecruitParametersVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleData(data)

    def as_setTankmanRoleDataS(self, data):
        """
        :param data: Represented by RecruitParametersVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTankmanRoleData(data)

    def as_setNationsDataS(self, data):
        """
        :param data: Represented by RecruitParametersVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setNationsData(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\RecruitParametersMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:36 Støední Evropa (letní èas)
