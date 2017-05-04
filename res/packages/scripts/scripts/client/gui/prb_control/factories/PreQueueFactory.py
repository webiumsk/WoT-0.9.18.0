# 2017.05.04 15:22:17 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/factories/PreQueueFactory.py
import inspect
import gui.prb_control.prb_getters
from constants import QUEUE_TYPE
from debug_utils import LOG_ERROR
from gui.prb_control.factories.ControlFactory import ControlFactory
from gui.prb_control.entities.base.pre_queue.ctx import LeavePreQueueCtx
from gui.prb_control.entities.fallout.pre_queue.entity import FalloutClassicEntity, FalloutMultiTeamEntity
from gui.prb_control.entities.fallout.pre_queue.entity import NoFalloutEntity
from gui.prb_control.entities.fallout.pre_queue.entity import FalloutClassicEntryPoint, FalloutMultiTeamEntryPoint
from gui.prb_control.entities.fallout.pre_queue.entity import NoFalloutEntryPoint
from gui.prb_control.entities.fallout.pre_queue.entity import falloutQueueTypeFactory
from gui.prb_control.entities.random.pre_queue.entity import RandomEntity, RandomEntryPoint
from gui.prb_control.entities.sandbox.pre_queue.entity import SandboxEntity, SandboxEntryPoint
from gui.prb_control.entities.tutorial.pre_queue.entity import TutorialEntity, TutorialEntryPoint
from gui.prb_control.items import FunctionalState
from gui.prb_control.settings import FUNCTIONAL_FLAG as _FLAG, FUNCTIONAL_FLAG
from gui.prb_control.settings import PREBATTLE_ACTION_NAME, CTRL_ENTITY_TYPE
from gui.prb_control.storages import prequeue_storage_getter
__all__ = ('PreQueueFactory',)
_SUPPORTED_QUEUES = {QUEUE_TYPE.RANDOMS: RandomEntity,
 QUEUE_TYPE.FALLOUT_CLASSIC: FalloutClassicEntity,
 QUEUE_TYPE.FALLOUT_MULTITEAM: FalloutMultiTeamEntity,
 QUEUE_TYPE.TUTORIAL: TutorialEntity,
 QUEUE_TYPE.SANDBOX: SandboxEntity}
_SUPPORTED_ENTRY_BY_ACTION = {PREBATTLE_ACTION_NAME.RANDOM: RandomEntryPoint,
 PREBATTLE_ACTION_NAME.FALLOUT: NoFalloutEntryPoint,
 PREBATTLE_ACTION_NAME.FALLOUT_CLASSIC: FalloutClassicEntryPoint,
 PREBATTLE_ACTION_NAME.FALLOUT_MULTITEAM: FalloutMultiTeamEntryPoint,
 PREBATTLE_ACTION_NAME.BATTLE_TUTORIAL: TutorialEntryPoint,
 PREBATTLE_ACTION_NAME.SANDBOX: SandboxEntryPoint}

class PreQueueFactory(ControlFactory):
    """
    Creates entry point, ctx or entity for prequeue control.
    """

    @prequeue_storage_getter(QUEUE_TYPE.FALLOUT)
    def falloutStorage(self):
        """
        Decorated property getter for fallout storage.
        """
        return None

    @prequeue_storage_getter(QUEUE_TYPE.SANDBOX)
    def pveStorage(self):
        """
        Decorated property getter for PvE storage.
        """
        return None

    def createEntry(self, ctx):
        """
        Routine can not be invoke, i.e. preQueue entity has not any entries.
        """
        LOG_ERROR('preQueue functional has not any entries')
        return None

    def createEntryByAction(self, action):
        return self._createEntryByAction(action, _SUPPORTED_ENTRY_BY_ACTION)

    def createEntity(self, ctx):
        if ctx.getCtrlType() == CTRL_ENTITY_TYPE.PREQUEUE:
            queueType = ctx.getEntityType()
            if queueType:
                created = self.__createByQueueType(queueType, ctx)
            else:
                created = self.__createDefaultEntity(ctx)
        else:
            created = self.__createByAccountState(ctx)
        return created

    def createStateEntity(self, entity):
        return FunctionalState(CTRL_ENTITY_TYPE.PREQUEUE, entity.getEntityType(), True, entity.isInQueue(), funcFlags=entity.getFunctionalFlags())

    def createLeaveCtx(self, flags = FUNCTIONAL_FLAG.UNDEFINED, entityType = 0):
        return LeavePreQueueCtx(waitingID='prebattle/leave', flags=flags, entityType=entityType)

    def __createByAccountState(self, ctx):
        """
        Tries to create entity by current account state.
        Args:
            ctx: creation request context.
        
        Returns:
            new prebattle prequeue entity
        """
        queueType = gui.prb_control.prb_getters.getQueueType()
        if queueType:
            return self.__createByQueueType(queueType, ctx)
        return self.__createDefaultEntity(ctx)

    def __createByQueueType(self, queueType, ctx):
        """
        Tries to create entity by given queue type.
        Args:
            queueType: queue type
            ctx: creation request context.
        
        Returns:
            new prebattle prequeue entity
        """
        if ctx.getCtrlType() != CTRL_ENTITY_TYPE.PREQUEUE:
            return self.__createDefaultEntity(ctx)
        else:
            clazz = queueType in _SUPPORTED_QUEUES and _SUPPORTED_QUEUES[queueType]
            if not inspect.isclass(clazz):
                raise AssertionError('Class is not found, checks settings')
                created = clazz()
                return created
            return None

    def __createDefaultEntity(self, ctx):
        """
        Creates default entity for prequeue.
        Args:
            ctx: creation request context.
        
        Returns:
            new prebattle prequeue entity
        """
        created = self.__createDefaultByStorage(ctx)
        if created is None:
            if ctx.hasFlags(_FLAG.FALLOUT):
                created = NoFalloutEntity()
            else:
                created = RandomEntity()
        return created

    def __createDefaultByStorage(self, ctx):
        """
        Tries to create default entity for prequeue by storage.
        Args:
            ctx: creation request context.
        
        Returns:
            new prebattle prequeue entity
        """
        if self.falloutStorage.isModeSelected():
            return falloutQueueTypeFactory(self.falloutStorage.getBattleType())
        elif self.pveStorage.isModeSelected():
            return SandboxEntity()
        else:
            return None
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\factories\PreQueueFactory.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:17 St�edn� Evropa (letn� �as)
