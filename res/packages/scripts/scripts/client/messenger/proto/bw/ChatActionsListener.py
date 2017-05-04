# 2017.05.04 15:27:12 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/proto/bw/ChatActionsListener.py
from ChatManager import chatManager
from debug_utils import LOG_ERROR

class ChatActionsListener(object):

    def __init__(self, responseHandlers = None):
        super(ChatActionsListener, self).__init__()
        if responseHandlers is not None:
            self._responseHandlers = responseHandlers
        else:
            self._responseHandlers = {}
        return

    def addListener(self, callback, action, cid = None):
        chatManager.subscribeChatAction(callback, action, cid)

    def removeListener(self, callback, action, cid = None):
        chatManager.unsubscribeChatAction(callback, action, cid)

    def removeAllListeners(self):
        chatManager.unsubcribeAllChatActions()

    def handleChatActionFailureEvent(self, actionResponse, chatAction):
        handler = self._responseHandlers.get(actionResponse)
        if handler is None:
            return False
        elif hasattr(self, handler):
            return getattr(self, handler)(actionResponse, chatAction)
        else:
            LOG_ERROR('handleChatActionFailureEvent: response handler for response %s(%s) not registered' % (actionResponse, actionResponse.index()))
            return False
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\bw\ChatActionsListener.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:12 Støední Evropa (letní èas)
