# 2017.05.04 15:25:52 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/__init__.py
from collections import namedtuple
import BigWorld
from gui.shared.items_parameters import params_helper, formatters
import nations
from debug_utils import *
from helpers import i18n, time_utils
from items import ITEM_TYPE_NAMES, vehicles, getTypeInfoByName, ITEM_TYPE_INDICES
from shared_utils import CONST_CONTAINER
from gui import nationCompareByIndex, GUI_SETTINGS
from gui.shared.money import Money, ZERO_MONEY, Currency
from gui.shared.economics import getActionPrc
from gui.shared.utils.functions import getShortDescr, stripShortDescrTags
CLAN_LOCK = 1
_ICONS_MASK = '../maps/icons/%(type)s/%(subtype)s%(unicName)s.png'
GUI_ITEM_TYPE_NAMES = tuple(ITEM_TYPE_NAMES) + tuple(['reserved'] * (16 - len(ITEM_TYPE_NAMES)))
GUI_ITEM_TYPE_NAMES += ('dossierAccount',
 'dossierVehicle',
 'dossierTankman',
 'achievement',
 'tankmanSkill')
GUI_ITEM_TYPE_INDICES = dict(((n, idx) for idx, n in enumerate(GUI_ITEM_TYPE_NAMES)))

class GUI_ITEM_TYPE(CONST_CONTAINER):
    VEHICLE = GUI_ITEM_TYPE_INDICES['vehicle']
    CHASSIS = GUI_ITEM_TYPE_INDICES['vehicleChassis']
    TURRET = GUI_ITEM_TYPE_INDICES['vehicleTurret']
    GUN = GUI_ITEM_TYPE_INDICES['vehicleGun']
    ENGINE = GUI_ITEM_TYPE_INDICES['vehicleEngine']
    FUEL_TANK = GUI_ITEM_TYPE_INDICES['vehicleFuelTank']
    RADIO = GUI_ITEM_TYPE_INDICES['vehicleRadio']
    TANKMAN = GUI_ITEM_TYPE_INDICES['tankman']
    OPTIONALDEVICE = GUI_ITEM_TYPE_INDICES['optionalDevice']
    SHELL = GUI_ITEM_TYPE_INDICES['shell']
    EQUIPMENT = GUI_ITEM_TYPE_INDICES['equipment']
    COMMON = tuple(ITEM_TYPE_INDICES.keys())
    ARTEFACTS = (EQUIPMENT, OPTIONALDEVICE)
    ACCOUNT_DOSSIER = GUI_ITEM_TYPE_INDICES['dossierAccount']
    VEHICLE_DOSSIER = GUI_ITEM_TYPE_INDICES['dossierVehicle']
    TANKMAN_DOSSIER = GUI_ITEM_TYPE_INDICES['dossierTankman']
    ACHIEVEMENT = GUI_ITEM_TYPE_INDICES['achievement']
    SKILL = GUI_ITEM_TYPE_INDICES['tankmanSkill']
    GUI = (ACCOUNT_DOSSIER,
     VEHICLE_DOSSIER,
     TANKMAN_DOSSIER,
     ACHIEVEMENT,
     SKILL)
    VEHICLE_MODULES = (GUN,
     TURRET,
     ENGINE,
     CHASSIS,
     RADIO)
    VEHICLE_COMPONENTS = VEHICLE_MODULES + ARTEFACTS + (SHELL,)


class ItemsCollection(dict):

    def filter(self, criteria):
        result = self.__class__()
        for intCD, item in self.iteritems():
            if criteria(item):
                result.update({intCD: item})

        return result

    def __repr__(self):
        return '%s<size:%d>' % (self.__class__.__name__, len(self.items()))


def getVehicleComponentsByType(vehicle, itemTypeIdx):
    """
    Returns collection of vehicle's installed items.
    
    @param vehicle: target vehicle
    @param itemTypeIdx: items.ITEM_TYPE_NAMES index
    
    @return: ItemsCollection instance
    """

    def packModules(modules):
        """ Helper function to pack item ot items list to the collection """
        if not isinstance(modules, list):
            modules = [modules]
        return ItemsCollection([ (module.intCD, module) for module in modules if module is not None ])

    if itemTypeIdx == vehicles._CHASSIS:
        return packModules(vehicle.chassis)
    if itemTypeIdx == vehicles._TURRET:
        return packModules(vehicle.turret)
    if itemTypeIdx == vehicles._GUN:
        return packModules(vehicle.gun)
    if itemTypeIdx == vehicles._ENGINE:
        return packModules(vehicle.engine)
    if itemTypeIdx == vehicles._FUEL_TANK:
        return packModules(vehicle.fuelTank)
    if itemTypeIdx == vehicles._RADIO:
        return packModules(vehicle.radio)
    if itemTypeIdx == vehicles._TANKMAN:
        from gui.shared.gui_items.Tankman import TankmenCollection
        return TankmenCollection([ (t.invID, t) for slotIdx, t in vehicle.crew ])
    if itemTypeIdx == vehicles._OPTIONALDEVICE:
        return packModules(vehicle.optDevices)
    if itemTypeIdx == vehicles._SHELL:
        return packModules(vehicle.shells)
    if itemTypeIdx == vehicles._EQUIPMENT:
        return packModules(vehicle.eqs)
    return ItemsCollection()


def getVehicleSuitablesByType(vehDescr, itemTypeId, turretPID = 0):
    """
    Returns all suitable items for given @vehicle.
    
    @param vehDescr: vehicle descriptor
    @param itemTypeId: requested items types
    @param turretPID: vehicle's turret id
    
    @return: (descriptors list, current vehicle's items compact descriptors list)
    """
    descriptorsList = list()
    current = list()
    if itemTypeId == vehicles._CHASSIS:
        current = [vehDescr.chassis['compactDescr']]
        descriptorsList = vehDescr.type.chassis
    elif itemTypeId == vehicles._ENGINE:
        current = [vehDescr.engine['compactDescr']]
        descriptorsList = vehDescr.type.engines
    elif itemTypeId == vehicles._RADIO:
        current = [vehDescr.radio['compactDescr']]
        descriptorsList = vehDescr.type.radios
    elif itemTypeId == vehicles._FUEL_TANK:
        current = [vehDescr.fuelTank['compactDescr']]
        descriptorsList = vehDescr.type.fuelTanks
    elif itemTypeId == vehicles._TURRET:
        current = [vehDescr.turret['compactDescr']]
        descriptorsList = vehDescr.type.turrets[turretPID]
    elif itemTypeId == vehicles._OPTIONALDEVICE:
        devs = vehicles.g_cache.optionalDevices()
        current = vehDescr.optionalDevices
        descriptorsList = [ dev for dev in devs.itervalues() if dev.checkCompatibilityWithVehicle(vehDescr)[0] ]
    elif itemTypeId == vehicles._EQUIPMENT:
        eqs = vehicles.g_cache.equipments()
        current = list()
        descriptorsList = [ eq for eq in eqs.itervalues() if eq.checkCompatibilityWithVehicle(vehDescr)[0] ]
    elif itemTypeId == vehicles._GUN:
        current = [vehDescr.gun['compactDescr']]
        for gun in vehDescr.turret['guns']:
            descriptorsList.append(gun)

        for turret in vehDescr.type.turrets[turretPID]:
            if turret is not vehDescr.turret:
                for gun in turret['guns']:
                    descriptorsList.append(gun)

    elif itemTypeId == vehicles._SHELL:
        for shot in vehDescr.gun['shots']:
            current.append(shot['shell']['compactDescr'])

        for gun in vehDescr.turret['guns']:
            for shot in gun['shots']:
                descriptorsList.append(shot['shell'])

        for turret in vehDescr.type.turrets[turretPID]:
            if turret is not vehDescr.turret:
                for gun in turret['guns']:
                    for shot in gun['shots']:
                        descriptorsList.append(shot['shell'])

    return (descriptorsList, current)


class GUIItem(object):

    def __init__(self, proxy = None):
        pass

    def __repr__(self):
        return self.__class__.__name__


class HasIntCD(object):

    def __init__(self, intCompactDescr):
        self.intCompactDescr = intCompactDescr
        self.itemTypeID, self.nationID, self.innationID = self._parseIntCompDescr(self.intCompactDescr)

    def _parseIntCompDescr(self, intCompactDescr):
        return vehicles.parseIntCompactDescr(intCompactDescr)

    @property
    def intCD(self):
        return self.intCompactDescr

    @property
    def itemTypeName(self):
        return ITEM_TYPE_NAMES[self.itemTypeID]

    @property
    def nationName(self):
        return nations.NAMES[self.nationID]

    def __cmp__(self, other):
        if self is other:
            return 1
        res = nationCompareByIndex(self.nationID, other.nationID)
        if res:
            return res
        return 0


class HasStrCD(object):

    def __init__(self, strCompactDescr):
        self.strCompactDescr = strCompactDescr

    @property
    def strCD(self):
        return self.strCompactDescr


_RentalInfoProvider = namedtuple('RentalInfoProvider', ('rentExpiryTime',
 'compensations',
 'battlesLeft',
 'winsLeft',
 'isRented'))

class RentalInfoProvider(_RentalInfoProvider):

    @staticmethod
    def __new__(cls, additionalData = None, time = 0, battles = 0, wins = 0, isRented = False, *args, **kwargs):
        additionalData = additionalData or {}
        if 'compensation' in additionalData:
            compensations = Money(*additionalData['compensation'])
        else:
            compensations = ZERO_MONEY
        result = _RentalInfoProvider.__new__(cls, time, compensations, battles, wins, isRented)
        return result

    def getTimeLeft(self):
        if self.rentExpiryTime != float('inf'):
            return float(time_utils.getTimeDeltaFromNow(time_utils.makeLocalServerTime(self.rentExpiryTime)))
        return float('inf')

    def getExpiryState(self):
        return self.rentExpiryTime != float('inf') and self.battlesLeft <= 0 and self.winsLeft <= 0 and self.getTimeLeft() <= 0


class FittingItem(GUIItem, HasIntCD):

    class TARGETS(object):
        CURRENT = 1
        IN_INVENTORY = 2
        OTHER = 3

    def __init__(self, intCompactDescr, proxy = None, isBoughtForCredits = False):
        GUIItem.__init__(self, proxy)
        HasIntCD.__init__(self, intCompactDescr)
        self.defaultPrice = ZERO_MONEY
        self._buyPrice = ZERO_MONEY
        self.sellPrice = ZERO_MONEY
        self.defaultSellPrice = ZERO_MONEY
        self.altPrice = None
        self.defaultAltPrice = None
        self.sellActionPrc = 0
        self.isHidden = False
        self.inventoryCount = 0
        self.sellForGold = False
        self.isUnlocked = False
        self.isBoughtForCredits = isBoughtForCredits
        self.rentInfo = RentalInfoProvider()
        self.restoreInfo = None
        self._personalDiscountPrice = None
        if proxy is not None and proxy.isSynced():
            self.defaultPrice = proxy.shop.defaults.getItemPrice(self.intCompactDescr)
            if self.defaultPrice is None:
                self.defaultPrice = ZERO_MONEY
            self._buyPrice, self.isHidden, self.sellForGold = proxy.shop.getItem(self.intCompactDescr)
            if self._buyPrice is None:
                self._buyPrice = ZERO_MONEY
            self.defaultSellPrice = Money(*BigWorld.player().shop.getSellPrice(self.defaultPrice, proxy.shop.defaults.sellPriceModifiers(intCompactDescr), self.itemTypeID))
            self.sellPrice = Money(*BigWorld.player().shop.getSellPrice(self._buyPrice, proxy.shop.sellPriceModifiers(intCompactDescr), self.itemTypeID))
            self.inventoryCount = proxy.inventory.getItems(self.itemTypeID, self.intCompactDescr)
            if self.inventoryCount is None:
                self.inventoryCount = 0
            self.isUnlocked = self.intCD in proxy.stats.unlocks
            self.isInitiallyUnlocked = self.intCD in proxy.stats.initialUnlocks
            self.altPrice = self._getAltPrice(self._buyPrice, proxy.shop)
            self.defaultAltPrice = self._getAltPrice(self.defaultPrice, proxy.shop.defaults)
            self.sellActionPrc = -1 * getActionPrc(self.sellPrice, self.defaultSellPrice)
        return

    def _getAltPrice(self, buyPrice, proxy):
        return None

    @property
    def buyPrice(self):
        return self._buyPrice

    @property
    def actionPrc(self):
        return getActionPrc(self.altPrice or self.buyPrice, self.defaultAltPrice or self.defaultPrice)

    @property
    def isSecret(self):
        return False

    @property
    def isPremium(self):
        return self.buyPrice.isSet(Currency.GOLD)

    @property
    def isPremiumIGR(self):
        return False

    @property
    def isRentable(self):
        return False

    @property
    def isRented(self):
        return False

    @property
    def descriptor(self):
        return vehicles.getDictDescr(self.intCompactDescr)

    @property
    def isRemovable(self):
        return True

    @property
    def minRentPrice(self):
        return None

    @property
    def rentLeftTime(self):
        return 0

    def isPreviewAllowed(self):
        return False

    @property
    def userType(self):
        return getTypeInfoByName(self.itemTypeName)['userString']

    @property
    def userName(self):
        return self.descriptor.get('userString', '')

    @property
    def longUserName(self):
        return self.userType + ' ' + self.userName

    @property
    def shortUserName(self):
        return self.descriptor.get('shortUserString', '')

    @property
    def shortDescription(self):
        return getShortDescr(self.descriptor.get('description', ''))

    @property
    def fullDescription(self):
        return stripShortDescrTags(self.descriptor.get('description', ''))

    @property
    def name(self):
        return self.descriptor.get('name', '')

    @property
    def level(self):
        return self.descriptor.get('level', 0)

    @property
    def isInInventory(self):
        return self.inventoryCount > 0

    def _getShortInfo(self, vehicle = None, expanded = False):
        try:
            description = i18n.makeString('#menu:descriptions/' + self.itemTypeName + ('Full' if expanded else ''))
            vehicleDescr = vehicle.descriptor if vehicle is not None else None
            params = params_helper.getParameters(self, vehicleDescr)
            formattedParametersDict = dict(formatters.getFormattedParamsList(self.descriptor, params))
            if self.itemTypeName == vehicles._VEHICLE:
                formattedParametersDict['caliber'] = BigWorld.wg_getIntegralFormat(self.descriptor.gun['shots'][0]['shell']['caliber'])
            result = description % formattedParametersDict
            return result
        except Exception:
            LOG_CURRENT_EXCEPTION()
            return ''

        return

    def getShortInfo(self, vehicle = None, expanded = False):
        if not GUI_SETTINGS.technicalInfo:
            return ''
        return self._getShortInfo(vehicle, expanded)

    def getParams(self, vehicle = None):
        return dict(params_helper.get(self, vehicle.descriptor if vehicle is not None else None))

    def getRentPackage(self, days = None):
        return None

    def getGUIEmblemID(self):
        return 'notFound'

    @property
    def icon(self):
        return _ICONS_MASK % {'type': self.itemTypeName,
         'subtype': '',
         'unicName': self.name.replace(':', '-')}

    @property
    def iconSmall(self):
        return _ICONS_MASK % {'type': self.itemTypeName,
         'subtype': 'small/',
         'unicName': self.name.replace(':', '-')}

    def getBuyPriceCurrency(self):
        if self.altPrice is not None:
            if self.altPrice.gold and not self.isBoughtForCredits:
                return Currency.GOLD
        elif self.buyPrice.gold:
            return Currency.GOLD
        return Currency.CREDITS

    def getSellPriceCurrency(self):
        return self.sellPrice.getCurrency()

    def isInstalled(self, vehicle, slotIdx = None):
        return False

    def mayInstall(self, vehicle, slotIdx = None):
        return vehicle.descriptor.mayInstallComponent(self.intCD)

    def mayRemove(self, vehicle):
        return (True, '')

    def mayRent(self, money):
        return (False, '')

    def mayRestore(self, money):
        return (False, '')

    def mayRestoreWithExchange(self, money, exchangeRate):
        return False

    def mayObtainForMoney(self, money):
        """
        # Check if possible to buy or to restore or to rent item
        @param money: <Money>
        @return: <bool>
        """
        mayRent, rentReason = self.mayRent(money)
        if self.isRestoreAvailable():
            mayPurchase, reason = self.mayRestore(money)
        else:
            mayPurchase, reason = self.mayPurchase(money)
        if mayRent or mayPurchase:
            return (True, '')
        elif self.isRentable and not mayRent:
            return (mayRent, rentReason)
        else:
            return (mayPurchase, reason)

    def mayPurchaseWithExchange(self, money, exchangeRate):
        canBuy, reason = self.mayPurchase(money)
        if canBuy:
            return canBuy
        elif reason == 'credits_error':
            price = self.altPrice or self.buyPrice
            money = money.exchange(Currency.GOLD, Currency.CREDITS, exchangeRate)
            return price <= money
        else:
            return False

    def mayObtainWithMoneyExchange(self, money, exchangeRate):
        """
        Check if possible to buy or to restore or to rent item with gold exchange
        @param money: <Money>
        @param exchangeRate: <int>
        @return: <bool>
        """
        canRent, rentReason = self.mayRent(money)
        if self.isRestoreAvailable():
            mayPurchase = self.mayRestoreWithExchange(money, exchangeRate)
        else:
            mayPurchase = self.mayPurchaseWithExchange(money, exchangeRate)
        return canRent or mayPurchase

    def mayPurchase(self, money):
        if getattr(BigWorld.player(), 'isLongDisconnectedFromCenter', False):
            return (False, 'center_unavailable')
        if self.itemTypeID not in (GUI_ITEM_TYPE.EQUIPMENT, GUI_ITEM_TYPE.OPTIONALDEVICE, GUI_ITEM_TYPE.SHELL) and not self.isUnlocked:
            return (False, 'unlock_error')
        if self.isHidden:
            return (False, 'isHidden')
        price = self.altPrice or self.buyPrice
        if not price:
            return (True, '')
        for c in price.getSetCurrencies():
            if money.get(c) >= price.get(c):
                return (True, '')

        shortage = money.getShortage(price)
        if shortage:
            currency, _ = shortage.pop()
            return (False, '%s_error' % currency)
        return (True, '')

    def getTarget(self, vehicle):
        if self.isInstalled(vehicle):
            return self.TARGETS.CURRENT
        if self.isInInventory:
            return self.TARGETS.IN_INVENTORY
        return self.TARGETS.OTHER

    def getConflictedEquipments(self, vehicle):
        return ()

    def getInstalledVehicles(self, vehs):
        return set()

    def isRestorePossible(self):
        return False

    def isRestoreAvailable(self):
        return False

    def _sortByType(self, other):
        return 0

    def __cmp__(self, other):
        if other is None:
            return 1
        res = HasIntCD.__cmp__(self, other)
        if res:
            return res
        res = self._sortByType(other)
        if res:
            return res
        res = self.level - other.level
        if res:
            return res
        res = self.buyPrice.gold - other.buyPrice.gold
        if res:
            return res
        res = self.buyPrice.credits - other.buyPrice.credits
        if res:
            return res
        else:
            return cmp(self.userName, other.userName)

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return self.intCompactDescr == other.intCompactDescr

    def __repr__(self):
        return '%s<intCD:%d, type:%s, nation:%d>' % (self.__class__.__name__,
         self.intCD,
         self.itemTypeName,
         self.nationID)


def getItemIconName(itemName):
    return '%s.png' % itemName.replace(':', '-')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:53 St�edn� Evropa (letn� �as)
