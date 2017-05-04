# 2017.05.04 15:24:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleParametersMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehicleParametersMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onParamClick(self, paramID):
        self._printOverrideError('onParamClick')

    def onListScroll(self):
        self._printOverrideError('onListScroll')

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()

    def as_setIsParamsAnimatedS(self, isParamsAnimated):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsParamsAnimated(isParamsAnimated)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\VehicleParametersMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:41 Støední Evropa (letní èas)
