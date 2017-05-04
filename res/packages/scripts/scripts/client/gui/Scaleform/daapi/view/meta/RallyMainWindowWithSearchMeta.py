# 2017.05.04 15:24:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RallyMainWindowWithSearchMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyMainWindow import BaseRallyMainWindow

class RallyMainWindowWithSearchMeta(BaseRallyMainWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyMainWindow
    """

    def onAutoMatch(self, value, values):
        self._printOverrideError('onAutoMatch')

    def autoSearchApply(self, value):
        self._printOverrideError('autoSearchApply')

    def autoSearchCancel(self, value):
        self._printOverrideError('autoSearchCancel')

    def as_autoSearchEnableBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_autoSearchEnableBtn(value)

    def as_changeAutoSearchStateS(self, value):
        """
        :param value: Represented by AutoSearchVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_changeAutoSearchState(value)

    def as_changeAutoSearchBtnsStateS(self, waitingPlayers, searchEnemy):
        if self._isDAAPIInited():
            return self.flashObject.as_changeAutoSearchBtnsState(waitingPlayers, searchEnemy)

    def as_hideAutoSearchS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideAutoSearch()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\RallyMainWindowWithSearchMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:35 Støední Evropa (letní èas)
