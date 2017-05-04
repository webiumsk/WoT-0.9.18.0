# 2017.05.04 15:22:04 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/base/unit/vehicles_watcher.py
from UnitBase import UNIT_SLOT
from account_helpers import getAccountDatabaseID
from constants import PREBATTLE_TYPE
from gui import game_control
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.prb_control.entities.base.unit.ctx import AssignUnitCtx
from gui.shared import g_itemsCache
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.game_control import IRentalsController, IIGRController

class UnitVehiclesWatcher(object):
    rentals = dependency.descriptor(IRentalsController)
    igrCtrl = dependency.descriptor(IIGRController)

    def __init__(self, entity):
        super(UnitVehiclesWatcher, self).__init__()
        self.__entity = entity

    def init(self):
        """
        Initialization method. Adds required subscriptions.
        """
        g_clientUpdateManager.addCallbacks({'inventory.1': self.__onVehiclesUpdated})
        self.rentals.onRentChangeNotify += self.__onRentUpdated
        self.igrCtrl.onIgrTypeChanged += self.__onIgrRoomChanged

    def fini(self):
        """
        Finalization method. Removes added subscriptions.
        """
        g_clientUpdateManager.removeObjectCallbacks(self, force=True)
        self.rentals.onRentChangeNotify -= self.__onRentUpdated
        self.igrCtrl.onIgrTypeChanged -= self.__onIgrRoomChanged

    def validate(self, update = False):
        """
        Validates vehicles selected in unit if player is in slot now
        Args:
            update: is this unit update
        """
        items = g_itemsCache.items
        invVehicles = items.getVehicles(REQ_CRITERIA.INVENTORY)
        vehCDs = invVehicles.keys()
        pInfo = self.__entity.getPlayerInfo()
        if pInfo.isInSlot:
            _, unit = self.__entity.getUnit()
            roster = unit.getRoster()
            if not roster.checkVehicleList(vehCDs, pInfo.slotIdx) and not pInfo.isCommander():
                self.__entity.request(AssignUnitCtx(pInfo.dbID, UNIT_SLOT.REMOVE, 'prebattle/assign'))
            elif self.__entity.getEntityType() != PREBATTLE_TYPE.FALLOUT:
                resultCtx = self.__entity.invalidateSelectedVehicles(vehCDs)
                if resultCtx is not None:
                    self.__entity.request(resultCtx)
                elif update:
                    self.__entity.unit_onUnitPlayerVehDictChanged(getAccountDatabaseID())
        elif update:
            self.__entity.unit_onUnitPlayerVehDictChanged(getAccountDatabaseID())
        return

    def __onVehiclesUpdated(self, vehicles):
        """
        Listener for inventory vehicles update
        Args:
            vehicles:
        """
        self.validate(update=True)

    def __onRentUpdated(self, vehicles):
        """
        Listener for rented vehicles update
        Args:
            vehicles:
        """
        self.validate(update=True)

    def __onIgrRoomChanged(self, roomType, xpFactor):
        """
        Listener for IGR room type changed
        Args:
            roomType:
            xpFactor:
        """
        self.validate(update=True)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\unit\vehicles_watcher.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:04 St�edn� Evropa (letn� �as)
