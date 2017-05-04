# 2017.05.04 15:22:09 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/fallout/pre_queue/ctx.py
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getVehicleInventoryIDs', 'vInvIDs'), ('getGameplaysMask', 'gameplayMask'), ('getWaitingID', 'waitingID'))

class FalloutQueueCtx(QueueCtx):

    def __init__(self, queueType, vehInvIDs, canAddToSquad = False, waitingID = ''):
        super(FalloutQueueCtx, self).__init__(entityType=queueType, waitingID=waitingID)
        self.__vehInvIDs = vehInvIDs
        self.__canAddToSquad = canAddToSquad

    def getVehicleInventoryIDs(self):
        return list(self.__vehInvIDs)

    def canAddToSquad(self):
        return self.__canAddToSquad
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\fallout\pre_queue\ctx.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:09 Støední Evropa (letní èas)
