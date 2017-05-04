# 2017.05.04 15:21:12 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/battle_control/controllers/flag_nots_ctrl.py
import weakref
from CTFManager import g_ctfManager
from gui.battle_control import avatar_getter
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.view_components import IViewComponentsController
CAPTURE_SOUND_ID = 'take_flag'
DELIVERED_SOUND_ID = 'deliver_flag'
CONSUMED_SOUND_ID = 'consumed_flag'
ENEMY_CAPTURE_SOUND_ID = 'enemy_take_flag'
ALLY_CAPTURE_SOUND_ID = 'ally_take_flag'
ALLY_DROPPED_SOUND_ID = 'ally_drop_flag'
ALLY_DELIVERED_SOUND_ID = 'ally_deliver_flag'

class IFlagNotificationView(object):

    def showFlagCaptured(self):
        raise NotImplementedError

    def showFlagDelivered(self):
        raise NotImplementedError

    def showFlagAbsorbed(self):
        raise NotImplementedError

    def showFlagDropped(self):
        raise NotImplementedError


class NotificationsController(IViewComponentsController):

    def __init__(self, setup):
        super(NotificationsController, self).__init__()
        self.__ui = None
        self.__arenaDP = weakref.proxy(setup.arenaDP)
        self.__arenaVisitor = weakref.proxy(setup.arenaVisitor)
        self.__soundNotifications = None
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.FLAG_NOTS

    def startControl(self):
        nots = avatar_getter.getSoundNotifications()
        if nots is not None:
            self.__soundNotifications = weakref.proxy(nots)
        self.__setPlayerFlagBearerIfNeed()
        g_ctfManager.onFlagCapturedByVehicle += self.__onFlagCapturedByVehicle
        g_ctfManager.onFlagAbsorbed += self.__onFlagAbsorbed
        g_ctfManager.onFlagDroppedToGround += self.__onFlagDroppedToGround
        g_ctfManager.onFlagRemoved += self.__onFlagRemoved
        return

    def stopControl(self):
        g_ctfManager.onFlagCapturedByVehicle -= self.__onFlagCapturedByVehicle
        g_ctfManager.onFlagAbsorbed -= self.__onFlagAbsorbed
        g_ctfManager.onFlagDroppedToGround -= self.__onFlagDroppedToGround
        g_ctfManager.onFlagRemoved -= self.__onFlagRemoved
        self.clearViewComponents()
        self.__arenaDP = None
        self.__arenaVisitor = None
        self.__soundNotifications = None
        return

    def setViewComponents(self, *components):
        self.__ui = components[0]
        self.__setPlayerFlagBearerIfNeed()

    def clearViewComponents(self):
        self.__ui = None
        return

    def __setPlayerFlagBearerIfNeed(self):
        playerVehicleID = self.__arenaDP.getPlayerVehicleID()
        if self.__ui is not None and g_ctfManager.getVehicleCarriedFlagID(playerVehicleID) is not None:
            self.__ui.showFlagCaptured()
        return

    def __onFlagCapturedByVehicle(self, flagID, flagTeam, vehicleID):
        vehInfo = self.__arenaDP.getVehicleInfo(vehicleID)
        playerVehicleID = self.__arenaDP.getPlayerVehicleID()
        if vehicleID == playerVehicleID:
            self.__playSound(CAPTURE_SOUND_ID)
            if self.__ui is not None:
                self.__ui.showFlagCaptured()
        elif vehInfo.team == self.__arenaDP.getNumberOfTeam():
            self.__playSound(ALLY_CAPTURE_SOUND_ID)
        else:
            self.__playSound(ENEMY_CAPTURE_SOUND_ID)
        return

    def __onFlagAbsorbed(self, flagID, flagTeam, vehicleID, respawnTime):
        vehInfo = self.__arenaDP.getVehicleInfo(vehicleID)
        playerVehicleID = self.__arenaDP.getPlayerVehicleID()
        if vehicleID == playerVehicleID:
            if self.__arenaVisitor.isSoloTeam(self.__arenaDP.getNumberOfTeam()):
                self.__playSound(CONSUMED_SOUND_ID)
                if self.__ui is not None:
                    self.__ui.showFlagAbsorbed()
            else:
                self.__playSound(DELIVERED_SOUND_ID)
                if self.__ui is not None:
                    self.__ui.showFlagDelivered()
        elif vehInfo.team == self.__arenaDP.getNumberOfTeam():
            self.__playSound(ALLY_DELIVERED_SOUND_ID)
        return

    def __onFlagDroppedToGround(self, flagID, flagTeam, loserVehicleID, flagPos, respawnTime):
        vehInfo = self.__arenaDP.getVehicleInfo(loserVehicleID)
        playerVehicleID = self.__arenaDP.getPlayerVehicleID()
        if loserVehicleID == playerVehicleID:
            if self.__ui is not None:
                self.__ui.showFlagDropped()
        elif vehInfo.team == self.__arenaDP.getNumberOfTeam():
            self.__playSound(ALLY_DROPPED_SOUND_ID)
        return

    def __onFlagRemoved(self, flagID, flagTeam, vehicleID):
        playerVehicleID = self.__arenaDP.getPlayerVehicleID()
        if self.__ui is not None and vehicleID == playerVehicleID:
            self.__ui.showFlagDropped()
        return

    def __playSound(self, soundID):
        if self.__soundNotifications is not None:
            self.__playSound(soundID)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_control\controllers\flag_nots_ctrl.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:12 St�edn� Evropa (letn� �as)
