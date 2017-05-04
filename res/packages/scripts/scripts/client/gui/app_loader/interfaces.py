# 2017.05.04 15:21:01 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/app_loader/interfaces.py
from constants import ARENA_GUI_TYPE
from gui import GUI_CTRL_MODE_FLAG as _CTRL_FLAG

class IAppFactory(object):

    def getPackageImporter(self):
        return None

    def hasApp(self, appNS):
        return False

    def getApp(self, appNS = None):
        return None

    def getDefLobbyApp(self):
        return None

    def getDefBattleApp(self):
        return None

    def createLobby(self):
        pass

    def reloadLobbyPackages(self):
        pass

    def destroyLobby(self):
        pass

    def showLobby(self):
        pass

    def hideLobby(self):
        pass

    def showBattle(self):
        pass

    def hideBattle(self):
        pass

    def createBattle(self, arenaGuiType):
        pass

    def destroyBattle(self):
        pass

    def destroy(self):
        pass

    def hasLobby(self):
        return False

    def hasBattle(self):
        return False

    def attachCursor(self, appNS, flags = _CTRL_FLAG.GUI_ENABLED):
        pass

    def detachCursor(self, appNS):
        pass

    def syncCursor(self, appNS, flags = _CTRL_FLAG.GUI_ENABLED):
        pass

    def goToIntroVideo(self, appNS):
        pass

    def goToLogin(self, appNS):
        pass

    def goToLobby(self, appNS):
        pass

    def loadBattlePage(self, appNS, arenaGuiType = ARENA_GUI_TYPE.UNKNOWN):
        pass

    def goToBattleLoading(self, appNS):
        pass

    def goToBattlePage(self, appNS):
        pass

    def showDisconnectDialog(self, appNS, description):
        pass

    def handleKey(self, appNS, isDown, key, mods):
        return False
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\app_loader\interfaces.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:01 St�edn� Evropa (letn� �as)
