# 2017.05.04 15:27:39 Støední Evropa (letní èas)
# Embedded file name: scripts/client/skeletons/messenger.py


class IMessengerEntry(object):

    @property
    def protos(self):
        raise NotImplementedError

    @property
    def storage(self):
        raise NotImplementedError

    @property
    def gui(self):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def onAccountShowGUI(self):
        raise NotImplementedError

    def onAvatarInitGUI(self):
        raise NotImplementedError

    def onAvatarShowGUI(self):
        raise NotImplementedError
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\skeletons\messenger.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:39 Støední Evropa (letní èas)
