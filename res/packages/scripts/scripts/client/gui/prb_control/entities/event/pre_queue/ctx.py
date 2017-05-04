# 2017.05.04 15:22:06 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/event/pre_queue/ctx.py
from constants import QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getVehicleInventoryIDs', 'vInvIDs'))

class EventBattleQueueCtx(QueueCtx):
    """
    Context to enqueue event battles
    """

    def __init__(self, vehInvIDs, waitingID = ''):
        super(EventBattleQueueCtx, self).__init__(entityType=QUEUE_TYPE.EVENT_BATTLES, waitingID=waitingID)
        self.__vehInvIDs = vehInvIDs

    def getVehicleInventoryIDs(self):
        """
        Getter for selected vehicles inventory IDs
        """
        return self.__vehInvIDs
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\event\pre_queue\ctx.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:06 Støední Evropa (letní èas)
