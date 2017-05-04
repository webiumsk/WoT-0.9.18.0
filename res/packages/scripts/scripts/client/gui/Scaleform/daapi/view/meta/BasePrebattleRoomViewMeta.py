# 2017.05.04 15:24:16 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BasePrebattleRoomViewMeta.py
from gui.Scaleform.daapi.view.lobby.rally.AbstractRallyView import AbstractRallyView

class BasePrebattleRoomViewMeta(AbstractRallyView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractRallyView
    """

    def requestToReady(self, value):
        self._printOverrideError('requestToReady')

    def requestToLeave(self):
        self._printOverrideError('requestToLeave')

    def showPrebattleSendInvitesWindow(self):
        self._printOverrideError('showPrebattleSendInvitesWindow')

    def canSendInvite(self):
        self._printOverrideError('canSendInvite')

    def canKickPlayer(self):
        self._printOverrideError('canKickPlayer')

    def isPlayerReady(self):
        self._printOverrideError('isPlayerReady')

    def isPlayerCreator(self):
        self._printOverrideError('isPlayerCreator')

    def isReadyBtnEnabled(self):
        self._printOverrideError('isReadyBtnEnabled')

    def isLeaveBtnEnabled(self):
        self._printOverrideError('isLeaveBtnEnabled')

    def getClientID(self):
        self._printOverrideError('getClientID')

    def as_setRosterListS(self, team, assigned, rosters):
        """
        :param rosters: Represented by DataProvider (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRosterList(team, assigned, rosters)

    def as_setPlayerStateS(self, team, assigned, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerState(team, assigned, data)

    def as_enableLeaveBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableLeaveBtn(value)

    def as_enableReadyBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableReadyBtn(value)

    def as_setCoolDownForReadyButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownForReadyButton(value)

    def as_resetReadyButtonCoolDownS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetReadyButtonCoolDown()

    def as_toggleReadyBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleReadyBtn(value)

    def as_refreshPermissionsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_refreshPermissions()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BasePrebattleRoomViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:16 St�edn� Evropa (letn� �as)
