# 2017.05.04 15:22:21 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/storages/prb_storage.py
from gui.prb_control.storages.local_storage import LocalStorage

class TrainingStorage(LocalStorage):
    __slots__ = ('isObserver',)

    def __init__(self):
        super(TrainingStorage, self).__init__()
        self.isObserver = False

    def clear(self):
        self.isObserver = False

    def suspend(self):
        self.clear()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\storages\prb_storage.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:21 Støední Evropa (letní èas)
