# 2017.05.04 15:21:19 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/battle_results/service.py
from adisp import async, process
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_WARNING
from gui import SystemMessages
from gui.LobbyContext import g_lobbyContext
from gui.Scaleform.locale.BATTLE_RESULTS import BATTLE_RESULTS
from gui.battle_results import composer
from gui.battle_results import emblems
from gui.battle_results import context
from gui.battle_results import reusable
from gui.battle_results import stored_sorting
from gui.battle_results.settings import PREMIUM_STATE
from gui.shared import event_dispatcher
from gui.shared import g_eventBus, events
from gui.shared import g_itemsCache
from gui.shared.gui_items.processors.common import BattleResultsGetter
from helpers import dependency
from skeletons.gui.battle_results import IBattleResultsService
from skeletons.gui.battle_session import IBattleSessionProvider

class BattleResultsService(IBattleResultsService):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __slots__ = ('__composers', '__buy')

    def __init__(self):
        super(BattleResultsService, self).__init__()
        self.__composers = {}
        self.__buy = set()

    def init(self):
        g_eventBus.addListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__handleLobbyViewLoaded)
        g_eventBus.addListener(events.LobbySimpleEvent.PREMIUM_BOUGHT, self.__onPremiumBought)

    def fini(self):
        g_eventBus.removeListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__handleLobbyViewLoaded)
        g_eventBus.removeListener(events.LobbySimpleEvent.PREMIUM_BOUGHT, self.__onPremiumBought)
        self.clear()

    def clear(self):
        while self.__composers:
            _, item = self.__composers.popitem()
            item.clear()

    @async
    @process
    def requestResults(self, ctx, callback = None):
        arenaUniqueID = ctx.getArenaUniqueID()
        if ctx.needToShowImmediately():
            event_dispatcher.showBattleResultsWindow(arenaUniqueID)
        if not ctx.resetCache() and arenaUniqueID in self.__composers:
            isSuccess = True

            def dummy(callback = None):
                if callback is not None:
                    callback(None)
                return

            yield dummy
            self.__notifyBattleResultsPosted(arenaUniqueID, needToShowUI=ctx.needToShowIfPosted())
        else:
            results = yield BattleResultsGetter(arenaUniqueID).request()
            isSuccess = results.success
            if not results.success or not self.postResult(results.auxData, ctx.needToShowIfPosted()):
                self.__composers.pop(arenaUniqueID, None)
                event_dispatcher.hideBattleResults()
        if callback is not None:
            callback(isSuccess)
        return

    @async
    def requestEmblem(self, ctx, callback = None):
        fetcher = emblems.createFetcher(ctx)
        if fetcher is not None:
            fetcher.fetch(callback)
        else:
            LOG_WARNING('Icon fetcher is not found', ctx)
            if callback is not None:
                callback(None)
        return

    def postResult(self, result, needToShowUI = True):
        reusableInfo = reusable.createReusableInfo(result)
        if reusableInfo is None:
            SystemMessages.pushI18nMessage(BATTLE_RESULTS.NODATA, type=SystemMessages.SM_TYPE.Warning)
            return False
        else:
            arenaUniqueID = reusableInfo.arenaUniqueID
            reusableInfo.premiumState = self.__makePremiumState(arenaUniqueID)
            reusableInfo.clientIndex = g_lobbyContext.getClientIDByArenaUniqueID(arenaUniqueID)
            created = composer.createComposer(reusableInfo)
            created.setResults(result, reusableInfo)
            self.__composers[arenaUniqueID] = created
            self.__notifyBattleResultsPosted(arenaUniqueID, needToShowUI=needToShowUI)
            return True

    def areResultsPosted(self, arenaUniqueID):
        return arenaUniqueID in self.__composers

    def getResultsVO(self, arenaUniqueID):
        if arenaUniqueID in self.__composers:
            found = self.__composers[arenaUniqueID]
            vo = found.getVO()
        else:
            vo = None
        return vo

    def popResultsAnimation(self, arenaUniqueID):
        if arenaUniqueID in self.__composers:
            found = self.__composers[arenaUniqueID]
            vo = found.popAnimation()
        else:
            vo = None
        return vo

    def saveStatsSorting(self, bonusType, iconType, sortDirection):
        stored_sorting.writeStatsSorting(bonusType, iconType, sortDirection)

    @process
    def __showResults(self, ctx):
        yield self.requestResults(ctx)

    @staticmethod
    def __notifyBattleResultsPosted(arenaUniqueID, needToShowUI = False):
        if needToShowUI:
            event_dispatcher.showBattleResultsWindow(arenaUniqueID)
        event_dispatcher.notifyBattleResultsPosted(arenaUniqueID)

    def __handleLobbyViewLoaded(self, _):
        battleCtx = self.sessionProvider.getCtx()
        arenaUniqueID = battleCtx.lastArenaUniqueID
        if arenaUniqueID:
            try:
                self.__showResults(context.RequestResultsContext(arenaUniqueID))
            except:
                LOG_CURRENT_EXCEPTION()

            battleCtx.lastArenaUniqueID = None
        return

    def __onPremiumBought(self, event):
        ctx = event.ctx
        raise 'arenaUniqueID' in ctx or AssertionError
        arenaUniqueID = event.ctx['arenaUniqueID']
        if not 'becomePremium' in ctx:
            raise AssertionError
            becomePremium = event.ctx['becomePremium']
            becomePremium and arenaUniqueID and self.__buy.add(arenaUniqueID)
            event_dispatcher.hideBattleResults()
            self.__showResults(context.RequestResultsContext(arenaUniqueID, resetCache=True))

    def __makePremiumState(self, arenaUniqueID):
        state = PREMIUM_STATE.NONE
        settings = g_lobbyContext.getServerSettings()
        if settings is not None and settings.isPremiumInPostBattleEnabled():
            state |= PREMIUM_STATE.BUY_ENABLED
        if g_itemsCache.items.stats.isPremium:
            state |= PREMIUM_STATE.HAS_ALREADY
        if arenaUniqueID in self.__buy:
            state |= PREMIUM_STATE.BOUGHT
        return state
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_results\service.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:19 St�edn� Evropa (letn� �as)
