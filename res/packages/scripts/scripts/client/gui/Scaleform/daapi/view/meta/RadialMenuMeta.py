# 2017.05.04 15:24:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RadialMenuMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RadialMenuMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onSelect(self):
        self._printOverrideError('onSelect')

    def onAction(self, action):
        self._printOverrideError('onAction')

    def as_buildDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_buildData(data)

    def as_showS(self, radialState, offset, ratio):
        if self._isDAAPIInited():
            return self.flashObject.as_show(radialState, offset, ratio)

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\RadialMenuMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:35 Støední Evropa (letní èas)
