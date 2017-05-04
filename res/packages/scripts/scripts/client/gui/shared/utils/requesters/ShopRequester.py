# 2017.05.04 15:26:29 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/utils/requesters/ShopRequester.py
import weakref
from collections import defaultdict, namedtuple
from abc import ABCMeta, abstractmethod
import BigWorld
from adisp import async
from constants import WIN_XP_FACTOR_MODE
from debug_utils import LOG_DEBUG
from goodies.goodie_constants import GOODIE_VARIETY, GOODIE_TARGET_TYPE
from goodies.goodie_helpers import getPremiumCost, getPriceWithDiscount, GoodieData, getPriceTupleWithDiscount
from gui.shared.money import Money
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
_VehiclesRestoreConfig = namedtuple('_VehiclesRestoreConfig', 'restoreDuration restoreCooldown restorePriceModif')
_TankmenRestoreConfig = namedtuple('_VehiclesRestoreConfig', 'freeDuration creditsDuration cost limit')
_TargetData = namedtuple('_TargetData', 'targetType, targetValue, limit')
_ResourceData = namedtuple('_ResourceData', 'resourceType, value, isPercentage')
_ConditionData = namedtuple('_ConditionData', 'conditionType, value')
_TradeInData = namedtuple('_TradeInData', ['sellPriceFactor',
 'allowedVehicleLevels',
 'forbiddenVehicles',
 'minAcceptableSellPrice'])
_TradeInData.__new__.__defaults__ = (0,
 (),
 (),
 0)

class _NamedGoodieData(GoodieData):
    """
    variety - GOODIE_VARIETY.BOOSTER or GOODIE_VARIETY.DISCOUNT
    
    target - (targetType, targetValue, limit) - denotes the type of the discountable/boostable entity
             targetType - one of GOODIE_TARGET_TYPEs
             targetValue - the name of the target (for example premium packet name)
             limit - limits resource usage (for example 100% discount on free xp conversion, but no more than 20 gold)
    
    enabled - denotes whether a goodie of that type can be given
    
    lifetime - lifetime of a goodie [seconds]
    
    useby - time after which a goodie will no longer be valid and be lost [seconds]
    
    counter - denotes how many goodies will be given initially [deprecated]
    
    autostart - denotes whether to activate a goodie right after creation True or False
    
    condition - (conditionType, value) - denotes internal condition for a goodie (for example vehicle level)
                conditionType - one of GOODIE_CONDITION_TYPEs
                value - condition value (e.g. vehicle level)
    
    resource - (resourceType, value, isPercentage)
               resourceType - one of GOODIE_RESOURCE_TYPEs
               value - discount/booster value on that given resource
               isPercentage - True if percentage, False otherwise
    """

    @staticmethod
    def __new__(cls, variety, target, enabled, lifetime, useby, counter, autostart, condition, resource):
        return GoodieData.__new__(cls, variety, _TargetData(*target) if target else None, enabled, lifetime, useby, counter, autostart, _ConditionData(*condition) if condition else None, _ResourceData(*resource) if resource else None)

    def getTargetValue(self):
        if self.target.targetType == GOODIE_TARGET_TYPE.ON_BUY_PREMIUM:
            return int(self.target.targetValue.split('_')[1])
        else:
            return self.target.targetValue


class TradeInData(_TradeInData):
    """
    Trade in config data:
        sellPriceFactor - multiplier for buy price, that player will receive during trade off
        allowedVehicleLevels - vehicle levels that allowed to trade
        forbiddenVehicles - vehicle int CDs that are forbidden to trade
    """

    @property
    def isEnabled(self):
        """
        Trade in price factor greater then zero means that all trade in feature is enabled.
        """
        return self.sellPriceFactor > 0


class ShopCommonStats(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getValue(self, key, defaultValue = None):
        pass

    def getPrices(self):
        return self.getItemsData().get('itemPrices', {})

    def getBoosterPrices(self):
        return self.getGoodiesData().get('prices', {})

    def getHiddens(self):
        return self.getItemsData().get('notInShopItems', set([]))

    def getHiddenBoosters(self):
        return self.getGoodiesData().get('notInShop', set([]))

    def getNotToBuyVehicles(self):
        return self.getItemsData().get('vehiclesNotToBuy', set([]))

    def getVehicleRentPrices(self):
        return self.getItemsData().get('vehiclesRentPrices', {})

    def getVehiclesForGold(self):
        return self.getItemsData().get('vehiclesToSellForGold', set([]))

    def getVehiclesSellPriceFactors(self):
        return self.getItemsData().get('vehicleSellPriceFactors', {})

    def getItemPrice(self, intCD):
        asTuple = self.getPrices().get(intCD, tuple())
        return Money(*asTuple)

    def getBoosterPrice(self, boosterID):
        asTuple = self.getBoosterPrices().get(boosterID, tuple())
        return Money(*asTuple)

    def getItem(self, intCD):
        return (self.getItemPrice(intCD), intCD in self.getHiddens(), intCD in self.getVehiclesForGold())

    @property
    def revision(self):
        """
        @return: shop revision value
        """
        return self.getValue('rev', 0)

    @property
    def paidRemovalCost(self):
        """
        @return: cost of dismantling of non-removable optional
                                devices for gold
        """
        return self.getValue('paidRemovalCost', 10)

    @property
    def exchangeRate(self):
        """
        @return: rate of gold for credits exchanging
        """
        return self.getValue('exchangeRate', 400)

    @property
    def exchangeRateForShellsAndEqs(self):
        """
        @return: rate of gold for credits exchanging for F2W
                                premium shells and eqs action
        """
        return self.getValue('exchangeRateForShellsAndEqs', 400)

    @property
    def sellPriceModif(self):
        return self.getValue('sellPriceModif', 0.5)

    @property
    def vehiclesRestoreConfig(self):
        config = self.__getRestoreConfig().get('vehicles', {})
        return _VehiclesRestoreConfig(config.get('premiumDuration', 0), config.get('actionCooldown', 0), config.get('sellToRestoreFactor', 1.1))

    @property
    def tankmenRestoreConfig(self):
        config = self.__getRestoreConfig().get('tankmen', {})
        return _TankmenRestoreConfig(config.get('freeDuration', 0), config.get('creditsDuration', 0), Money(credits=config.get('creditsCost', 0)), config.get('limit', 100))

    def sellPriceModifiers(self, compDescr):
        sellPriceModif = self.sellPriceModif
        sellPriceFactors = self.getVehiclesSellPriceFactors()
        sellForGold = self.getVehiclesForGold()
        return (self.revision,
         self.exchangeRate,
         self.exchangeRateForShellsAndEqs,
         sellPriceModif,
         sellPriceFactors.get(compDescr, sellPriceModif),
         compDescr in sellForGold)

    @property
    def slotsPrices(self):
        return self.getValue('slotsPrices', (0, [300]))

    def getVehicleSlotsPrice(self, currentSlotsCount):
        """
        @param currentSlotsCount: current vehicle slots count
        @return: new vehicle slot price
        """
        player = BigWorld.player()
        return player.shop.getNextSlotPrice(currentSlotsCount, self.slotsPrices)

    @property
    def dropSkillsCost(self):
        """
        @return: drop tankman skill cost
        """
        return self.getValue('dropSkillsCost', {})

    @property
    def dailyXPFactor(self):
        """
        @return: daily experience multiplier
        """
        return self.getValue('dailyXPFactor', 2)

    @property
    def winXPFactorMode(self):
        """
        @return: mode for applying daily XP factor
        """
        return self.getValue('winXPFactorMode', WIN_XP_FACTOR_MODE.DAILY)

    @property
    def berthsPrices(self):
        return self.getValue('berthsPrices', (0, 1, [300]))

    def getTankmanBerthPrice(self, berthsCount):
        """
        @param berthsCount: current barrack's berths count
        @return: (new berths pack price, pack berths count)
        """
        prices = self.berthsPrices
        goldCost = BigWorld.player().shop.getNextBerthPackPrice(berthsCount, prices)
        return (Money(gold=goldCost), prices[1])

    @property
    def isEnabledBuyingGoldShellsForCredits(self):
        """
        @return: is premium shells for credits action enabled
        """
        return self.getValue('isEnabledBuyingGoldShellsForCredits', False)

    @property
    def isEnabledBuyingGoldEqsForCredits(self):
        """
        @return: is premium equipments for credits action enabled
        """
        return self.getValue('isEnabledBuyingGoldEqsForCredits', False)

    @property
    def tankmanCost(self):
        """
        @return: tankman studying cost
                        tmanCost -  ( tmanCostType, ), where
                        tmanCostType = {
                                        'roleLevel' : minimal role level after operation,
                                        'credits' : cost in credits,
                                        'gold' : cost in gold,
                                        'baseRoleLoss' : float in [0, 1], fraction of role to drop,
                                        'classChangeRoleLoss' : float in [0, 1], fraction of role to drop
                                                additionally if
                                                classes of self.vehicleTypeID and newVehicleTypeID are different,
                                        'isPremium' : tankman becomes premium,
                                        }.
                                List is sorted by role level.
        """
        return self.getValue('tankmanCost', tuple())

    @property
    def changeRoleCost(self):
        """
        @return: tankman change role cost in gold
        """
        return self.getValue('changeRoleCost', 600)

    @property
    def freeXPConversion(self):
        """
        @return: free experience to vehicle xp exchange rate and cost
                                ( discrecity, cost)
        """
        return self.getValue('freeXPConversion', (25, 1))

    @property
    def passportChangeCost(self):
        """
        @return: tankman passport replace cost in gold
        """
        return self.getValue('passportChangeCost', 50)

    @property
    def passportFemaleChangeCost(self):
        """
        @return: tankman passport replace cost in gold
        """
        return self.getValue('femalePassportChangeCost', 500)

    @property
    def freeXPToTManXPRate(self):
        """
        @return: free experience to tankman experience exchange rate
        """
        return self.getValue('freeXPToTManXPRate', 10)

    def getItemsData(self):
        return self.getValue('items', {})

    def getGoodiesData(self):
        return self.getValue('goodies', {})

    def getVehCamouflagePriceFactor(self, typeCompDescr):
        return self.getItemsData().get('vehicleCamouflagePriceFactors', {}).get(typeCompDescr)

    def getHornPriceFactor(self, hornID):
        return self.getItemsData().get('vehicleHornPriceFactors', {}).get(hornID)

    def getEmblemsGroupPriceFactors(self):
        return self.getItemsData().get('playerEmblemGroupPriceFactors', {})

    def getEmblemsGroupHiddens(self):
        return self.getItemsData().get('notInShopPlayerEmblemGroups', set([]))

    def getInscriptionsGroupPriceFactors(self, nationID):
        return self.getItemsData().get('inscriptionGroupPriceFactors', [])[nationID]

    def getInscriptionsGroupHiddens(self, nationID):
        return self.getItemsData().get('notInShopInscriptionGroups', [])[nationID]

    def getCamouflagesPriceFactors(self, nationID):
        return self.getItemsData().get('camouflagePriceFactors', [])[nationID]

    def getCamouflagesHiddens(self, nationID):
        return self.getItemsData().get('notInShopCamouflages', [])[nationID]

    def getHornPrice(self, hornID):
        return self.getItemsData().get('hornPrices', {}).get(hornID)

    @property
    def premiumCost(self):
        return self.getValue('premiumCost', {})

    @property
    def goodies(self):
        return self.getGoodiesData().get('goodies', {})

    def getGoodieByID(self, discountID):
        return self.goodies.get(discountID, None)

    def getGoodiesByVariety(self, variety):
        return dict(filter(lambda (goodieID, item): item.variety == variety, self.goodies.iteritems()))

    @property
    def boosters(self):
        return self.getGoodiesByVariety(GOODIE_VARIETY.BOOSTER)

    @property
    def discounts(self):
        return self.getGoodiesByVariety(GOODIE_VARIETY.DISCOUNT)

    def getPremiumPacketCost(self, days):
        return self.premiumCost.get(days)

    @property
    def camouflageCost(self):
        return self.getValue('camouflageCost', {})

    def getCamouflageCost(self, days = 0):
        return self.camouflageCost.get(days)

    @property
    def playerInscriptionCost(self):
        return self.getValue('playerInscriptionCost', {})

    def getInscriptionCost(self, days = 0):
        return self.playerInscriptionCost.get(days)

    @property
    def playerEmblemCost(self):
        return self.getValue('playerEmblemCost', {})

    def getEmblemCost(self, days = 0):
        return self.playerEmblemCost.get(days)

    @property
    def refSystem(self):
        return self.getValue('refSystem', {})

    @property
    def tradeIn(self):
        tradeInData = self.getValue('tradeIn')
        if tradeInData is not None:
            return TradeInData(**tradeInData)
        else:
            return TradeInData()

    def __getRestoreConfig(self):
        return self.getValue('restore_config', {})


class ShopRequester(AbstractSyncDataRequester, ShopCommonStats):

    def __init__(self, goodies):
        super(ShopRequester, self).__init__()
        self.defaults = DefaultShopRequester({}, self)
        self._goodies = weakref.proxy(goodies)

    def clear(self):
        self.defaults.clear()
        super(ShopRequester, self).clear()

    def getValue(self, key, defaultValue = None):
        return self.getCacheValue(key, defaultValue)

    def _response(self, resID, invData, callback):
        if invData is not None:
            self.defaults.update(invData.get('defaults'))
        super(ShopRequester, self)._response(resID, invData, callback)
        return

    @async
    def _requestCache(self, callback):
        """
        Overloaded method to request shop cache
        """
        BigWorld.player().shop.getCache(lambda resID, value, rev: self._response(resID, value, callback))

    def _preprocessValidData(self, data):
        data = dict(data)
        if 'goodies' in data:
            goodies = data['goodies'].get('goodies', {})
            formattedGoodies = {}
            for goodieID, goodieData in goodies.iteritems():
                formattedGoodies[goodieID] = _NamedGoodieData(*goodieData)

            data['goodies']['goodies'] = formattedGoodies
        return data

    def getPremiumCostWithDiscount(self, premiumPacketDiscounts = None):
        discounts = premiumPacketDiscounts or self.personalPremiumPacketsDiscounts
        premiumCostWithDiscount = self.premiumCost.copy()
        for discount in discounts.itervalues():
            premiumCostWithDiscount[discount.getTargetValue()] = getPremiumCost(self.premiumCost, discount)

        return premiumCostWithDiscount

    def getTankmanCostWithDefaults(self):
        """
        @return: tankman studying cost
                        tmanCost, action -  ( tmanCostType, ), ( actionData, ) where
                        tmanCostType = {
                                        'roleLevel' : minimal role level after operation,
                                        'credits' : cost in credits,
                                        'defCredits' : cost in credits,
                                        'gold' : default cost in gold,
                                        'defGold' : default cost in gold,
                                        'baseRoleLoss' : float in [0, 1], fraction of role to drop,
                                        'classChangeRoleLoss' : float in [0, 1], fraction of role to drop
                                        additionally if
                                                classes of self.vehicleTypeID and newVehicleTypeID are different,
                                        'isPremium' : tankman becomes premium,
                                        }.
                                List is sorted by role level.
                        actionData = Action data for each level of retraining
        """
        from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE
        from gui.shared.tooltips.formatters import packActionTooltipData
        shopPrices = self.tankmanCost
        defaultPrices = self.defaults.tankmanCost
        action = []
        tmanCost = []
        for idx, price in enumerate(shopPrices):
            data = price.copy()
            shopPrice = Money(**price)
            defaultPrice = Money(**defaultPrices[idx])
            actionData = None
            if shopPrice != defaultPrice:
                key = '{}TankmanCost'.format(shopPrice.getCurrency(byWeight=True))
                actionData = packActionTooltipData(ACTION_TOOLTIPS_TYPE.ECONOMICS, key, True, shopPrice, defaultPrice)
            tmanCost.append(data)
            action.append(actionData)

        return (tmanCost, action)

    def getVehicleSlotsPrice(self, currentSlotsCount):
        price = super(ShopRequester, self).getVehicleSlotsPrice(currentSlotsCount)
        slotGoodies = self.personalSlotDiscounts
        if slotGoodies:
            bestGoody = self.bestGoody(slotGoodies)
            return getPriceWithDiscount(price, bestGoody.resource)
        else:
            return price

    @property
    def tankmanCostWithGoodyDiscount(self):
        prices = self.tankmanCost
        tankmanGoodies = self.personalTankmanDiscounts
        if tankmanGoodies:
            bestGoody = self.bestGoody(tankmanGoodies)
            return self.__applyGoodyToStudyCost(prices, bestGoody)
        else:
            return prices

    @property
    def freeXPConversionLimit(self):
        goody = self.bestGoody(self.personalXPExchangeDiscounts)
        if goody:
            return goody.target.limit * self.defaults.freeXPConversion[0]
        else:
            return None
            return None

    @property
    def freeXPConversionWithDiscount(self):
        goody = self.bestGoody(self.personalXPExchangeDiscounts)
        rate = self.freeXPConversion
        if goody:
            return (getPriceWithDiscount(rate[0], goody.resource), rate[1])
        else:
            return rate

    @property
    def isXPConversionActionActive(self):
        goody = self.bestGoody(self.personalXPExchangeDiscounts)
        return self.freeXPConversion[0] > self.defaults.freeXPConversion[0] or goody is not None

    @property
    def personalPremiumPacketsDiscounts(self):
        return self.__personalDiscountsByTarget(GOODIE_TARGET_TYPE.ON_BUY_PREMIUM)

    @property
    def personalSlotDiscounts(self):
        return self.__personalDiscountsByTarget(GOODIE_TARGET_TYPE.ON_BUY_SLOT)

    @property
    def personalTankmanDiscounts(self):
        return self.__personalDiscountsByTarget(GOODIE_TARGET_TYPE.ON_BUY_GOLD_TANKMEN)

    @property
    def personalXPExchangeDiscounts(self):
        return self.__personalDiscountsByTarget(GOODIE_TARGET_TYPE.ON_FREE_XP_CONVERSION)

    @property
    def personalVehicleDiscounts(self):
        """
        Return personal vehicle discounts in account
        """
        return self.__personalDiscountsByTarget(GOODIE_TARGET_TYPE.ON_BUY_VEHICLE)

    def getVehicleDiscountDescriptions(self):
        """
        Return vehicle discounts descriptions
        """
        return self.__getDiscountsDescriptionsByTarget(GOODIE_TARGET_TYPE.ON_BUY_VEHICLE)

    def getPersonalVehicleDiscountPrice(self, typeCompDescr):
        """
        Return price with max discount for selected vehicle
        """
        defaultPrice = self.defaults.getItemPrice(typeCompDescr)
        currency = defaultPrice.getCurrency()
        personalVehicleDiscountPrice = None
        for discountID, discount in self.personalVehicleDiscounts.iteritems():
            if discount.getTargetValue() == typeCompDescr:
                discountPrice = getPriceTupleWithDiscount(defaultPrice, discount.resource)
                if discountPrice is not None:
                    tempPrice = Money(*discountPrice)
                    if personalVehicleDiscountPrice is None or tempPrice.get(currency) <= personalVehicleDiscountPrice.get(currency):
                        personalVehicleDiscountPrice = tempPrice

        return personalVehicleDiscountPrice

    def bestGoody(self, goodies):
        if goodies:
            _, goody = sorted(goodies.iteritems(), key=lambda (_, goody): goody.resource[1])[-1]
            return goody
        else:
            return None
            return None

    def __getDiscountsDescriptionsByTarget(self, targetType):
        """
        Gets all possible discounts descriptions by targetType
        """
        return dict(filter(lambda (discountID, item): item.target.targetType == targetType and item.enabled, self.discounts.iteritems()))

    def __applyGoodyToStudyCost(self, prices, goody):

        def convert(price):
            newPrice = price.copy()
            if price['isPremium']:
                newPrice['gold'] = getPriceWithDiscount(price['gold'], goody.resource)
            return newPrice

        return tuple(map(convert, prices))

    def __personalDiscountsByTarget(self, targetType):
        """
        Gets discounts by targetType in account
        """
        discounts = self.__getDiscountsDescriptionsByTarget(targetType)
        return dict(filter(lambda (discountID, item): discountID in self._goodies.goodies, discounts.iteritems()))


class DefaultShopRequester(ShopCommonStats):

    def __init__(self, cache, proxy):
        self.__cache = cache.copy()
        self.__proxy = weakref.proxy(proxy)

    def clear(self):
        LOG_DEBUG('Clearing shop defaults.')
        self.__cache.clear()

    def update(self, cache):
        if cache is None:
            cache = {}
        self.clear()
        self.__cache = cache.copy()
        return

    def getValue(self, key, defaultValue = None):
        return self.__cache.get(key, defaultValue)

    @property
    def revision(self):
        return self.__proxy.revision

    def getPrices(self):
        return self.getItemsData().get('itemPrices', self.__proxy.getPrices())

    def getBoosterPrices(self):
        return self.getGoodiesData().get('prices', self.__proxy.getBoosterPrices())

    def getHiddens(self):
        return self.getItemsData().get('notInShopItems', self.__proxy.getHiddens())

    def getHiddenBoosters(self):
        return self.getGoodiesData().get('notInShop', self.__proxy.getHiddenBoosters())

    def getNotToBuyVehicles(self):
        return self.getItemsData().get('vehiclesNotToBuy', self.__proxy.getNotToBuyVehicles())

    def getVehicleRentPrices(self):
        return self.getItemsData().get('vehiclesRentPrices', self.__proxy.getVehicleRentPrices())

    def getVehiclesForGold(self):
        return self.getItemsData().get('vehiclesToSellForGold', {})

    def getVehiclesSellPriceFactors(self):
        return self.getItemsData().get('vehicleSellPriceFactors', {})

    def getItemPrice(self, intCD):
        return Money(*self.getPrices().get(intCD, self.__proxy.getItemPrice(intCD)))

    def getBoosterPrice(self, boosterID):
        return Money(*self.getBoosterPrices().get(boosterID, self.__proxy.getBoosterPrice(boosterID)))

    @property
    def paidRemovalCost(self):
        """
        @return: cost of dismantling of non-removable optional
                                devices for gold
        """
        return self.getValue('paidRemovalCost', self.__proxy.paidRemovalCost)

    @property
    def exchangeRate(self):
        """
        @return: rate of gold for credits exchanging
        """
        return self.getValue('exchangeRate', self.__proxy.exchangeRate)

    @property
    def exchangeRateForShellsAndEqs(self):
        """
        @return: rate of gold for credits exchanging for F2W
                                premium shells and eqs action
        """
        return self.getValue('exchangeRateForShellsAndEqs', self.__proxy.exchangeRateForShellsAndEqs)

    @property
    def sellPriceModif(self):
        return self.getValue('sellPriceModif', self.__proxy.sellPriceModif)

    @property
    def slotsPrices(self):
        return self.getValue('slotsPrices', self.__proxy.slotsPrices)

    @property
    def dropSkillsCost(self):
        """
        @return: drop tankman skill cost
        """
        value = self.__proxy.dropSkillsCost
        defaults = self.getValue('dropSkillsCost')
        if defaults is None:
            return value
        else:
            newValue = {}
            for k, v in value.items():
                mergedValue = v.copy()
                defaultValue = defaults.get(k, {})
                mergedValue.update(defaultValue)
                newValue[k] = mergedValue

            return newValue

    @property
    def dailyXPFactor(self):
        """
        @return: daily experience multiplier
        """
        return self.getValue('dailyXPFactor', self.__proxy.dailyXPFactor)

    @property
    def winXPFactorMode(self):
        """
        @return: mode for applying daily XP factor
        """
        return self.getValue('winXPFactorMode', self.__proxy.winXPFactorMode)

    @property
    def berthsPrices(self):
        return self.getValue('berthsPrices', self.__proxy.berthsPrices)

    @property
    def isEnabledBuyingGoldShellsForCredits(self):
        """
        @return: is premium shells for credits action enabled
        """
        return self.getValue('isEnabledBuyingGoldShellsForCredits', self.__proxy.isEnabledBuyingGoldShellsForCredits)

    @property
    def isEnabledBuyingGoldEqsForCredits(self):
        """
        @return: is premium equipments for credits action enabled
        """
        return self.getValue('isEnabledBuyingGoldEqsForCredits', self.__proxy.isEnabledBuyingGoldEqsForCredits)

    @property
    def tankmanCost(self):
        """
        @return: tankman studying cost
                        tmanCost -  ( tmanCostType, ), where
                        tmanCostType = {
                                        'roleLevel' : minimal role level after operation,
                                        'credits' : cost in credits,
                                        'gold' : cost in gold,
                                        'baseRoleLoss' : float in [0, 1], fraction of role to drop,
                                        'classChangeRoleLoss' : float in [0, 1], fraction of role to drop
                                        additionally if
                                                classes of self.vehicleTypeID and newVehicleTypeID are different,
                                        'isPremium' : tankman becomes premium,
                                        }.
                                List is sorted by role level.
        """
        value = self.__proxy.tankmanCost
        defaults = self.getValue('tankmanCost')
        if defaults is None:
            return value
        else:
            newValues = []
            for idx, cost in enumerate(value):
                default = defaults[idx] if len(defaults) > idx else {}
                newValue = cost.copy()
                newValue.update(default)
                newValues.append(newValue)

            return newValues

    @property
    def changeRoleCost(self):
        """
        @return: tankman change role cost in gold
        """
        return self.getValue('changeRoleCost', self.__proxy.changeRoleCost)

    @property
    def freeXPConversion(self):
        """
        @return: free experience to vehicle xp exchange rate and cost
                                ( discrecity, cost)
        """
        return self.getValue('freeXPConversion', self.__proxy.freeXPConversion)

    @property
    def passportChangeCost(self):
        """
        @return: tankman passport replace cost in gold
        """
        return self.getValue('passportChangeCost', self.__proxy.passportChangeCost)

    @property
    def passportFemaleChangeCost(self):
        """
        @return: tankman passport replace cost in gold
        """
        return self.getValue('femalePassportChangeCost', self.__proxy.passportFemaleChangeCost)

    @property
    def freeXPToTManXPRate(self):
        """
        @return: free experience to tankman experience exchange rate
        """
        return self.getValue('freeXPToTManXPRate', self.__proxy.freeXPToTManXPRate)

    def getItemsData(self):
        return self.getValue('items', self.__proxy.getItemsData())

    def getGoodiesData(self):
        return self.getValue('goodies', self.__proxy.getGoodiesData())

    def getVehCamouflagePriceFactor(self, typeCompDescr):
        value = self.getItemsData().get('vehicleCamouflagePriceFactors', {}).get(typeCompDescr)
        if value is None:
            return self.__proxy.getVehCamouflagePriceFactor(typeCompDescr)
        else:
            return value

    def getHornPriceFactor(self, hornID):
        value = self.getItemsData().get('vehicleHornPriceFactors', {}).get(hornID)
        if value is None:
            return self.__proxy.getVehCamouflagePriceFactor(hornID)
        else:
            return value

    def getEmblemsGroupPriceFactors(self):
        return self.getItemsData().get('playerEmblemGroupPriceFactors', self.__proxy.getEmblemsGroupPriceFactors())

    def getEmblemsGroupHiddens(self):
        return self.getItemsData().get('notInShopPlayerEmblemGroups', self.__proxy.getEmblemsGroupHiddens())

    def getInscriptionsGroupPriceFactors(self, nationID):
        value = self.getItemsData().get('inscriptionGroupPriceFactors', [])
        if len(value) <= nationID:
            return self.__proxy.getInscriptionsGroupPriceFactors(nationID)
        return value[nationID]

    def getInscriptionsGroupHiddens(self, nationID):
        value = self.getItemsData().get('notInShopInscriptionGroups', [])
        if len(value) <= nationID:
            return self.__proxy.getInscriptionsGroupHiddens(nationID)
        return value[nationID]

    def getCamouflagesPriceFactors(self, nationID):
        value = self.getItemsData().get('camouflagePriceFactors', [])
        if len(value) <= nationID:
            return self.__proxy.getCamouflagesPriceFactors(nationID)
        return value[nationID]

    def getCamouflagesHiddens(self, nationID):
        value = self.getItemsData().get('notInShopCamouflages', [])
        if len(value) <= nationID:
            return self.__proxy.getCamouflagesHiddens(nationID)
        return value[nationID]

    def getHornPrice(self, hornID):
        value = self.getItemsData().get('hornPrices', {}).get(hornID)
        if value is None:
            return self.__proxy.getHornPrice(hornID)
        else:
            return value

    @property
    def premiumCost(self):
        value = self.__proxy.premiumCost.copy()
        value.update(self.getValue('premiumCost', {}))
        return value

    @property
    def goodies(self):
        return self.getGoodiesData().get('goodies', self.__proxy.goodies)

    @property
    def camouflageCost(self):
        value = self.__proxy.camouflageCost.copy()
        value.update(self.getValue('camouflageCost', {}))
        return value

    @property
    def playerInscriptionCost(self):
        value = self.__proxy.playerInscriptionCost.copy()
        value.update(self.getValue('playerInscriptionCost', {}))
        return value

    @property
    def playerEmblemCost(self):
        value = self.__proxy.playerEmblemCost.copy()
        value.update(self.getValue('playerEmblemCost', {}))
        return value
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\utils\requesters\ShopRequester.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:30 St�edn� Evropa (letn� �as)
