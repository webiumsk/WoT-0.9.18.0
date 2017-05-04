# 2017.05.04 15:19:45 Støední Evropa (letní èas)
# Embedded file name: scripts/client/AimTrigger.py
import BigWorld
import TriggersManager

class AimTrigger(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        self.__id = TriggersManager.g_manager.addTrigger(TriggersManager.TRIGGER_TYPE.AIM, name=self.name, position=self.position, radius=self.radius, maxDistance=self.maxDistance)

    def destroy(self):
        TriggersManager.g_manager.delTrigger(self.__id)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\AimTrigger.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:19:45 Støední Evropa (letní èas)
