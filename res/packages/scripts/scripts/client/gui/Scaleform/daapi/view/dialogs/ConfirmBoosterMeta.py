# 2017.05.04 15:22:47 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/ConfirmBoosterMeta.py
import math
from Event import EventManager, Event
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta
from gui.Scaleform.framework import ScopeTemplates
from gui.goodies.goodies_cache import g_goodiesCache
from gui.shared import events
from gui.shared.gui_items.processors.goodies import BoosterBuyer
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.shared.utils.decorators import process
from gui.shared.money import Currency
from gui.shared.tooltips.formatters import packActionTooltipData
from gui import SystemMessages
MAX_BOOSTERS_FOR_OPERATION = 1000000

class BuyBoosterMeta(I18nConfirmDialogMeta):

    def __init__(self, boosterID, balance):
        super(BuyBoosterMeta, self).__init__('buyConfirmation', scope=ScopeTemplates.LOBBY_SUB_SCOPE)
        self.__booster = g_goodiesCache.getBooster(boosterID)
        self.__balance = balance
        self._eManager = EventManager()
        self.onInvalidate = Event(self._eManager)
        g_clientUpdateManager.addCallbacks({'stats': self.__onStatsChanged})

    def getEventType(self):
        return events.ShowDialogEvent.SHOW_CONFIRM_BOOSTER

    def getBoosterID(self):
        return self.__booster.boosterID

    def getBooster(self):
        return self.__booster

    def destroy(self):
        self.__booster = None
        self.__balance = None
        self._eManager.clear()
        g_clientUpdateManager.removeObjectCallbacks(self)
        return

    def getMaxAvailableItemsCount(self):
        return (self.__getMaxCount(Currency.CREDITS), self.__getMaxCount(Currency.GOLD))

    def getActionVO(self):
        buyPrice = self.__booster.buyPrice
        defaultPrice = self.__booster.defaultPrice
        if buyPrice != defaultPrice:
            return packActionTooltipData(ACTION_TOOLTIPS_TYPE.BOOSTER, str(self.__booster.boosterID), True, buyPrice, defaultPrice)
        else:
            return None

    def getCurrency(self):
        return self.__booster.getBuyPriceCurrency()

    def getPrice(self):
        return self.__booster.buyPrice

    @process('buyItem')
    def submit(self, count, currency):
        result = yield BoosterBuyer(self.__booster, count, currency == Currency.GOLD).request()
        if len(result.userMsg):
            SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)

    def __onStatsChanged(self, stats):
        if 'credits' in stats:
            self.__balance = self.__balance.replace(Currency.CREDITS, stats['credits'])
            self.onInvalidate()
        if 'gold' in stats:
            self.__balance = self.__balance.replace(Currency.GOLD, stats['gold'])
            self.onInvalidate()

    def __getMaxCount(self, currency):
        result = 0
        boosterPrice = self.__booster.buyPrice
        if boosterPrice.get(currency) > 0:
            result = math.floor(self.__balance.get(currency) / boosterPrice.get(currency))
        return min(result, MAX_BOOSTERS_FOR_OPERATION)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\dialogs\ConfirmBoosterMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:48 St�edn� Evropa (letn� �as)
