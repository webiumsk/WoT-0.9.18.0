# 2017.05.04 15:26:58 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/gui/interfaces.py
from messenger.gui.Scaleform import FILL_COLORS

class IGUIEntry(object):

    def init(self):
        pass

    def clear(self):
        pass

    def show(self):
        pass

    def close(self, nextScope):
        pass

    @property
    def channelsCtrl(self):
        return None

    def invoke(self, method, *args, **kwargs):
        pass

    def isFocused(self):
        return False

    def handleKey(self, event):
        return False

    def addClientMessage(self, message, isCurrentPlayer = False):
        pass


class IGUIEntryDecorator(IGUIEntry):

    def getEntry(self, scope):
        pass

    def setEntry(self, scope, entry):
        pass

    def switch(self, scope):
        pass


class IControllerFactory(object):

    def init(self):
        return []

    def clear(self):
        pass

    def factory(self, entity):
        pass


class IControllersCollection(IControllerFactory):

    def getController(self, clientID):
        return None

    def hasController(self, controller):
        return False

    def getControllerByCriteria(self, criteria):
        return None

    def getControllersIterator(self):
        return None

    def removeControllers(self):
        pass


class IEntityController(object):

    def setView(self, view):
        pass

    def removeView(self):
        pass

    def clear(self):
        pass


class IChannelController(IEntityController):

    def getChannel(self):
        return None

    def join(self):
        pass

    def exit(self):
        pass

    def activate(self):
        pass

    def deactivate(self, entryClosing = False):
        pass

    def isJoined(self):
        return False

    def setHistory(self, history):
        pass

    def getHistory(self):
        return []

    def hasUnreadMessages(self):
        return len(self.getHistory()) > 0

    def setMembersDP(self, membersDP):
        pass

    def removeMembersDP(self):
        pass

    def canSendMessage(self):
        return (False, 'N/A')

    def sendMessage(self, message):
        pass

    def sendCommand(self, command):
        pass

    def addMessage(self, message, doFormatting = True):
        return False

    def addCommand(self, command):
        return ''

    def isEnabled(self):
        return True


class IBattleChannelView(object):

    def addController(self, ctrl):
        pass

    def removeController(self, ctrl):
        pass

    def addMessage(self, text, fillColor = FILL_COLORS.BLACK, accountDBID = 0):
        """
        Invoked when a new message is relieved.
        
        :param text: Formatted message text.
        :param fillColor: Color scheme.
        :param accountDBID: Sender database ID or 0 if it is not defined or a specific processing
        is not supposed.
        """
        pass
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\gui\interfaces.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:58 St�edn� Evropa (letn� �as)
