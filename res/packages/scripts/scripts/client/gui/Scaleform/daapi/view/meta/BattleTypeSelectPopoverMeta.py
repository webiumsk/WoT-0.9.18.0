# 2017.05.04 15:24:18 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleTypeSelectPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class BattleTypeSelectPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def selectFight(self, actionName):
        self._printOverrideError('selectFight')

    def demoClick(self):
        self._printOverrideError('demoClick')

    def getTooltipData(self, itemData, itemIsDisabled):
        self._printOverrideError('getTooltipData')

    def as_updateS(self, items, isShowDemonstrator, demonstratorEnabled):
        """
        :param items: Represented by DataProvider (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(items, isShowDemonstrator, demonstratorEnabled)

    def as_showMiniClientInfoS(self, description, hyperlink):
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BattleTypeSelectPopoverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:18 Støední Evropa (letní èas)
