# 2017.05.04 15:24:32 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MinimapGridMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MinimapGridMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def setClick(self, x, y):
        self._printOverrideError('setClick')

    def as_clickEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_clickEnabled(value)

    def as_addPointS(self, x, y):
        if self._isDAAPIInited():
            return self.flashObject.as_addPoint(x, y)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\MinimapGridMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:32 Støední Evropa (letní èas)
