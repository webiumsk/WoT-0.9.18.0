# 2017.05.04 15:23:51 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/rally/UnitUserCMHandler.py
from account_helpers import getAccountDatabaseID
from adisp import process
from constants import PREBATTLE_TYPE
from gui.Scaleform.daapi.view.lobby.user_cm_handlers import BaseUserCMHandler, USER
from gui.Scaleform.locale.MENU import MENU
from gui.prb_control.entities.base.unit.ctx import KickPlayerUnitCtx, GiveLeadershipUnitCtx
from gui.prb_control.entities.listener import IGlobalListener
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
from UnitBase import UNIT_FLAGS
KICK_FROM_UNIT = 'kickPlayerFromUnit'
GIVE_LEADERSHIP = 'giveLeadership'
TAKE_LEADERSHIP = 'takeLeadership'

class UnitUserCMHandler(BaseUserCMHandler, IGlobalListener):

    def __init__(self, cmProxy, ctx = None):
        super(UnitUserCMHandler, self).__init__(cmProxy, ctx)
        self.startPrbListening()

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def bwProto(self):
        return None

    def isSquadCreator(self):
        return self.prbEntity.isCommander()

    def fini(self):
        self.stopPrbListening()
        super(UnitUserCMHandler, self).fini()

    def onUnitPlayerRemoved(self, pInfo):
        self.onContextMenuHide()

    def onUnitMembersListChanged(self):
        self.onContextMenuHide()

    def onCommanderIsReady(self, isReady):
        self.onContextMenuHide()

    def giveLeadership(self):
        self._giveLeadership(self.databaseID)

    def takeLeadership(self):
        self._takeLeadership()

    def kickPlayerFromUnit(self):
        self._kickPlayerFromUnit(self.databaseID)

    def _addMutedInfo(self, option, userCMInfo):
        muted = USER.UNSET_MUTED if userCMInfo.isMuted else USER.SET_MUTED
        if not userCMInfo.isIgnored:
            if self.bwProto.voipController.isVOIPEnabled():
                option.append(self._makeItem(muted, MENU.contextmenu(muted)))
        return option

    def _addSquadInfo(self, options, isIgnored):
        if self.prbEntity.getEntityType() not in PREBATTLE_TYPE.SQUAD_PREBATTLES:
            return super(UnitUserCMHandler, self)._addSquadInfo(options, isIgnored)
        return options

    def _addPrebattleInfo(self, options, userCMInfo):
        if self._canKick():
            options.append(self._makeItem(KICK_FROM_UNIT, MENU.contextmenu(KICK_FROM_UNIT)))
        if self._canGiveLeadership():
            options.append(self._makeItem(GIVE_LEADERSHIP, MENU.contextmenu(GIVE_LEADERSHIP)))
        if self._canTakeLeadership():
            options.append(self._makeItem(TAKE_LEADERSHIP, MENU.contextmenu(TAKE_LEADERSHIP)))
        return options

    def _canKick(self):
        unitEntity = self.prbEntity
        pInfo = unitEntity.getPlayerInfo(dbID=self.databaseID)
        flags = pInfo.unit.getFlags()
        isInPreArena = flags & UNIT_FLAGS.IN_PRE_ARENA > 0
        isInArena = flags & UNIT_FLAGS.IN_ARENA > 0
        canKick = self.prbEntity.getPermissions().canKick()
        if isInArena or isInPreArena:
            return canKick and not pInfo.isInSlot
        else:
            return canKick

    def _canGiveLeadership(self):
        unitEntity = self.prbEntity
        myPermissions = unitEntity.getPermissions()
        myPInfo = unitEntity.getPlayerInfo()
        permissions = unitEntity.getPermissions(dbID=self.databaseID)
        pInfo = unitEntity.getPlayerInfo(dbID=self.databaseID)
        return myPInfo.isCommander() and pInfo.isInSlot and myPermissions.canChangeLeadership() and permissions.canLead() and not pInfo.isLegionary()

    def _canTakeLeadership(self):
        unitEntity = self.prbEntity
        myPermissions = unitEntity.getPermissions()
        pInfo = unitEntity.getPlayerInfo(dbID=self.databaseID)
        return pInfo.isCommander() and myPermissions.canStealLeadership() and myPermissions.canLead()

    def _getHandlers(self):
        handlers = super(UnitUserCMHandler, self)._getHandlers()
        handlers.update({KICK_FROM_UNIT: 'kickPlayerFromUnit',
         GIVE_LEADERSHIP: 'giveLeadership',
         TAKE_LEADERSHIP: 'takeLeadership'})
        return handlers

    @process
    def _kickPlayerFromUnit(self, databaseID):
        yield self.prbDispatcher.sendPrbRequest(KickPlayerUnitCtx(databaseID, 'prebattle/kick'))

    @process
    def _giveLeadership(self, databaseID):
        yield self.prbDispatcher.sendPrbRequest(GiveLeadershipUnitCtx(databaseID, 'prebattle/giveLeadership'))

    @process
    def _takeLeadership(self):
        yield self.prbDispatcher.sendPrbRequest(GiveLeadershipUnitCtx(getAccountDatabaseID(), 'prebattle/takeLeadership'))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\rally\UnitUserCMHandler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:51 St�edn� Evropa (letn� �as)
