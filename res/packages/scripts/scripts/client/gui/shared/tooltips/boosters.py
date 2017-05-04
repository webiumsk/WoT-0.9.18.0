# 2017.05.04 15:26:12 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/tooltips/boosters.py
from gui.Scaleform.daapi.view.lobby.server_events import events_helpers
from gui.shared.economics import getActionPrc
from gui.shared.tooltips.common import BlocksTooltipData, makePriceBlock, CURRENCY_SETTINGS
from gui.shared.tooltips import TOOLTIP_TYPE
from gui.shared.tooltips import formatters
from gui.shared.formatters import text_styles
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES
from helpers.i18n import makeString
from gui.Scaleform.locale.MENU import MENU
from gui.shared import g_itemsCache

class BoosterTooltipData(BlocksTooltipData):

    def __init__(self, context):
        super(BoosterTooltipData, self).__init__(context, TOOLTIP_TYPE.BOOSTER)
        self._setContentMargin(top=15, left=19, bottom=21, right=22)
        self._setMargins(afterBlock=14)
        self._setWidth(396)
        self.leftPadding = 20

    def _packBlocks(self, boosterID, *args, **kwargs):
        items = super(BoosterTooltipData, self)._packBlocks(*args, **kwargs)
        booster = self.context.buildItem(boosterID)
        statsFields = self.context.getStatsConfiguration(booster)
        items.append(formatters.packBuildUpBlockData([formatters.packTitleDescBlock(text_styles.highTitle(booster.fullUserName), desc=text_styles.main(booster.description)), formatters.packImageBlockData(img=booster.bigTooltipIcon, align=BLOCKS_TOOLTIP_TYPES.ALIGN_CENTER, width=180, height=180, padding={'top': -14,
          'bottom': -14})]))
        items.append(self.__packDueDate(booster))
        if statsFields.quests:
            questsResult = self.__getBoosterQuestNames(boosterID)
            if len(questsResult):
                items.append(self.__packAccessCondition(questsResult))
        if statsFields.buyPrice and booster.buyPrice:
            priceBlock = self.__getBoosterPrice(booster)
            items.append(formatters.packBuildUpBlockData(priceBlock))
        if statsFields.activeState and booster.inCooldown:
            items.append(self.__packActiveState(booster.getUsageLeftTimeStr()))
        return items

    def __packDueDate(self, booster):
        if booster.expiryTime:
            text = makeString(TOOLTIPS.BOOSTERSWINDOW_BOOSTER_DUEDATE_VALUE, date=booster.getExpiryDate())
        else:
            text = makeString(MENU.BOOSTERSWINDOW_BOOSTERSTABLERENDERER_UNDEFINETIME)
        return formatters.packBuildUpBlockData([formatters.packTitleDescBlock(text_styles.middleTitle(TOOLTIPS.BOOSTERSWINDOW_BOOSTER_DUEDATE_TITLE), text_styles.standard(text))])

    def __packAccessCondition(self, questsResult):
        qNames = '"%s"' % ', '.join(questsResult)
        return formatters.packBuildUpBlockData([formatters.packTitleDescBlock(text_styles.middleTitle(TOOLTIPS.BOOSTERSWINDOW_BOOSTER_GETCONDITION_TITLE), text_styles.standard(makeString(TOOLTIPS.BOOSTERSWINDOW_BOOSTER_GETCONDITION_VALUE, questName=text_styles.neutral(qNames))))])

    def __packActiveState(self, time):
        state = text_styles.main(makeString(TOOLTIPS.BOOSTERSWINDOW_BOOSTER_ACTIVE_VALUE, time=text_styles.stats(time)))
        return formatters.packBuildUpBlockData([formatters.packAlignedTextBlockData(text_styles.statInfo(TOOLTIPS.BOOSTERSWINDOW_BOOSTER_ACTIVE_TITLE), BLOCKS_TOOLTIP_TYPES.ALIGN_CENTER, padding={'bottom': 4}), formatters.packAlignedTextBlockData(state, BLOCKS_TOOLTIP_TYPES.ALIGN_CENTER)])

    def __getBoosterQuestNames(self, boosterID):
        questsResult = set()
        quests = events_helpers.getBoosterQuests()
        for q in quests.itervalues():
            bonuses = q.getBonuses('goodies')
            for b in bonuses:
                boosters = b.getBoosters()
                for qBooster, count in boosters.iteritems():
                    if boosterID == qBooster.boosterID:
                        questsResult.add(q.getUserName())

        for chapter, boosters in events_helpers.getTutorialQuestsBoosters().iteritems():
            for booster, count in boosters:
                if boosterID == booster.boosterID:
                    questsResult.add(chapter.getTitle())

        return questsResult

    def __getBoosterPrice(self, booster):
        block = []
        money = g_itemsCache.items.stats.money
        if booster.buyPrice:
            price = booster.buyPrice
            defPrice = booster.defaultPrice
            need = price - money
            need = need.toNonNegative()
            leftPadding = 92
            if price.credits > 0:
                creditsActionPercent = getActionPrc(price.credits, defPrice.credits)
                block.append(makePriceBlock(price.credits, CURRENCY_SETTINGS.BUY_CREDITS_PRICE, need.credits if need.credits > 0 else None, defPrice.credits if defPrice.credits > 0 else None, creditsActionPercent, leftPadding=leftPadding))
            if price.gold > 0:
                goldActionPercent = getActionPrc(price.gold, defPrice.gold)
                if price.credits > 0:
                    block.append(formatters.packTextBlockData(text=text_styles.standard(TOOLTIPS.VEHICLE_TEXTDELIMITER_OR), padding=formatters.packPadding(left=(101 if goldActionPercent > 0 else 81) + self.leftPadding)))
                block.append(makePriceBlock(price.gold, CURRENCY_SETTINGS.BUY_GOLD_PRICE, need.gold if need.gold > 0 else None, defPrice.gold if defPrice.gold > 0 else None, goldActionPercent, leftPadding=leftPadding))
        return block
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\tooltips\boosters.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:12 St�edn� Evropa (letn� �as)
