# 2017.05.04 15:23:53 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/recruitWindow/QuestsRecruitWindow.py
import nations
from gui import SystemMessages
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.QuestRecruitWindowMeta import QuestRecruitWindowMeta
from gui.shared.gui_items import Tankman
from gui.shared.gui_items.processors.quests import PotapovQuestsGetTankwomanReward
from gui.shared.utils import decorators
from helpers import dependency
from items import tankmen
from skeletons.gui.server_events import IEventsCache

class QuestsRecruitWindow(QuestRecruitWindowMeta):
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, ctx = None):
        super(QuestsRecruitWindow, self).__init__()
        self.__currentSelectedNationID = None
        raise len({'isPremium',
         'fnGroup',
         'lnGroup',
         'iGroupID',
         'questID'} - set(ctx.keys())) == 0 or AssertionError
        self.__questID = ctx['questID']
        self.__isPremium = ctx['isPremium']
        self.__fnGroup = ctx['fnGroup']
        self.__lnGroup = ctx['lnGroup']
        self.__iGroupID = ctx['iGroupID']
        self.__freeXpValue = ctx.get('freeXP', 0)
        return

    def onWindowClose(self):
        self.destroy()

    @decorators.process('updating')
    def onApply(self, data):
        potapovQuest = self.eventsCache.potapov.getQuests().get(self.__questID)
        result = yield PotapovQuestsGetTankwomanReward(potapovQuest, int(data.nation), int(data.vehicle), data.tankmanRole).request()
        if len(result.userMsg):
            SystemMessages.pushMessage(result.userMsg, type=result.sysMsgType)
        if result.success:
            self.destroy()

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(QuestsRecruitWindow, self)._onRegisterFlashComponent(viewPy, alias)
        if alias == VIEW_ALIAS.RECRUIT_PARAMS:
            viewPy.onDataChange += self.__paramsChangeHandler
            viewPy.setNationsData(showEmptyRow=False)

    def _onUnregisterFlashComponent(self, viewPy, alias):
        super(QuestsRecruitWindow, self)._onUnregisterFlashComponent(viewPy, alias)
        viewPy.onDataChange -= self.__paramsChangeHandler

    def __paramsChangeHandler(self, selectedNationID, selectedVehClass, selectedVehicle, selectedTmanRole):
        selectedNationID = int(selectedNationID)
        nationName = nations.NAMES[selectedNationID]
        if self.__currentSelectedNationID != selectedNationID:
            firstNameID, lastNameID, iconID = self.eventsCache.potapov.getNextTankwomanIDs(selectedNationID, self.__isPremium, int(self.__fnGroup), int(self.__lnGroup), int(self.__iGroupID))
            rankID = Tankman.calculateRankID(tankmen.MAX_SKILL_LEVEL, self.__freeXpValue)
            self.as_setInitDataS({'name': Tankman.getFullUserName(selectedNationID, firstNameID, lastNameID),
             'nation': nationName,
             'rank': Tankman.getRankUserName(selectedNationID, rankID),
             'vehicle': '',
             'faceIcon': Tankman.getBigIconPath(selectedNationID, iconID),
             'rankIcon': Tankman.getRankBigIconPath(selectedNationID, rankID)})
        self.__currentSelectedNationID = selectedNationID
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\recruitWindow\QuestsRecruitWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:53 St�edn� Evropa (letn� �as)
