# 2017.05.04 15:25:34 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/server_events/events_dispatcher.py
import constants
from gui.shared import g_eventBus, events, event_dispatcher as shared_events, EVENT_BUS_SCOPE
from gui.server_events import awards
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS

def showPQSeasonAwardsWindow(questsType):
    g_eventBus.handleEvent(events.LoadViewEvent(VIEW_ALIAS.QUESTS_SEASON_AWARDS_WINDOW, ctx={'questsType': questsType}), EVENT_BUS_SCOPE.LOBBY)


def showTankwomanRecruitWindow(questID, isPremium, fnGroup, lnGroup, iGroup):
    g_eventBus.handleEvent(events.LoadViewEvent(VIEW_ALIAS.QUESTS_RECRUIT_WINDOW, ctx={'questID': questID,
     'isPremium': isPremium,
     'fnGroup': fnGroup,
     'lnGroup': lnGroup,
     'iGroupID': iGroup}), EVENT_BUS_SCOPE.LOBBY)


def showEventsWindow(eventID = None, eventType = None, doResetNavInfo = False):
    g_eventBus.handleEvent(events.LoadViewEvent(VIEW_ALIAS.EVENTS_WINDOW, ctx={'eventID': eventID,
     'eventType': eventType,
     'doResetNavInfo': doResetNavInfo}), EVENT_BUS_SCOPE.LOBBY)


def showTutorialTabInEventsWindow(eventID = ''):
    showEventsWindow(eventID, constants.EVENT_TYPE.TUTORIAL)


def showAchievementsAward(achievements):
    shared_events.showAwardWindow(awards.AchievementsAward(achievements))


def showTokenAward(potapovQuest, tokenID, tokensCount):
    shared_events.showAwardWindow(awards.TokenAward(potapovQuest, tokenID, tokensCount, showEventsWindow))


def showVehicleAward(vehicle):
    shared_events.showAwardWindow(awards.VehicleAward(vehicle))


def showMotiveAward(quest):
    shared_events.showAwardWindow(awards.MotiveQuestAward(quest, showEventsWindow))


def showTankwomanAward(questID, tankmanData):
    shared_events.showAwardWindow(awards.TankwomanAward(questID, tankmanData, showTankwomanRecruitWindow), isUniqueName=False)


def showMissionAward(quest, ctx):
    missionAward = awards.MissionAward(quest, ctx, showEventsWindow)
    if missionAward.getAwards():
        shared_events.showMissionAwardWindow(missionAward)


def showPersonalMissionAward(quest, ctx):
    shared_events.showMissionAwardWindow(awards.PersonalMissionAward(quest, ctx, showEventsWindow))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\server_events\events_dispatcher.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:34 St�edn� Evropa (letn� �as)
