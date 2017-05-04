# 2017.05.04 15:24:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ColorSchemeManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ColorSchemeManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def getColorScheme(self, schemeName):
        self._printOverrideError('getColorScheme')

    def getIsColorBlind(self):
        self._printOverrideError('getIsColorBlind')

    def as_updateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_update()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\ColorSchemeManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:46 Støední Evropa (letní èas)
