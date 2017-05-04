# 2017.05.04 15:21:43 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/game_control/RentalsController.py
from operator import itemgetter
import BigWorld
import Event
from gui.shared.ItemsCache import g_itemsCache
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers import time_utils
from skeletons.gui.game_control import IRentalsController

class RentalsController(IRentalsController):

    def __init__(self):
        super(RentalsController, self).__init__()
        self.onRentChangeNotify = Event.Event()
        self.__rentNotifyTimeCallback = None
        self.__vehiclesForUpdate = []
        return

    def fini(self):
        self._stop()
        super(RentalsController, self).fini()

    def onLobbyInited(self, event):
        g_itemsCache.onSyncCompleted += self._update
        if self.__rentNotifyTimeCallback is None:
            self.__startRentTimeNotifyCallback()
        return

    def onAvatarBecomePlayer(self):
        self._stop()

    def onDisconnected(self):
        self._stop()

    def _stop(self):
        self.__clearRentTimeNotifyCallback()
        self.__vehiclesForUpdate = None
        self.onRentChangeNotify.clear()
        g_itemsCache.onSyncCompleted -= self._update
        return

    def _update(self, *args):
        self.__clearRentTimeNotifyCallback()
        self.__startRentTimeNotifyCallback()

    def __startRentTimeNotifyCallback(self):
        self.__vehiclesForUpdate = []
        rentedVehicles = g_itemsCache.items.getVehicles(REQ_CRITERIA.VEHICLE.ACTIVE_RENT).values()
        notificationList = []
        for vehicle in rentedVehicles:
            delta = vehicle.rentLeftTime
            if delta > 0:
                if delta > time_utils.ONE_DAY:
                    period = time_utils.ONE_DAY
                elif delta > time_utils.ONE_HOUR:
                    period = time_utils.ONE_HOUR
                else:
                    period = delta
                notificationList.append((vehicle.intCD, delta % period or period))

        if len(notificationList) > 0:
            _, nextRentNotification = min(notificationList, key=itemgetter(1))
            for item in notificationList:
                if item[1] == nextRentNotification:
                    self.__vehiclesForUpdate.append(item[0])

            nextRentNotification = max(nextRentNotification, 0)
        else:
            return
        self.__rentNotifyTimeCallback = BigWorld.callback(nextRentNotification, self.__notifyRentTime)

    def __notifyRentTime(self):
        self.__rentNotifyTimeCallback = None
        self.onRentChangeNotify(self.__vehiclesForUpdate)
        self.__startRentTimeNotifyCallback()
        return

    def __clearRentTimeNotifyCallback(self):
        if self.__rentNotifyTimeCallback is not None:
            BigWorld.cancelCallback(self.__rentNotifyTimeCallback)
            self.__rentNotifyTimeCallback = None
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\game_control\RentalsController.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:43 St�edn� Evropa (letn� �as)
