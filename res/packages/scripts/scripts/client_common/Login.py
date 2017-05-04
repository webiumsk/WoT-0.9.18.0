# 2017.05.04 15:28:12 Støední Evropa (letní èas)
# Embedded file name: scripts/client_common/Login.py
import BigWorld
from PlayerEvents import g_playerEvents
from debug_utils import LOG_DEBUG

class PlayerLogin(BigWorld.Entity):

    def __init__(self):
        pass

    def onBecomePlayer(self):
        pass

    def onBecomeNonPlayer(self):
        pass

    def onKickedFromServer(self, checkoutPeripheryID):
        LOG_DEBUG('onKickedFromServer', checkoutPeripheryID)
        g_playerEvents.onKickWhileLoginReceived(checkoutPeripheryID)

    def receiveLoginQueueNumber(self, queueNumber):
        LOG_DEBUG('receiveLoginQueueNumber', queueNumber)
        g_playerEvents.onLoginQueueNumberReceived(queueNumber)

    def handleKeyEvent(self, event):
        return False


Login = PlayerLogin
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client_common\Login.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:12 Støední Evropa (letní èas)
