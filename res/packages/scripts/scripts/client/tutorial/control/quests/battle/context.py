# 2017.05.04 15:27:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/control/quests/battle/context.py
from account_helpers.AccountSettings import AccountSettings
from account_helpers.settings_core.settings_constants import TUTORIAL
from constants import ARENA_GUI_TYPE, IS_DEVELOPMENT
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from tutorial.control import context

class BattleQuestsStartReqs(context.StartReqs):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def isEnabled(self):
        areSettingsInited = self.__areSettingsInited()
        arenaGuiTypes = [ARENA_GUI_TYPE.RANDOM, ARENA_GUI_TYPE.SANDBOX, ARENA_GUI_TYPE.RATED_SANDBOX]
        if IS_DEVELOPMENT:
            arenaGuiTypes.append(ARENA_GUI_TYPE.TRAINING)
        return self.sessionProvider.arenaVisitor.getArenaGuiType() in arenaGuiTypes and areSettingsInited

    def __areSettingsInited(self):
        validateSettings = (TUTORIAL.FIRE_EXTINGUISHER_INSTALLED, TUTORIAL.MEDKIT_INSTALLED, TUTORIAL.REPAIRKIT_INSTALLED)
        getter = AccountSettings.getSettings
        for setting in validateSettings:
            if getter(setting):
                return True

        return False

    def prepare(self, ctx):
        pass

    def process(self, descriptor, ctx):
        return True


class FakeBonusesRequester(context.BonusesRequester):

    def request(self, chapterID = None):
        pass
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\control\quests\battle\context.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:51 Støední Evropa (letní èas)
