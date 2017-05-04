# 2017.05.04 15:21:35 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/customization/inventory.py
from account_helpers.AccountSettings import AccountSettings
from gui.customization.shared import CUSTOMIZATION_TYPE, TYPE_NAME
from helpers import dependency
from skeletons.gui.server_events import IEventsCache

class Inventory(object):
    _questsCache = dependency.descriptor(IEventsCache)

    def __init__(self, events, dependencies):
        self._events = events
        self._currentVehicle = dependencies.g_currentVehicle
        self._itemsCache = dependencies.g_itemsCache
        self._vehiclesCache = dependencies.g_vehiclesCache

    def init(self):
        self._questsCache.onSyncCompleted += self._update
        self._currentVehicle.onChanged += self._update

    def start(self):
        self._update()

    def fini(self):
        self._currentVehicle.onChanged -= self._update
        self._questsCache.onSyncCompleted -= self._update

    def getInventoryItems(self, cNationID, rawItems = None):
        inventoryItems = ({}, {}, {})
        inventoryCustomization = self._itemsCache.items.inventory.getItemsData('customizations')
        for isGold, itemsData in inventoryCustomization.iteritems():
            if itemsData:
                for key in (None, self._currentVehicle.item.intCD):
                    if key not in itemsData:
                        continue
                    typedItemsData = itemsData[key]
                    for cTypeName, items in typedItemsData.iteritems():
                        cType = TYPE_NAME[cTypeName]
                        for item, itemNum in items.iteritems():
                            if cType != CUSTOMIZATION_TYPE.EMBLEM:
                                nationID, itemID = item
                            else:
                                nationID, itemID = None, item
                            allowedVehicles = []
                            if key is not None:
                                allowedVehicles.append(key)
                            if cNationID == nationID or cType == CUSTOMIZATION_TYPE.EMBLEM:
                                inventoryItems[cType][itemID] = [itemID,
                                 None if rawItems is None else rawItems[cType][itemID],
                                 None,
                                 isGold,
                                 allowedVehicles,
                                 [],
                                 (isGold, itemNum)]

        return inventoryItems

    def _update(self):
        cNationID = self._currentVehicle.item.descriptor.type.customizationNationID
        rawItems = (self._vehiclesCache.customization(cNationID)['camouflages'], self._vehiclesCache.playerEmblems()[1], self._vehiclesCache.customization(cNationID)['inscriptions'])
        inventoryItems = self.getInventoryItems(cNationID, rawItems)
        self._saveNewInventoryItemsOnFileSystem(inventoryItems)
        self._events.onInventoryUpdated(inventoryItems)

    def _saveNewInventoryItemsOnFileSystem(self, inventoryItems):
        newInventoryItems = AccountSettings.getSettings('customization')
        if newInventoryItems is None or not isinstance(newInventoryItems, tuple):
            newInventoryItems = ({}, {}, {})
        for cType in CUSTOMIZATION_TYPE.ALL:
            for itemID in inventoryItems[cType].keys():
                if self._currentVehicle.item.intCD not in newInventoryItems[cType]:
                    newInventoryItems[cType][self._currentVehicle.item.intCD] = {}
                if itemID not in newInventoryItems[cType][self._currentVehicle.item.intCD]:
                    newInventoryItems[cType][self._currentVehicle.item.intCD][itemID] = True

        AccountSettings.setSettings('customization', newInventoryItems)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\customization\inventory.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:35 St�edn� Evropa (letn� �as)
