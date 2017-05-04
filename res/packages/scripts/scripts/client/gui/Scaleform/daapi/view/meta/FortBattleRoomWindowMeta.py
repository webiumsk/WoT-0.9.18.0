# 2017.05.04 15:24:25 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBattleRoomWindowMeta.py
from gui.Scaleform.daapi.view.lobby.rally.RallyMainWindowWithSearch import RallyMainWindowWithSearch

class FortBattleRoomWindowMeta(RallyMainWindowWithSearch):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends RallyMainWindowWithSearch
    """

    def onBrowseClanBattles(self):
        self._printOverrideError('onBrowseClanBattles')

    def onJoinClanBattle(self, rallyId, slotIndex, peripheryId):
        self._printOverrideError('onJoinClanBattle')

    def onCreatedBattleRoom(self, battleID, peripheryId):
        self._printOverrideError('onCreatedBattleRoom')

    def refresh(self):
        self._printOverrideError('refresh')

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)

    def as_setWaitingS(self, visible, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setWaiting(visible, message)

    def as_setInfoS(self, visible, message, buttonLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfo(visible, message, buttonLabel)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortBattleRoomWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:25 Støední Evropa (letní èas)
