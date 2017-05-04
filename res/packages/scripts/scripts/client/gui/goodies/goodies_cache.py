# 2017.05.04 15:21:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/goodies/goodies_cache.py
import weakref
from collections import defaultdict
from debug_utils import LOG_WARNING
from goodies.goodie_constants import GOODIE_VARIETY, GOODIE_STATE, GOODIE_TARGET_TYPE
from gui.goodies.goodie_items import Booster, PersonalVehicleDiscount
from gui.shared.ItemsCache import g_itemsCache
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA

def _createBooster(boosterID, boosterDescription, proxy):
    """
    Creates booster GUI instance
    """
    return Booster(boosterID, boosterDescription, proxy)


def _createDiscount(discountID, discountDescription, proxy):
    """
    Creates personal discount GUI instance.
    Right now we have only one gui instance for discounts: PersonalVehicleDiscount.
    For others discounts we don't have UX, in that case return None
    """
    targetType = discountDescription.target.targetType
    if targetType in _DISCOUNT_TYPES_MAPPING:
        return _DISCOUNT_TYPES_MAPPING[targetType](discountID, discountDescription, proxy)
    else:
        LOG_WARNING('Current discount with ID: %s and type: %s is not supported by UX' % (discountID, targetType))
        return None
        return None


_GOODIES_VARIETY_MAPPING = {GOODIE_VARIETY.BOOSTER: _createBooster,
 GOODIE_VARIETY.DISCOUNT: _createDiscount}
_DISCOUNT_TYPES_MAPPING = {GOODIE_TARGET_TYPE.ON_BUY_VEHICLE: PersonalVehicleDiscount}

class _GoodiesCache(object):
    """
    Global goodies cache. Contains booster and goodie GUI items.
    Uses g_itemsCache.items.shop and g_itemsCache.items.goodies to create goodies cache
    Listen g_itemsCache events and keep cache in valid state
    """

    def __init__(self):
        self._items = weakref.proxy(g_itemsCache.items)
        self.__goodiesCache = defaultdict(dict)
        self.__activeBoostersTypes = None
        return

    def init(self):
        g_itemsCache.onSyncStarted += self.__clearCache

    def fini(self):
        g_itemsCache.onSyncStarted -= self.__clearCache

    def clear(self):
        self.__activeBoostersTypes = None
        while len(self.__goodiesCache):
            _, cache = self.__goodiesCache.popitem()
            cache.clear()

        return

    @property
    def personalGoodies(self):
        """
        Gets dynamic parts of goodies received on Account in player data. GoodiesRequester is Inventory analogue.
        """
        return self._items.goodies.goodies

    def getBoosterPriceData(self, boosterID):
        """
        Gets tuple of Booster price, Booster default price, is booster hidden
        """
        shop = self._items.shop
        return (shop.getBoosterPrice(boosterID), shop.defaults.getBoosterPrice(boosterID), boosterID in shop.getHiddenBoosters())

    def getItemByTargetValue(self, targetValue):
        """
        Gets GUI Item by target value
        """
        return self._items.getItemByCD(targetValue)

    def getActiveBoostersTypes(self):
        """
        Gets active boosters types
        """
        if self.__activeBoostersTypes is not None:
            return self.__activeBoostersTypes
        else:
            activeBoosterTypes = []
            for boosterID, boosterValues in self.personalGoodies.iteritems():
                if boosterValues.state == GOODIE_STATE.ACTIVE:
                    boosterDescription = self._items.shop.boosters.get(boosterID, None)
                    if boosterDescription:
                        activeBoosterTypes.append(boosterDescription.resource)

            self.__activeBoostersTypes = activeBoosterTypes
            return self.__activeBoostersTypes
            return

    def getBooster(self, boosterID):
        """
        Gets booster GUI instance
        """
        boosterDescription = self._items.shop.boosters.get(boosterID, None)
        return self.__makeGoodie(boosterID, boosterDescription)

    def getDiscount(self, discoutID):
        """
        Gets personal discount GUI instance
        """
        discountDescription = self._items.shop.discounts.get(discoutID, None)
        return self.__makeGoodie(discoutID, discountDescription)

    def getBoosters(self, criteria = REQ_CRITERIA.EMPTY):
        """
        Gets boosters GUI instances in format: {boosterID: booster, ...}
        """
        return self.__getGoodies(self._items.shop.boosters, criteria)

    def getDiscounts(self, criteria = REQ_CRITERIA.EMPTY):
        """
        Gets personal discounts GUI instances in format: {discountID: discount, ...}
        """
        return self.__getGoodies(self._items.shop.discounts, criteria)

    def __getGoodies(self, goodies, criteria = REQ_CRITERIA.EMPTY):
        """
        Gets goodies GUI instances in format: {goodieID: goodie, ...}
        """
        results = {}
        for goodieID, goodieDescription in goodies.iteritems():
            goodie = self.__makeGoodie(goodieID, goodieDescription)
            if goodie is not None and criteria(goodie):
                results[goodieID] = goodie

        return results

    def __makeGoodie(self, goodieID, goodieDescription):
        """
        Creates goodie GUI instance and adds it to cache by variety
        """
        goodie = None
        if goodieDescription is not None:
            variety = goodieDescription.variety
            container = self.__goodiesCache[variety]
            if goodieID in container:
                return container[goodieID]
            container[goodieID] = goodie = _GOODIES_VARIETY_MAPPING[variety](goodieID, goodieDescription, self)
        return goodie

    def __clearCache(self, *args):
        self.clear()


g_goodiesCache = _GoodiesCache()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\goodies\goodies_cache.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:46 St�edn� Evropa (letn� �as)
