# 2017.05.04 15:26:22 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/tooltips/wgm_currency.py
import BigWorld
from gui.shared.tooltips.common import DynamicBlocksTooltipData
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.utils.requesters import wgm_balance_info_requester
from gui.shared.tooltips import formatters
from gui.shared.formatters import text_styles
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared import g_itemsCache
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
_WAITING_FOR_DATA = ''
_UNKNOWN_VALUE = '-'

class _WGMCurrencyTooltip(DynamicBlocksTooltipData):

    def __init__(self, ctx):
        super(_WGMCurrencyTooltip, self).__init__(ctx, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI)
        self._setContentMargin(top=20, left=20, bottom=18, right=20)
        self._setMargins(afterBlock=0)
        self._setWidth(280)
        self.__requester = wgm_balance_info_requester.WGMBalanceInfoRequester()
        self.__data = None
        return

    def getWGMCurrencyValue(self, key):
        if not self.isWGMAvailable():
            return _UNKNOWN_VALUE
        elif self.__data is None:
            return _WAITING_FOR_DATA
        elif key in self.__data:
            return BigWorld.wg_getIntegralFormat(int(self.__data[key]))
        else:
            return _UNKNOWN_VALUE
            return

    def stopUpdates(self):
        self.__requester.clearCallbacks()
        super(_WGMCurrencyTooltip, self).stopUpdates()

    def changeVisibility(self, isVisible):
        super(_WGMCurrencyTooltip, self).changeVisibility(isVisible)
        if isVisible and self.isWGMAvailable():
            self.__requester.requestInfo(lambda result: self.__onDataResponse(result))

    @staticmethod
    def isWGMAvailable():
        return g_itemsCache.items.stats.mayConsumeWalletResources

    def __onDataResponse(self, data):
        if self.__data is None or self.__checkDiff(self.__data, data):
            self.__data = data
            self.updateData()
        return

    @staticmethod
    def __checkDiff(d1, d2):
        s1 = frozenset(d1.itervalues())
        s2 = frozenset(d2.itervalues())
        return s1 ^ s2


class WGMGoldCurrencyTooltip(_WGMCurrencyTooltip):

    def _packBlocks(self, *args, **kwargs):
        tooltipBlocks = super(WGMGoldCurrencyTooltip, self)._packBlocks(*args, **kwargs)
        currencyBlocks = list()
        currencyBlocks.append(formatters.packTitleDescBlock(text_styles.middleTitle(TOOLTIPS.HEADER_REFILL_HEADER), text_styles.main(TOOLTIPS.HEADER_REFILL_BODY), padding=formatters.packPadding(bottom=21)))
        currencyBlocks.append(formatters.packTextBlockData(text_styles.middleTitle(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_GOLDNAME), padding=formatters.packPadding(bottom=6)))
        currencyBlocks.append(formatters.packDashLineItemPriceBlockData(text_styles.main(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_PURCHASEDVALUE), self.__getGoldString(wgm_balance_info_requester.GOLD_PURCHASED), RES_ICONS.MAPS_ICONS_LIBRARY_GOLDICON_2, padding=formatters.packPadding(bottom=-1)))
        currencyBlocks.append(formatters.packDashLineItemPriceBlockData(text_styles.main(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_EARNEDVALUE), self.__getGoldString(wgm_balance_info_requester.GOLD_EARNED), RES_ICONS.MAPS_ICONS_LIBRARY_GOLDICON_2, padding=formatters.packPadding(bottom=16)))
        currencyBlocks.append(formatters.packDashLineItemPriceBlockData(text_styles.main(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_TOTALVALUE), text_styles.gold(self.__getGoldTotal()), RES_ICONS.MAPS_ICONS_LIBRARY_GOLDICON_2))
        tooltipBlocks.append(formatters.packBuildUpBlockData(currencyBlocks))
        return tooltipBlocks

    def __getGoldString(self, goldType):
        result = self.getWGMCurrencyValue(goldType)
        if result != _WAITING_FOR_DATA:
            return text_styles.gold(result)
        return result

    def __getGoldTotal(self):
        if self.isWGMAvailable():
            return BigWorld.wg_getIntegralFormat(g_itemsCache.items.stats.gold)
        return _UNKNOWN_VALUE


class WGMCreditsCurrencyTooltip(_WGMCurrencyTooltip):

    def _packBlocks(self, *args, **kwargs):
        tooltipBlocks = super(WGMCreditsCurrencyTooltip, self)._packBlocks(*args, **kwargs)
        currencyBlocks = list()
        currencyBlocks.append(formatters.packTitleDescBlock(text_styles.middleTitle(TOOLTIPS.HEADER_GOLD_EXCHANGE_HEADER), text_styles.main(TOOLTIPS.HEADER_GOLD_EXCHANGE_BODY), padding=formatters.packPadding(bottom=21)))
        currencyBlocks.append(formatters.packTextBlockData(text_styles.middleTitle(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_CREDITSNAME), padding=formatters.packPadding(bottom=6)))
        currencyBlocks.append(formatters.packDashLineItemPriceBlockData(text_styles.main(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_PURCHASEDVALUE), self.__getCreditsString(wgm_balance_info_requester.CREDITS_PURCHASED), RES_ICONS.MAPS_ICONS_LIBRARY_CREDITSICON_2, padding=formatters.packPadding(bottom=-1)))
        currencyBlocks.append(formatters.packDashLineItemPriceBlockData(text_styles.main(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_EARNEDVALUE), self.__getCreditsString(wgm_balance_info_requester.CREDITS_EARNED), RES_ICONS.MAPS_ICONS_LIBRARY_CREDITSICON_2, padding=formatters.packPadding(bottom=16)))
        currencyBlocks.append(formatters.packDashLineItemPriceBlockData(text_styles.main(TOOLTIPS.HANGAR_HEADER_WGMONEYTOOLTIP_TOTALVALUE), text_styles.credits(self.__getCreditsTotal()), RES_ICONS.MAPS_ICONS_LIBRARY_CREDITSICON_2))
        tooltipBlocks.append(formatters.packBuildUpBlockData(currencyBlocks))
        return tooltipBlocks

    def __getCreditsString(self, creditsType):
        result = self.getWGMCurrencyValue(creditsType)
        if result != _WAITING_FOR_DATA:
            return text_styles.credits(result)
        return result

    def __getCreditsTotal(self):
        if self.isWGMAvailable():
            return BigWorld.wg_getIntegralFormat(g_itemsCache.items.stats.credits)
        return _UNKNOWN_VALUE
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\tooltips\wgm_currency.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:22 St�edn� Evropa (letn� �as)
