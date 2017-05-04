# 2017.05.04 15:27:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/skeletons/gui/prb_control.py


class IPrbControlLoader(object):
    __slots__ = ()

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def getDispatcher(self):
        raise NotImplementedError

    def getInvitesManager(self):
        raise NotImplementedError

    def getAutoInvitesNotifier(self):
        raise NotImplementedError

    def getPeripheriesHandler(self):
        raise NotImplementedError

    def getStorage(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def setEnabled(self, enabled):
        raise NotImplementedError

    def onAccountShowGUI(self, ctx):
        raise NotImplementedError

    def onAvatarBecomePlayer(self):
        raise NotImplementedError

    def onDisconnected(self):
        raise NotImplementedError
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\skeletons\gui\prb_control.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:41 Støední Evropa (letní èas)
