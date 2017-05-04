# 2017.05.04 15:22:00 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/base/squad/ctx.py
from constants import PREBATTLE_TYPE
from gui.prb_control import settings as prb_settings
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getWaitingID', 'waitingID'), ('getFlagsToStrings', 'flags'))

class SquadSettingsCtx(UnitRequestCtx):
    """
    Context for changing squad settings.
    """
    __slots__ = ('__accountsToInvite',)

    def __init__(self, entityType = PREBATTLE_TYPE.SQUAD, waitingID = '', flags = prb_settings.FUNCTIONAL_FLAG.UNDEFINED, accountsToInvite = None, isForced = False):
        super(SquadSettingsCtx, self).__init__(entityType=entityType, waitingID=waitingID, flags=flags, isForced=isForced)
        self.__accountsToInvite = accountsToInvite or []

    def getRequestType(self):
        return prb_settings.REQUEST_TYPE.CREATE

    def getID(self):
        """
        Stub to looks like other create contexts
        """
        return 0

    def getAccountsToInvite(self):
        """
        Getter for accounts to invite list
        """
        return self.__accountsToInvite
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\squad\ctx.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:00 Støední Evropa (letní èas)
