# 2017.05.04 15:21:10 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/battle_control/controllers/avatar_stats_ctrl.py
import Event
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController

class AvatarStatsController(IBattleController):

    def __init__(self):
        super(AvatarStatsController, self).__init__()
        self.__stats = {}
        self.__eManager = Event.EventManager()
        self.onUpdated = Event.Event(self.__eManager)

    def getControllerID(self):
        return BATTLE_CTRL_ID.AVATAR_PRIVATE_STATS

    def startControl(self):
        pass

    def stopControl(self):
        self.__eManager.clear()
        self.__eManager = None
        return

    def getStats(self):
        return self.__stats

    def update(self, stats):
        self.__stats = stats
        self.onUpdated(stats)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_control\controllers\avatar_stats_ctrl.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:10 Støední Evropa (letní èas)
