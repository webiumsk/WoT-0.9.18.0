# 2017.05.04 15:24:30 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IngameMenuMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class IngameMenuMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def quitBattleClick(self):
        self._printOverrideError('quitBattleClick')

    def settingsClick(self):
        self._printOverrideError('settingsClick')

    def helpClick(self):
        self._printOverrideError('helpClick')

    def cancelClick(self):
        self._printOverrideError('cancelClick')

    def onCounterNeedUpdate(self):
        self._printOverrideError('onCounterNeedUpdate')

    def as_setServerSettingS(self, serverName, tooltipFullData, serverState):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerSetting(serverName, tooltipFullData, serverState)

    def as_setServerStatsS(self, stats, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStats(stats, tooltipType)

    def as_setSettingsBtnCounterS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSettingsBtnCounter(value)

    def as_removeSettingsBtnCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeSettingsBtnCounter()

    def as_setMenuButtonsLabelsS(self, helpLabel, settingsLabel, cancelLabel, quitLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setMenuButtonsLabels(helpLabel, settingsLabel, cancelLabel, quitLabel)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\IngameMenuMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:30 Støední Evropa (letní èas)
