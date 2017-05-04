# 2017.05.04 15:23:48 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/profile_cm_handlers.py
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU
from gui.shared import g_itemsCache, event_dispatcher as shared_events
from helpers import dependency
from skeletons.gui.game_control import IVehicleComparisonBasket

class PROFILE(object):
    VEHICLE_COMPARE = 'profileVehicleCompare'
    VEHICLE_INFO = 'profileVehicleInfo'


class ProfileVehicleCMHandler(AbstractContextMenuHandler, EventSystemEntity):
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)

    def __init__(self, cmProxy, ctx = None):
        super(ProfileVehicleCMHandler, self).__init__(cmProxy, ctx, {PROFILE.VEHICLE_COMPARE: 'compareVehicle',
         PROFILE.VEHICLE_INFO: 'showVehicleInfo'})

    def compareVehicle(self):
        self.comparisonBasket.addVehicle(self.__vehCD)

    def showVehicleInfo(self):
        shared_events.showVehicleInfo(self.__vehCD)

    def _generateOptions(self, ctx = None):
        vehicle = g_itemsCache.items.getItemByCD(self.__vehCD)
        options = []
        if not vehicle.isSecret or vehicle.isInInventory:
            options.append(self._makeItem(PROFILE.VEHICLE_INFO, MENU.CONTEXTMENU_VEHICLEINFOEX))
        if self.comparisonBasket.isEnabled():
            options.append(self._makeItem(PROFILE.VEHICLE_COMPARE, MENU.contextmenu(PROFILE.VEHICLE_COMPARE), {'enabled': self.comparisonBasket.isReadyToAdd(vehicle)}))
        return options

    def _initFlashValues(self, ctx):
        self.__vehCD = int(ctx.id)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\profile\profile_cm_handlers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:48 St�edn� Evropa (letn� �as)
