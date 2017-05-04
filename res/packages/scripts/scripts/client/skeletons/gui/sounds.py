# 2017.05.04 15:27:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/skeletons/gui/sounds.py


class ISoundsController(object):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self, isDisconnected = False):
        raise NotImplementedError

    @property
    def system(self):
        raise NotImplementedError

    def enable(self):
        raise NotImplementedError

    def disable(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\skeletons\gui\sounds.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:41 Støední Evropa (letní èas)
