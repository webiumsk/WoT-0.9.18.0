# 2017.05.04 15:24:16 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseBattleLoadingMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BaseBattleLoadingMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setProgressS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(value)

    def as_setMapIconS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapIcon(source)

    def as_setPlayerDataS(self, playerVehicleID, prebattleID):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerData(playerVehicleID, prebattleID)

    def as_setEventInfoPanelDataS(self, data):
        """
        :param data: Represented by EventInfoPanelVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setEventInfoPanelData(data)

    def as_setTipS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTip(value)

    def as_setTipTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTipTitle(title)

    def as_setVisualTipInfoS(self, data):
        """
        :param data: Represented by VisualTipInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVisualTipInfo(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BaseBattleLoadingMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:16 Støední Evropa (letní èas)
