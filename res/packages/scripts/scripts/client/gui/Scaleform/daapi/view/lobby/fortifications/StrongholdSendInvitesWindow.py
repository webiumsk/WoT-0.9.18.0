# 2017.05.04 15:23:25 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/StrongholdSendInvitesWindow.py
import BigWorld
from gui.prb_control.entities.stronghold.unit.ctx import SendInvitesUnitCtx
from gui.Scaleform.daapi.view.lobby.SendInvitesWindow import SendInvitesWindow
from gui.shared.utils.requesters.abstract import Response
from gui.shared.view_helpers.UsersInfoHelper import UsersInfoHelper
from client_request_lib.exceptions import ResponseCodes
from gui import SystemMessages
from gui.Scaleform.locale.INVITES import INVITES
from functools import partial

class StrongholdSendInvitesWindow(SendInvitesWindow, UsersInfoHelper):

    def sendInvites(self, accountsToInvite, comment):
        if accountsToInvite:
            self.prbEntity.request(SendInvitesUnitCtx(accountsToInvite, comment), partial(self.__sendInvitesCallback, accountsToInvite))

    def __sendInvitesCallback(self, accountsToInvite, response):
        if isinstance(response, Response) and response.getCode() == ResponseCodes.NO_ERRORS:
            for userId in accountsToInvite:
                SystemMessages.pushI18nMessage(INVITES.STRONGHOLD_INVITE_SENDINVITETOUSERNAME, type=SystemMessages.SM_TYPE.Information, name=self.getUserName(userId))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\fortifications\StrongholdSendInvitesWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:25 St�edn� Evropa (letn� �as)
