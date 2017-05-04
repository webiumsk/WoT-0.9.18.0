# 2017.05.04 15:22:13 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/sandbox/pre_queue/vehicles_watcher.py
from itertools import chain
from constants import MAX_VEHICLE_LEVEL
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.prb_control.ctrl_events import g_prbCtrlEvents
from gui.prb_control.settings import SANDBOX_MAX_VEHICLE_LEVEL
from gui.shared import g_itemsCache
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.utils.requesters import REQ_CRITERIA

class SandboxVehiclesWatcher(object):
    """
    Sandbox vehicles watcher class: listens for proper events
    and updates the states of vehicles selected
    """

    def start(self):
        """
        Starts listening for events
        """
        self.__setUnsuitableState()
        g_clientUpdateManager.addCallbacks({'inventory': self.__onInventoryChanged})

    def stop(self):
        """
        Stops listening for events
        """
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__clearUnsuitableState()

    def __getUnsuitableVehicles(self):
        """
        Gets all unsupported vehicles
        """
        vehs = g_itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.LEVELS(range(SANDBOX_MAX_VEHICLE_LEVEL + 1, MAX_VEHICLE_LEVEL + 1))).itervalues()
        eventVehs = g_itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.EVENT_BATTLE).itervalues()
        return chain(vehs, eventVehs)

    def __setUnsuitableState(self):
        """
        Sets to all unsupported vehicles custom state
        """
        vehicles = self.__getUnsuitableVehicles()
        intCDs = set()
        for vehicle in vehicles:
            vehicle.setCustomState(Vehicle.VEHICLE_STATE.UNSUITABLE_TO_QUEUE)
            intCDs.add(vehicle.intCD)

        if intCDs:
            g_prbCtrlEvents.onVehicleClientStateChanged(intCDs)

    def __clearUnsuitableState(self):
        """
        Unsets to all unsupported vehicles custom state
        """
        vehicles = self.__getUnsuitableVehicles()
        intCDs = set()
        for vehicle in vehicles:
            vehicle.clearCustomState()
            intCDs.add(vehicle.intCD)

        if intCDs:
            g_prbCtrlEvents.onVehicleClientStateChanged(intCDs)

    def __onInventoryChanged(self, diff):
        """
        Listener for inventory update envent
        Args:
            diff: inventory update diff
        """
        self.__setUnsuitableState()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\sandbox\pre_queue\vehicles_watcher.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:13 St�edn� Evropa (letn� �as)
