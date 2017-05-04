# 2017.05.04 15:26:22 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/tooltips/__init__.py
import weakref
import sys
from shared_utils import CONST_CONTAINER
from debug_utils import LOG_CURRENT_EXCEPTION
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.app_loader.decorators import sf_lobby
from gui.shared import g_itemsCache
from gui.shared.formatters import icons
from helpers.i18n import makeString
from items import vehicles

class TOOLTIP_TYPE(CONST_CONTAINER):
    VEHICLE = 'vehicle'
    TANKMAN = 'tankman'
    SKILL = 'skill'
    ACHIEVEMENT = 'achievement'
    ACHIEVEMENT_ATTR = 'achievementAttr'
    MODULE = 'module'
    SHELL = 'shell'
    EQUIPMENT = 'equipment'
    EFFICIENCY = 'efficiency'
    FORTIFICATIONS = 'fortification'
    IGR = 'igr'
    CYBER_SPORT = 'cyberSport'
    MAP = 'map'
    CONTROL = 'control'
    REF_SYSTEM = 'refSystem'
    PRIVATE_QUESTS = 'privateQuests'
    CONTACT = 'contact'
    QUESTS = 'quests'
    HANGAR_TUTORIAL = 'hangarTutorial'
    CLAN_PROFILE = 'clanProfile'
    TECH_CUSTOMIZATION = 'techCustomization'
    TECH_CUSTOMIZATION_BONUS = 'techCustomizationBonus'
    BOOSTER = 'booster'
    VEHICLE_FILTER = 'vehicleFilter'
    VEH_CMP_CUSTOMIZATION = 'vehCmpCustomization'
    RESERVE = 'reserve'


class TOOLTIP_COMPONENT(CONST_CONTAINER):
    TECH_MAIN = 'technical_maintenance'
    HANGAR = 'hangar'
    SHOP = 'shop'
    INVENTORY = 'inventory'
    PERSONAL_CASE = 'personal_case'
    CAROUSEL = 'carousel'
    RESEARCH = 'research'
    PROFILE = 'profile'
    PROFILE_VEHICLE = 'profileVehicle'
    FINAL_STATISTIC = 'FinalStatistic'
    CYBER_SPORT_UNIT = 'CyberSportUnit'
    FORTIFICATIONS = 'fortification'
    CLAN_PROFILE = 'clanProfile'
    SETTINGS = 'settings'
    CUSTOMIZATION = 'customization'
    CONTACT = 'contact'
    HANGAR_TUTORIAL = 'hangarTutorial'
    TECH_CUSTOMIZATION = 'techCustomization'
    BOOSTER = 'booster'
    RESERVE = 'reserve'


class ACTION_TOOLTIPS_TYPE(CONST_CONTAINER):
    ECONOMICS = 'economics'
    ITEM = 'item'
    BOOSTER = 'booster'
    CAMOUFLAGE = 'camouflage'
    EMBLEMS = 'emblems'
    AMMO = 'ammo'
    RENT = 'rent'


class ACTION_TOOLTIPS_STATE(CONST_CONTAINER):
    DISCOUNT = 'discount'
    PENALTY = 'penalty'


class ToolTipBaseData(object):

    def __init__(self, context, toolTipType):
        self._context = context
        self._toolTipType = toolTipType

    @sf_lobby
    def app(self):
        return None

    @property
    def context(self):
        return self._context

    def getDisplayableData(self, *args, **kwargs):
        return None

    def buildToolTip(self, *args, **kwargs):
        return {'type': self.getType(),
         'component': self.context.getComponent(),
         'data': self.getDisplayableData(*args, **kwargs)}

    def getType(self):
        return self._toolTipType


class ToolTipData(ToolTipBaseData):

    def __init__(self, context, toolTipType):
        super(ToolTipData, self).__init__(context, toolTipType)
        self.item = None
        self.fields = tuple()
        return

    def getDisplayableData(self, *args, **kwargs):
        self.item = self.context.buildItem(*args, **kwargs)
        result = dict()
        for field in self.fields:
            key, value = field.buildData()
            if field.isAvailable and key not in self.context.fieldsToExclude:
                result[key] = value

        return result


class ToolTipDataField(object):

    def __init__(self, tooltip, name):
        self._tooltip = weakref.proxy(tooltip)
        self._name = name
        self._isAvailable = True

    def buildData(self):
        return (self._name, self._getValue())

    @property
    def isAvailable(self):
        return self._isAvailable

    def _getValue(self):
        return None


class ToolTipAttrField(ToolTipDataField):

    def __init__(self, context, name, attr = None):
        super(ToolTipAttrField, self).__init__(context, name)
        self._attr = attr

    def _getItem(self):
        return self._tooltip.item

    def _getValue(self):
        attr = self._attr or self._name
        item = self._getItem()
        if hasattr(item, attr):
            return getattr(item, attr)
        return super(ToolTipAttrField, self)._getValue()


class ToolTipMethodField(ToolTipDataField):

    def __init__(self, context, name, method = None, args = None):
        super(ToolTipMethodField, self).__init__(context, name)
        self._method = method
        self._args = args or tuple()

    def _getItem(self):
        return self._tooltip.item

    def _getValue(self):
        attr = self._method or self._name
        item = self._getItem()
        if hasattr(item, attr):
            return getattr(item, attr)(*self._args)
        return super(ToolTipMethodField, self)._getValue()


class ToolTipAttrCheckField(ToolTipAttrField):

    def __init__(self, context, name, value, attr = None):
        super(ToolTipAttrCheckField, self).__init__(context, name, attr)
        self._value = value

    def _getValue(self):
        return super(ToolTipAttrCheckField, self)._getValue() == self._value


class ToolTipMethodCheckField(ToolTipMethodField):

    def __init__(self, context, name, value, method = None, args = None):
        super(ToolTipMethodCheckField, self).__init__(context, name, method, args)
        self._value = value

    def _getValue(self):
        return super(ToolTipMethodCheckField, self)._getValue() == self._value


class ToolTipParameterField(ToolTipDataField):

    def _getParameterValue(self, *args):
        return None


def getComplexStatus(statusKey, **kwargs):
    try:
        if not statusKey:
            return (None, None)
        headerKey = statusKey + '/header'
        textKey = statusKey + '/text'
        header = makeString(headerKey, **kwargs)
        text = makeString(textKey, **kwargs)
        if headerKey == TOOLTIPS.VEHICLESTATUS_INPREMIUMIGRONLY_HEADER:
            icon = icons.premiumIgrSmall()
            header = makeString(headerKey, icon=icon)
        if header == headerKey.split(':', 1)[1]:
            header = None
        if text == textKey.split(':', 1)[1]:
            text = None
        return (header, text)
    except Exception:
        LOG_CURRENT_EXCEPTION()
        return (None, None)

    return


def getUnlockPrice(compactDescr, parentCD = None):
    item_type_id, _, _ = vehicles.parseIntCompactDescr(compactDescr)
    freeXP = g_itemsCache.items.stats.actualFreeXP
    unlocks = g_itemsCache.items.stats.unlocks
    xpVehs = g_itemsCache.items.stats.vehiclesXPs
    g_techTreeDP.load()
    pricesDict = g_techTreeDP.getUnlockPrices(compactDescr)

    def getUnlockProps(isAvailable, vehCompDescr):
        unlockPrice = pricesDict.get(vehCompDescr, 0)
        pVehXp = xpVehs.get(vehCompDescr, 0)
        need = unlockPrice - pVehXp
        needWithFreeXP = need - freeXP
        return (isAvailable, unlockPrice, min(need, needWithFreeXP))

    if item_type_id == vehicles._VEHICLE:
        isAvailable, props = g_techTreeDP.isNext2Unlock(compactDescr, unlocks, xpVehs, freeXP)
        if parentCD is not None:
            return getUnlockProps(isAvailable, parentCD)
        return getUnlockProps(isAvailable, props.parentID)
    else:
        isAvailable = compactDescr in unlocks
        if not pricesDict:
            return (isAvailable, 0, 0)
        if parentCD is not None:
            return getUnlockProps(isAvailable, parentCD)
        vehsCompDescrs = [ compDescr for compDescr in pricesDict.keys() if compDescr in unlocks ]
        if not vehsCompDescrs:
            vehsCompDescrs = pricesDict.keys()
        minUnlockPrice = sys.maxint
        minUnlockPriceVehCD = None
        for vcd in vehsCompDescrs:
            if pricesDict[vcd] <= minUnlockPrice:
                minUnlockPrice = pricesDict[vcd]
                minUnlockPriceVehCD = vcd

        if minUnlockPriceVehCD is None:
            return (isAvailable, 0, 0)
        return getUnlockProps(isAvailable, minUnlockPriceVehCD)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\tooltips\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:22 St�edn� Evropa (letn� �as)
