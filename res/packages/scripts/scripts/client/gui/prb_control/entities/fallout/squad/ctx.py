# 2017.05.04 15:22:09 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/fallout/squad/ctx.py
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx
from gui.prb_control.settings import REQUEST_TYPE
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('__queueType', 'queueType'), ('getWaitingID', 'waitingID'))

class ChangeFalloutQueueTypeCtx(UnitRequestCtx):
    __slots__ = ('__queueType',)

    def __init__(self, queueType, waitingID = ''):
        super(ChangeFalloutQueueTypeCtx, self).__init__(waitingID=waitingID)
        self.__queueType = queueType

    def getBattleType(self):
        return self.__queueType

    def getRequestType(self):
        return REQUEST_TYPE.CHANGE_FALLOUT_QUEUE_TYPE
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\fallout\squad\ctx.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:09 Støední Evropa (letní èas)
