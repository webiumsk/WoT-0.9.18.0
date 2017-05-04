# 2017.05.04 15:27:34 Støední Evropa (letní èas)
# Embedded file name: scripts/client/notification/BaseMessagesController.py


class BaseMessagesController(object):

    def __init__(self, model):
        self._model = model

    def cleanUp(self):
        self._model = None
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\notification\BaseMessagesController.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:34 Støední Evropa (letní èas)
