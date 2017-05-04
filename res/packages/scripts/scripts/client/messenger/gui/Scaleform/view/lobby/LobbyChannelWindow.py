# 2017.05.04 15:27:09 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/lobby/LobbyChannelWindow.py
from constants import PREBATTLE_TYPE
from gui.Scaleform.managers.windows_stored_data import DATA_TYPE, TARGET_ID
from gui.Scaleform.managers.windows_stored_data import stored_window
from messenger.ext.channel_num_gen import getClientID4Prebattle
from messenger.gui.Scaleform.data.MembersDataProvider import MembersDataProvider
from messenger.gui.Scaleform.meta.LobbyChannelWindowMeta import LobbyChannelWindowMeta
from messenger.m_constants import PROTO_TYPE

def _tryToSetTrusted(window, storedData):
    if window.getProtoType() == PROTO_TYPE.BW_CHAT2 and window.getClientID() == getClientID4Prebattle(PREBATTLE_TYPE.TRAINING):
        storedData.setTrusted(True)


@stored_window(DATA_TYPE.CHANNEL_WINDOW, TARGET_ID.CHANNEL_CAROUSEL, sideEffect=_tryToSetTrusted)

class LobbyChannelWindow(LobbyChannelWindowMeta):

    def _populate(self):
        super(LobbyChannelWindow, self)._populate()
        channel = self._controller.getChannel()
        if channel.haveMembers():
            membersDP = MembersDataProvider()
            membersDP.setFlashObject(self.as_getMembersDPS())
            self._controller.setMembersDP(membersDP)
        else:
            self.as_hideMembersListS()

    def _dispose(self):
        if self._controller is not None:
            self._controller.removeMembersDP()
        super(LobbyChannelWindow, self)._dispose()
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\gui\Scaleform\view\lobby\LobbyChannelWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:09 Støední Evropa (letní èas)
