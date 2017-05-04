# 2017.05.04 15:23:58 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/server_events/TutorialQuestsTab.py
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.server_events.QuestsCurrentTab import QuestsCurrentTab
from gui.Scaleform.daapi.view.lobby.server_events import events_helpers
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.server_events import formatters
from gui.server_events.formatters import PROGRESS_BAR_TYPE
from gui.shared.ItemsCache import g_itemsCache
from gui import SystemMessages
from helpers import dependency
from shared_utils import findFirst
from skeletons.gui.server_events import IEventsCache
NO_PROGRESS_COUNT = -1
_EVENT_STATUS = events_helpers.EVENT_STATUS

class TutorialQuestsTab(QuestsCurrentTab):
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self):
        super(TutorialQuestsTab, self).__init__()
        self.__questsDescriptor = events_helpers.getTutorialEventsDescriptor()

    def _populate(self):
        super(TutorialQuestsTab, self)._populate()
        g_clientUpdateManager.addCallbacks({'stats.tutorialsCompleted': self.__onEventsUpdated,
         'stats.dossier': self.__onEventsUpdated})
        self._invalidateEventsData()

    def _dispose(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__questsDescriptor = None
        super(TutorialQuestsTab, self)._dispose()
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(TutorialQuestsTab, self)._onRegisterFlashComponent(viewPy, alias)
        if alias == QUESTS_ALIASES.TUTORIAL_HANGAR_QUEST_DETAILS_PY_ALIAS:
            self.components.get(alias).setQuestsDescriptor(self.__questsDescriptor)

    def _getDefaultQuestID(self):
        return self._navInfo.tutorial.questID

    def _selectQuest(self, questID):
        motiveQuests = self.eventsCache.getMotiveQuests(filterFunc=self._filterFunc)
        if questID in motiveQuests or self.__questsDescriptor is not None and self.__questsDescriptor.getChapter(questID) is not None:
            return self.as_setSelectedQuestS(questID)
        else:
            if questID in self.eventsCache.getMotiveQuests(filterFunc=lambda q: q.isCompleted()):
                sortedQuests = sorted(motiveQuests.values(), key=lambda q: q.getPriority())
                nextQuest = findFirst(None, sortedQuests)
                if nextQuest:
                    return self.as_setSelectedQuestS(nextQuest.getID())
            SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.QUESTS_NOQUESTSWITHGIVENID)
            return

    def _invalidateEventsData(self):
        result = []
        if self.__questsDescriptor is not None:
            completed = g_itemsCache.items.stats.tutorialsCompleted
            for chapter in self.__questsDescriptor:
                chapterStatus = chapter.getChapterStatus(self.__questsDescriptor, completed)
                if chapterStatus != _EVENT_STATUS.NOT_AVAILABLE:
                    qProgCur, qProgTot, progressBarType = self.__getProgressValues(chapter)
                    result.append({'questID': chapter.getID(),
                     'isNew': False,
                     'status': chapterStatus,
                     'description': chapter.getTitle(),
                     'isSelectable': True,
                     'rendererType': QUESTS_ALIASES.RENDERER_TYPE_QUEST,
                     'tooltip': TOOLTIPS.QUESTS_RENDERER_LABEL,
                     'tasksCount': NO_PROGRESS_COUNT,
                     'maxProgrVal': qProgTot,
                     'currentProgrVal': qProgCur,
                     'progrBarType': progressBarType,
                     'detailsLinkage': QUESTS_ALIASES.TUTORIAL_HANGAR_QUEST_DETAILS_LINKAGE,
                     'detailsPyAlias': QUESTS_ALIASES.TUTORIAL_HANGAR_QUEST_DETAILS_PY_ALIAS})

        svrEvents = self._applyFilters(self.eventsCache.getMotiveQuests().values())
        if len(svrEvents):
            result.append(formatters.packGroupBlock(QUESTS.QUESTS_TITLE_MANEUVERSQUESTS))
            for e in svrEvents:
                infoData = events_helpers.getEventInfo(e, svrEvents)
                infoData.update({'detailsLinkage': QUESTS_ALIASES.TUTORIAL_HANGAR_MOTIVE_QUEST_DETAILS_LINKAGE,
                 'detailsPyAlias': QUESTS_ALIASES.TUTORIAL_HANGAR_MOTIVE_QUEST_DETAILS_PY_ALIAS})
                result.append(infoData)

        self.as_setQuestsDataS({'quests': result,
         'totalTasks': len(svrEvents)})
        return

    def _filterFunc(self, event):
        return not event.isCompleted() and event.isAvailable()[0]

    def __onEventsUpdated(self, *args):
        self._invalidateEventsData()

    def __getProgressValues(self, chapter):
        progrCondition = chapter.getProgressCondition()
        if progrCondition.getID() == 'vehicleBattlesCount':
            vehicleCD = progrCondition.getValues().get('vehicle')
            battlesLimit = progrCondition.getValues().get('limit', NO_PROGRESS_COUNT)
            progressBarType = progrCondition.getValues().get('progressBarType', PROGRESS_BAR_TYPE.NONE)
            vehicleDossier = g_itemsCache.items.getVehicleDossier(vehicleCD)
            return (vehicleDossier.getTotalStats().getBattlesCount(), battlesLimit, progressBarType)
        return (NO_PROGRESS_COUNT, NO_PROGRESS_COUNT, PROGRESS_BAR_TYPE.NONE)

    def _updateFilterView(self):
        pass
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\server_events\TutorialQuestsTab.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:58 St�edn� Evropa (letn� �as)
