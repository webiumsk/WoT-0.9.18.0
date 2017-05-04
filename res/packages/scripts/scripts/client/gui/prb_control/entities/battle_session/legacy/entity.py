# 2017.05.04 15:22:04 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/battle_session/legacy/entity.py
from constants import PREBATTLE_TYPE, QUEUE_TYPE
from gui import SystemMessages
from gui.LobbyContext import g_lobbyContext
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as I18N_SYSTEM_MESSAGES
from gui.prb_control import prb_getters
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.entities.base import vehicleAmmoCheck
from gui.prb_control.entities.base.legacy.ctx import JoinLegacyModeCtx, SetPlayerStateCtx
from gui.prb_control.entities.base.legacy.entity import LegacyEntryPoint, LegacyEntity
from gui.prb_control.entities.battle_session.legacy.limits import BattleSessionLimits
from gui.prb_control.entities.battle_session.legacy.permissions import BattleSessionPermissions
from gui.prb_control.invites import AutoInvitesNotifier
from gui.prb_control.items import prb_items, SelectResult
from gui.prb_control.settings import PREBATTLE_SETTING_NAME, FUNCTIONAL_FLAG
from gui.prb_control.settings import REQUEST_TYPE, PREBATTLE_ROSTER, PREBATTLE_ACTION_NAME
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import ChannelCarouselEvent
from helpers import i18n

class BattleSessionListEntryPoint(LegacyEntryPoint):
    """
    Battle sessions browsers entry point
    """

    def __init__(self):
        super(BattleSessionListEntryPoint, self).__init__(FUNCTIONAL_FLAG.BATTLE_SESSION)

    def isVisualOnly(self):
        return True

    def makeDefCtx(self):
        return JoinLegacyModeCtx(PREBATTLE_TYPE.CLAN)

    def create(self, ctx, callback = None):
        raise Exception('BattleSession can be created through the web only')

    def join(self, ctx, callback = None):
        g_eventDispatcher.loadBattleSessionList()
        if callback:
            callback(True)


class BattleSessionEntryPoint(LegacyEntryPoint):
    """
    Battle sessions room entry point
    """

    def __init__(self):
        super(BattleSessionEntryPoint, self).__init__(FUNCTIONAL_FLAG.BATTLE_SESSION)

    def create(self, ctx, callback = None):
        raise Exception('BattleSession can be created through the web only')

    def join(self, ctx, callback = None):
        prbID = ctx.getID()
        if not AutoInvitesNotifier.hasInvite(prbID):
            SystemMessages.pushI18nMessage(I18N_SYSTEM_MESSAGES.ARENA_START_ERRORS_JOIN_NOT_FOUND, type=SystemMessages.SM_TYPE.Error)
            if callback:
                callback(False)
            return
        peripheryID = AutoInvitesNotifier.getInvite(prbID).peripheryID
        if g_lobbyContext.isAnotherPeriphery(peripheryID):
            hostName = g_lobbyContext.getPeripheryName(peripheryID)
            if hostName:
                message = i18n.makeString(I18N_SYSTEM_MESSAGES.ARENA_START_ERRORS_JOIN_WRONG_PERIPHERY_KNOWN, hostName)
            else:
                message = i18n.makeString(I18N_SYSTEM_MESSAGES.ARENA_START_ERRORS_JOIN_WRONG_PERIPHERY_UNKNOWN)
            SystemMessages.pushMessage(message, type=SystemMessages.SM_TYPE.Warning)
            if callback:
                callback(False)
        else:
            super(BattleSessionEntryPoint, self).join(ctx, callback)


class BattleSessionEntity(LegacyEntity):
    """
    Battle sessions entity
    """

    def __init__(self, settings):
        requests = {REQUEST_TYPE.ASSIGN: self.assign,
         REQUEST_TYPE.SET_TEAM_STATE: self.setTeamState,
         REQUEST_TYPE.SET_PLAYER_STATE: self.setPlayerState,
         REQUEST_TYPE.KICK: self.kickPlayer}
        super(BattleSessionEntity, self).__init__(FUNCTIONAL_FLAG.BATTLE_SESSION, settings, permClass=BattleSessionPermissions, limits=BattleSessionLimits(self), requestHandlers=requests)

    def init(self, clientPrb = None, ctx = None):
        result = super(BattleSessionEntity, self).init(clientPrb=clientPrb, ctx=ctx)
        g_eventDispatcher.loadHangar()
        g_eventDispatcher.loadBattleSessionWindow(self.getEntityType())
        result = FUNCTIONAL_FLAG.addIfNot(result, FUNCTIONAL_FLAG.LOAD_WINDOW)
        result = FUNCTIONAL_FLAG.addIfNot(result, FUNCTIONAL_FLAG.LOAD_PAGE)
        g_eventBus.addListener(ChannelCarouselEvent.CAROUSEL_INITED, self.__handleCarouselInited, scope=EVENT_BUS_SCOPE.LOBBY)
        return result

    def isGUIProcessed(self):
        return True

    def fini(self, clientPrb = None, ctx = None, woEvents = False):
        prbType = self.getEntityType()
        result = super(BattleSessionEntity, self).fini(clientPrb=clientPrb, ctx=ctx, woEvents=woEvents)
        if not woEvents:
            if not self.canSwitch(ctx):
                g_eventDispatcher.removeSpecBattleFromCarousel(prbType)
        else:
            g_eventDispatcher.removeSpecBattleFromCarousel(prbType, closeWindow=False)
        g_eventBus.removeListener(ChannelCarouselEvent.CAROUSEL_INITED, self.__handleCarouselInited, scope=EVENT_BUS_SCOPE.LOBBY)
        return result

    def getQueueType(self):
        return QUEUE_TYPE.SPEC_BATTLE

    @vehicleAmmoCheck
    def setPlayerState(self, ctx, callback = None):
        super(BattleSessionEntity, self).setPlayerState(ctx, callback)

    def showGUI(self, ctx = None):
        g_eventDispatcher.loadBattleSessionWindow(self.getEntityType())

    def getRosters(self, keys = None):
        rosters = prb_getters.getPrebattleRosters()
        prbRosters = PREBATTLE_ROSTER.getRange(self.getEntityType(), self.getPlayerTeam())
        result = dict(((r, []) for r in prbRosters))
        for roster in prbRosters:
            if roster in rosters:
                result[roster] = map(lambda accInfo: prb_items.PlayerPrbInfo(accInfo[0], entity=self, roster=roster, **accInfo[1]), rosters[roster].iteritems())

        return result

    def getTeamLimits(self):
        return prb_getters.getPrebattleSettings().getTeamLimits(self.getPlayerTeam())

    def doAction(self, action = None):
        if self.getPlayerInfo().isReady():
            self.setPlayerState(SetPlayerStateCtx(False, waitingID='prebattle/player_not_ready'))
        else:
            self.setPlayerState(SetPlayerStateCtx(True, waitingID='prebattle/player_ready'))
        return True

    def doSelectAction(self, action):
        if action.actionName == PREBATTLE_ACTION_NAME.SPEC_BATTLES_LIST:
            g_eventDispatcher.showBattleSessionWindow()
            return SelectResult(True)
        return super(BattleSessionEntity, self).doSelectAction(action)

    def prb_onSettingUpdated(self, settingName):
        super(BattleSessionEntity, self).prb_onSettingUpdated(settingName)
        if settingName == PREBATTLE_SETTING_NAME.LIMITS:
            g_eventDispatcher.updateUI()

    def prb_onPlayerStateChanged(self, pID, roster):
        super(BattleSessionEntity, self).prb_onPlayerStateChanged(pID, roster)
        g_eventDispatcher.updateUI()

    def prb_onRosterReceived(self):
        super(BattleSessionEntity, self).prb_onRosterReceived()
        g_eventDispatcher.updateUI()

    def prb_onPlayerRosterChanged(self, pID, prevRoster, roster, actorID):
        super(BattleSessionEntity, self).prb_onPlayerRosterChanged(pID, prevRoster, roster, actorID)
        g_eventDispatcher.updateUI()

    def __handleCarouselInited(self, _):
        """
        Listener for carousel init event. It adds spec battles tab in
        carousel.
        """
        g_eventDispatcher.addSpecBattleToCarousel(self.getEntityType())
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\battle_session\legacy\entity.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:05 St�edn� Evropa (letn� �as)
