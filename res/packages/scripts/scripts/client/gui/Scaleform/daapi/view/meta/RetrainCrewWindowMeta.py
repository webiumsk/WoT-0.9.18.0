# 2017.05.04 15:24:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RetrainCrewWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class RetrainCrewWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def submit(self, operationId):
        self._printOverrideError('submit')

    def changeRetrainType(self, retrainTypeIndex):
        self._printOverrideError('changeRetrainType')

    def as_setCrewDataS(self, data):
        """
        :param data: Represented by RetrainCrewBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewData(data)

    def as_setVehicleDataS(self, data):
        """
        :param data: Represented by RetrainVehicleBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleData(data)

    def as_setCrewOperationDataS(self, data):
        """
        :param data: Represented by RetrainCrewOperationVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewOperationData(data)

    def as_setAllCrewDataS(self, data):
        """
        :param data: Represented by RetrainCrewBlockVOBase (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setAllCrewData(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\RetrainCrewWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:37 Støední Evropa (letní èas)
