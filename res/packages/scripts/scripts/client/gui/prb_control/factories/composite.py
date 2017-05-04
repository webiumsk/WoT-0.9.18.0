# 2017.05.04 15:22:16 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/factories/composite.py
from debug_utils import LOG_ERROR
from gui.prb_control.factories.ControlFactory import ControlFactory
from gui.prb_control.factories.PreQueueFactory import PreQueueFactory
from gui.prb_control.factories.LegacyFactory import LegacyFactory
from gui.prb_control.factories.UnitFactory import UnitFactory
from gui.prb_control.settings import CTRL_ENTITY_TYPE
_ORDER_TO_CREATE = (CTRL_ENTITY_TYPE.LEGACY, CTRL_ENTITY_TYPE.UNIT, CTRL_ENTITY_TYPE.PREQUEUE)

class ControlFactoryComposite(ControlFactory):
    """
    Class to contain factories of supported entities on client.
    This entities are:
    - legacy;
    - unit;
    - preQueue.
    """

    def __init__(self):
        """
        Initialization of nested factories.
        """
        self.__factories = {CTRL_ENTITY_TYPE.LEGACY: LegacyFactory(),
         CTRL_ENTITY_TYPE.UNIT: UnitFactory(),
         CTRL_ENTITY_TYPE.PREQUEUE: PreQueueFactory()}

    def clear(self):
        """
        Clears factories.
        """
        self.__factories.clear()

    def get(self, ctrlType):
        """
        Gets factory by type.
        Args:
            ctrlType: control type
        
        Returns:
            instance of factory
        """
        if ctrlType in self.__factories:
            return self.__factories[ctrlType]
        else:
            return None

    def createEntry(self, ctx):
        """
        Creates entry point for given request context.
        Args:
            ctx: creation context
        
        Returns:
            entry point
        """
        ctrlType = ctx.getCtrlType()
        if ctrlType in self.__factories:
            return self.__factories[ctrlType].createEntry(ctx)
        else:
            LOG_ERROR('Entry factory is not found', ctx)
            return None

    def createEntryByAction(self, action):
        """
        Creates entry point for given prebattle action according to order.
        Args:
            action: user's action
        
        Returns:
            entry point
        """
        for ctrlType in _ORDER_TO_CREATE:
            result = self.__factories[ctrlType].createEntryByAction(action)
            if result is not None:
                return result

        return

    def createEntity(self, ctx):
        """
        Creates entry point for given context according to order.
        Args:
            ctx: creation request context
        
        Returns:
            prebattle entity
        """
        for ctrlType in _ORDER_TO_CREATE:
            result = self.__factories[ctrlType].createEntity(ctx)
            if result is not None:
                return result

        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\factories\composite.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:16 St�edn� Evropa (letn� �as)
