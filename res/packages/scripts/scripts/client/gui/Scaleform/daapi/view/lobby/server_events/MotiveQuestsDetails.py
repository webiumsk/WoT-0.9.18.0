# 2017.05.04 15:23:55 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/server_events/MotiveQuestsDetails.py
from gui.Scaleform.daapi.view.lobby.server_events import events_helpers
from gui.Scaleform.daapi.view.meta.TutorialHangarQuestDetailsMeta import TutorialHangarQuestDetailsMeta
from gui.server_events import settings
from helpers import dependency
from skeletons.gui.server_events import IEventsCache

class MotiveQuestDetails(TutorialHangarQuestDetailsMeta):
    eventsCache = dependency.descriptor(IEventsCache)

    def getSortedTableData(self, tableData):
        return events_helpers.getSortedTableData(tableData)

    def requestQuestInfo(self, questID):
        svrEvents = self.eventsCache.getMotiveQuests()
        event = svrEvents.get(questID)
        settings.visitEventGUI(event)
        info = None
        if event is not None:
            info = events_helpers.getEventDetails(event, svrEvents)
        self.as_updateQuestInfoS(info)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\server_events\MotiveQuestsDetails.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:55 Støední Evropa (letní èas)
