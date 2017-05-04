# 2017.05.04 15:26:59 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/gui/Scaleform/channels/layout.py
import BattleReplay
from debug_utils import LOG_DEBUG, LOG_ERROR
from gui import SystemMessages
from messenger import g_settings
from messenger.ext import isBattleChatEnabled
from messenger.formatters.chat_message import LobbyMessageBuilder
from messenger.gui.Scaleform import FILL_COLORS
from messenger.gui.Scaleform.data.MembersDataProvider import MembersDataProvider
from messenger.gui.Scaleform.view.lobby.ChannelComponent import ChannelComponent
from messenger.gui.interfaces import IChannelController, IBattleChannelView

class LobbyLayout(IChannelController):

    def __init__(self, channel, mBuilder = None):
        self._view = None
        self._mBuilder = mBuilder or LobbyMessageBuilder()
        self._membersDP = None
        self._channel = channel
        self._activated = False
        self._isNotifyInit = False
        self._isNotifyDestroy = False
        self._addListeners()
        return

    def __del__(self):
        LOG_DEBUG('Channel controller deleted:', self)

    def getChannel(self):
        return self._channel

    def activate(self):
        self._activated = True

    def deactivate(self, entryClosing = False):
        self.removeView()
        self._activated = False

    def setView(self, view):
        if self._view:
            LOG_ERROR('View is defined', self._view)
        elif isinstance(view, ChannelComponent):
            self._view = view
            self._view.onModuleDispose += self._onModuleDispose
            self._view.setController(self)
        else:
            LOG_ERROR('View must be extends ChannelComponent', view)

    def removeView(self):
        if self._view is not None:
            self._view.removeController()
            self._view.onModuleDispose -= self._onModuleDispose
            self._view = None
        return

    def clear(self):
        self._fireDestroyEvent()
        self._removeListeners()
        self._channel = None
        self._mBuilder = None
        self.removeView()
        self.removeMembersDP()
        return

    def isJoined(self):
        return self._channel.isJoined()

    def setHistory(self, history):
        if self._channel:
            self._channel.clearHistory()
            for message in history:
                self.addMessage(message)

    def getHistory(self):
        if self._channel:
            return self._channel.getHistory()
        return []

    def setMembersDP(self, membersDP):
        if self._membersDP:
            LOG_ERROR('Member data provider is defined', self._membersDP)
        elif isinstance(membersDP, MembersDataProvider):
            self._membersDP = membersDP
            self._membersDP.buildList(self._channel.getMembers())
            self._membersDP.refresh()
        else:
            LOG_ERROR('Member data provide must be extends MembersDataProvider', membersDP)

    def removeMembersDP(self):
        if self._membersDP is not None:
            self._membersDP._dispose()
            self._membersDP = None
        return

    def sendMessage(self, message):
        result, errorMsg = self.canSendMessage()
        if result:
            self._broadcast(message)
        else:
            SystemMessages.pushI18nMessage(errorMsg, type=SystemMessages.SM_TYPE.Error)
        return result

    def addMessage(self, message, doFormatting = True):
        text = self._format(message, doFormatting)
        if self._activated:
            if self._view:
                self._view.as_addMessageS(text)
        self._channel.addMessage(text)
        return self._activated

    def addCommand(self, command):
        text = command.getCommandText()
        if self._activated and self._view:
            self._view.as_addMessageS(text)
        return text

    def fireInitEvent(self):
        if not self._isNotifyInit:
            self._fireInitEvent()
            self._isNotifyInit = True

    def fireDestroyEvent(self):
        if not self._isNotifyDestroy:
            self._fireDestroyEvent()
            self._isNotifyDestroy = True

    def _onModuleDispose(self, _):
        self._view.removeController()
        self._view.onModuleDispose -= self._onModuleDispose
        self._view = None
        return

    def _refreshMembersDP(self):
        if self._membersDP:
            self._membersDP.buildList(self._channel.getMembers())
            self._membersDP.refresh()

    def _broadcast(self, message):
        raise NotImplementedError

    def _format(self, message, doFormatting = True):
        raise NotImplementedError

    def _fireInitEvent(self):
        pass

    def _fireDestroyEvent(self):
        pass

    def _addListeners(self):
        pass

    def _removeListeners(self):
        pass


class BattleLayout(IChannelController):

    def __init__(self, channel, mBuilder, isSecondaryChannelCtrl = False):
        super(BattleLayout, self).__init__()
        self._channel = channel
        self._view = None
        self._mBuilder = mBuilder
        self._isSecondaryChannelCtrl = isSecondaryChannelCtrl
        return

    def __del__(self):
        LOG_DEBUG('Channel controller deleted:', self)

    def getChannel(self):
        return self._channel

    def getSettings(self):
        raise NotImplementedError

    def getHistory(self):
        if self._channel:
            return self._channel.getHistory()
        return []

    def isEnabled(self):
        return isBattleChatEnabled()

    def clear(self):
        self.removeView()
        self._channel = None
        self._mBuilder = None
        return

    def setView(self, view):
        if self._view:
            LOG_ERROR('View is defined', self._view)
        elif isinstance(view, IBattleChannelView):
            self._view = view
            self._view.addController(self)
        else:
            LOG_ERROR('View must be IBattleChannelView', self._view)

    def removeView(self):
        if self._view is not None:
            self._view.removeController(self)
            self._view = None
        return

    def sendMessage(self, message):
        result, errorMsg = self.canSendMessage()
        if result:
            self._broadcast(message)
        elif self._view is not None:
            self._view.addMessage(g_settings.htmlTemplates.format('battleErrorMessage', ctx={'error': errorMsg}))
        return result

    def addMessage(self, message, doFormatting = True):
        isCurrent, text = self._formatMessage(message, doFormatting)
        if not self._isSecondaryChannelCtrl:
            self._channel.addMessage(text)
        if BattleReplay.g_replayCtrl.isRecording:
            BattleReplay.g_replayCtrl.onBattleChatMessage(text, isCurrent)
        if self._view:
            if isCurrent:
                fillColor = FILL_COLORS.BROWN
            else:
                fillColor = FILL_COLORS.BLACK
            self._view.addMessage(text, fillColor=fillColor, accountDBID=message.accountDBID)
        return True

    def addCommand(self, command):
        isCurrent, text = self._formatCommand(command)
        if self._view:
            if isCurrent:
                fillColor = FILL_COLORS.BROWN
            else:
                fillColor = FILL_COLORS.BLACK
            self._view.addMessage(text, fillColor=fillColor, accountDBID=command.getSenderID())

    def _broadcast(self, message):
        raise NotImplementedError

    def _formatMessage(self, message, doFormatting = True):
        raise NotImplementedError

    def _formatCommand(self, command):
        raise NotImplementedError
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\gui\Scaleform\channels\layout.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:59 St�edn� Evropa (letn� �as)
