# 2017.05.04 15:22:56 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/SkillDropWindow.py
import cPickle as pickle
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE
from items import tankmen
from gui import SystemMessages
from gui.shared.utils import decorators
from gui.shared.formatters import text_styles
from gui.shared.gui_items.serializers import packTankman
from gui.shared.gui_items.Tankman import Tankman
from gui.shared.gui_items.processors.tankman import TankmanDropSkills
from gui.shared.money import Money
from gui.shared.tooltips.formatters import packActionTooltipData
from gui.Scaleform.daapi.view.meta.SkillDropMeta import SkillDropMeta
from gui.shared import events, g_itemsCache
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.locale.MENU import MENU
from helpers import i18n

class SkillDropWindow(SkillDropMeta):

    def __init__(self, ctx = None):
        super(SkillDropWindow, self).__init__()
        self.tmanInvID = ctx.get('tankmanID')

    def __setData(self, *args):
        items = g_itemsCache.items
        tankman = items.getTankman(self.tmanInvID)
        if tankman is None:
            self.onWindowClose()
            return
        else:
            dropSkillsCost = []
            for k in sorted(items.shop.dropSkillsCost.keys()):
                skillCost = items.shop.dropSkillsCost[k]
                defaultSkillCots = items.shop.defaults.dropSkillsCost[k]
                price = Money(**skillCost)
                defaultPrice = Money(**defaultSkillCots)
                action = None
                if price != defaultPrice:
                    key = '{}DropSkillsCost'.format(price.getCurrency(byWeight=True))
                    action = packActionTooltipData(ACTION_TOOLTIPS_TYPE.ECONOMICS, key, True, price, defaultPrice)
                skillCost['action'] = action
                dropSkillsCost.append(skillCost)

            skills_count = list(tankmen.ACTIVE_SKILLS)
            availableSkillsCount = len(skills_count) - len(tankman.skills)
            hasNewSkills = tankman.roleLevel == tankmen.MAX_SKILL_LEVEL and availableSkillsCount and (tankman.descriptor.lastSkillLevel == tankmen.MAX_SKILL_LEVEL or not len(tankman.skills))
            self.as_setDataS({'money': items.stats.money,
             'tankman': packTankman(tankman, isCountPermanentSkills=False),
             'dropSkillsCost': dropSkillsCost,
             'hasNewSkills': hasNewSkills,
             'newSkills': tankman.newSkillCount,
             'defaultSavingMode': 0,
             'texts': self.__getTexts()})
            return

    def __getTexts(self):
        ms = i18n.makeString
        percentText = text_styles.neutral(ms(MENU.SKILLDROPWINDOW_FREEDROPPERCENT))
        freeDropText = text_styles.main(ms(MENU.SKILLDROPWINDOW_FREEDROPLABEL, percent=percentText))
        return {'freeDrop': freeDropText}

    def _populate(self):
        super(SkillDropWindow, self)._populate()
        self.__setData()
        g_itemsCache.onSyncCompleted += self.__setData
        g_clientUpdateManager.addCallbacks({'inventory.8.compDescr': self.onTankmanChanged,
         'stats.credits': self.onCreditsChange,
         'stats.gold': self.onGoldChange,
         'cache.mayConsumeWalletResources': self.onGoldChange})

    def _dispose(self):
        g_itemsCache.onSyncCompleted -= self.__setData
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(SkillDropWindow, self)._dispose()

    def onTankmanChanged(self, data):
        if self.tmanInvID in data:
            if data[self.tmanInvID] is None:
                self.onWindowClose()
                return
            self.__setData()
        return

    def onCreditsChange(self, credits):
        self.as_setCreditsS(credits)

    def onGoldChange(self, gold):
        self.as_setGoldS(g_itemsCache.items.stats.gold)

    def onWindowClose(self):
        self.destroy()

    def calcDropSkillsParams(self, tmanCompDescrPickle, xpReuseFraction):
        """
        Recalculates tankman skills by given skills reuse fraction
        
        @param tmanCompDescr: tankman string compact descriptor
        @param xpReuseFraction: tankman experience reuse fraction
        @return: (new skills count, last new skill level)
        """
        tmanCompDescr = pickle.loads(tmanCompDescrPickle)
        tmanDescr = tankmen.TankmanDescr(tmanCompDescr)
        tmanDescr.dropSkills(xpReuseFraction)
        tankman = Tankman(tmanDescr.makeCompactDescr())
        return (tankman.roleLevel,) + tankman.newSkillCount

    @decorators.process('deleting')
    def dropSkills(self, dropSkillCostIdx):
        """
        Drops all tankman skill using @dropSkillCostIdx modificator
        @param dropSkillCostIdx: tankman experience modificator index
        """
        tankman = g_itemsCache.items.getTankman(self.tmanInvID)
        proc = TankmanDropSkills(tankman, dropSkillCostIdx)
        result = yield proc.request()
        if len(result.userMsg):
            SystemMessages.pushMessage(result.userMsg, type=result.sysMsgType)
        if result.success:
            self.onWindowClose()
            self.fireEvent(events.SkillDropEvent(events.SkillDropEvent.SKILL_DROPPED_SUCCESSFULLY))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\SkillDropWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:56 St�edn� Evropa (letn� �as)
