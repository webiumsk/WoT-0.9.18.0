# 2017.05.04 15:28:01 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/quests/settings.py
from gui.Scaleform.framework import GroupedViewSettings, ViewTypes, ScopeTemplates
from tutorial.gui.Scaleform.quests import pop_ups

class TUTORIAL_VIEW_ALIAS(object):
    TUTORIAL_QUEST_AWARD_WINDOW = 'tQuestAwardWindow'


QUESTS_VIEW_SETTINGS = (GroupedViewSettings(TUTORIAL_VIEW_ALIAS.TUTORIAL_QUEST_AWARD_WINDOW, pop_ups.TutorialQuestAwardWindow, 'awardWindow.swf', ViewTypes.WINDOW, 'tQuestAwardGroup', None, ScopeTemplates.DEFAULT_SCOPE),)
WINDOW_ALIAS_MAP = {'awardWindow': TUTORIAL_VIEW_ALIAS.TUTORIAL_QUEST_AWARD_WINDOW}
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\gui\Scaleform\quests\settings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:01 Støední Evropa (letní èas)
