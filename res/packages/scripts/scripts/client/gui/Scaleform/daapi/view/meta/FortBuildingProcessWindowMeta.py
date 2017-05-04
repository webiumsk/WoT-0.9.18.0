# 2017.05.04 15:24:26 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBuildingProcessWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortBuildingProcessWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def requestBuildingInfo(self, uid):
        self._printOverrideError('requestBuildingInfo')

    def applyBuildingProcess(self, uid):
        self._printOverrideError('applyBuildingProcess')

    def as_setDataS(self, data):
        """
        :param data: Represented by BuildingProcessVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_responseBuildingInfoS(self, data):
        """
        :param data: Represented by BuildingProcessInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_responseBuildingInfo(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortBuildingProcessWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:26 Støední Evropa (letní èas)
