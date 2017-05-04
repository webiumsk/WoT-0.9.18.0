# 2017.05.04 15:22:07 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/event/squad/entity.py
from constants import PREBATTLE_TYPE, QUEUE_TYPE
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.entities.base.squad.entity import SquadEntryPoint, SquadEntity
from gui.prb_control.entities.event.squad.actions_handler import EventBattleSquadActionsHandler
from gui.prb_control.entities.event.squad.actions_validator import EventBattleSquadActionsValidator
from gui.prb_control.items import SelectResult
from gui.prb_control.settings import PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG

class EventBattleSquadEntryPoint(SquadEntryPoint):
    """
    Event battle squad entry point
    """

    def __init__(self, accountsToInvite = None):
        super(EventBattleSquadEntryPoint, self).__init__(FUNCTIONAL_FLAG.EVENT, accountsToInvite)

    def _doCreate(self, unitMgr, ctx):
        unitMgr.createEventSquad()


class EventBattleSquadEntity(SquadEntity):
    """
    Event battle squad entity
    """

    def __init__(self):
        super(EventBattleSquadEntity, self).__init__(FUNCTIONAL_FLAG.EVENT, PREBATTLE_TYPE.EVENT)

    def getQueueType(self):
        return QUEUE_TYPE.EVENT_BATTLES

    def doSelectAction(self, action):
        name = action.actionName
        if name in (PREBATTLE_ACTION_NAME.SQUAD, PREBATTLE_ACTION_NAME.RANDOM):
            g_eventDispatcher.showUnitWindow(self._prbType)
            return SelectResult(True)
        return super(EventBattleSquadEntity, self).doSelectAction(action)

    def _createActionsValidator(self):
        return EventBattleSquadActionsValidator(self)

    def _createActionsHandler(self):
        return EventBattleSquadActionsHandler(self)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\event\squad\entity.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:07 St�edn� Evropa (letn� �as)
