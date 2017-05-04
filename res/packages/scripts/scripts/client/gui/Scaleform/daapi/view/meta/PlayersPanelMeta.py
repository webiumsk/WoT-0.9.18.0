# 2017.05.04 15:24:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PlayersPanelMeta.py
from gui.Scaleform.daapi.view.battle.classic.base_stats import StatsBase

class PlayersPanelMeta(StatsBase):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends StatsBase
    """

    def tryToSetPanelModeByMouse(self, panelMode):
        self._printOverrideError('tryToSetPanelModeByMouse')

    def switchToOtherPlayer(self, vehicleID):
        self._printOverrideError('switchToOtherPlayer')

    def as_setPanelModeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelMode(value)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\PlayersPanelMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:33 Støední Evropa (letní èas)
