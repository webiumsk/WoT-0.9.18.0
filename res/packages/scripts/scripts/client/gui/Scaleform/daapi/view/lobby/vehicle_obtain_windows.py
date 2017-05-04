# 2017.05.04 15:22:57 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_obtain_windows.py
import constants
from debug_utils import LOG_ERROR
from gui import SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.DialogsInterface import showI18nConfirmDialog
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta, DIALOG_BUTTON_ID
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleVO
from gui.Scaleform.daapi.view.meta.VehicleBuyWindowMeta import VehicleBuyWindowMeta
from gui.Scaleform.locale.DIALOGS import DIALOGS
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.shared import g_itemsCache
from gui.shared.events import VehicleBuyEvent
from gui.shared.formatters import text_styles, moneyWithIcon
from gui.shared.formatters.text_styles import neutral
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.processors.vehicle import VehicleBuyer, VehicleSlotBuyer, VehicleRenter, VehicleRestoreProcessor, VehicleTradeInProcessor
from gui.shared.money import Money, ZERO_MONEY, Currency
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE
from gui.shared.tooltips.formatters import packActionTooltipData
from gui.shared.tooltips.formatters import packItemActionTooltipData, packItemRentActionTooltipData
from gui.shared.utils import decorators
from helpers import i18n, time_utils, dependency
from shared_utils import CONST_CONTAINER
from skeletons.gui.game_control import IRentalsController, ITradeInController, IRestoreController

class _TABS(CONST_CONTAINER):
    UNDEFINED = -1
    BUY = 0
    TRADE = 1


class VehicleBuyWindow(VehicleBuyWindowMeta):
    rentals = dependency.descriptor(IRentalsController)
    tradeIn = dependency.descriptor(ITradeInController)

    def __init__(self, ctx = None):
        super(VehicleBuyWindow, self).__init__()
        self.nationID = ctx.get('nationID')
        self.inNationID = ctx.get('itemID')
        self.vehicle = None
        self.tradeOffVehicle = None
        if ctx.get('isTradeIn', False):
            self.selectedTab = _TABS.TRADE
        else:
            self.selectedTab = _TABS.UNDEFINED
        return

    def onWindowClose(self):
        self.destroy()

    def submit(self, data):
        self.__requestForMoneyObtain(data)

    def onTradeInClearVehicle(self):
        self.tradeOffVehicle = None
        self.as_setTradeInWarningMessagegeS('')
        return

    def selectTab(self, tabIndex):
        self.selectedTab = tabIndex

    def _populate(self):
        super(VehicleBuyWindow, self)._populate()
        self._initData()
        g_itemsCache.onSyncCompleted += self._initData
        self.rentals.onRentChangeNotify += self.__onRentChange
        g_clientUpdateManager.addCallbacks({'stats.credits': self.__setCreditsCallBack,
         'stats.gold': self.__setGoldCallBack})
        self.addListener(VehicleBuyEvent.VEHICLE_SELECTED, self.__setTradeOffVehicle)

    def _dispose(self):
        g_itemsCache.onSyncCompleted -= self._initData
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.rentals.onRentChangeNotify -= self.__onRentChange
        self.removeListener(VehicleBuyEvent.VEHICLE_SELECTED, self.__setTradeOffVehicle)
        self.vehicle = None
        self.tradeOffVehicle = None
        super(VehicleBuyWindow, self)._dispose()
        return

    def _getGuiFields(self, vehicle):
        return {'title': i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_TITLE, vehiclename=vehicle.userName),
         'submitBtnLabel': i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_SUBMITBTN),
         'cancelBtnLabel': i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_CANCELBTN)}

    def _isTradeIn(self):
        return self.tradeIn.isEnabled() and self.vehicle.canTradeIn

    def __getTradeInGuiFields(self, vehicle):
        return {'tradeInTitle': i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_TRADEIN_TITLE, vehiclename=vehicle.userName),
         'tradeInSubmitBtnLabel': i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_TRADEIN_SUBMITBTN),
         'tradeInCancelBtnLabel': i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_TRADEIN_CANCELBTN)}

    def _getContentFields(self, vehicle):
        return {'priceLabel': i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_PRICELABEL, vehiclename=vehicle.shortUserName),
         'crewCheckbox': i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_TANKMENCHECKBOX),
         'warningMsg': i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_WARNING) if constants.IS_KOREA else None}

    def __getTradeInContentFields(self, vehicle):
        if self.selectedTab == _TABS.UNDEFINED:
            if vehicle.mayPurchase(g_itemsCache.items.stats.money)[0]:
                self.selectedTab = _TABS.BUY
            else:
                self.selectedTab = _TABS.TRADE
        return {'tradeInPriceLabel': i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_TRADEIN_PRICELABEL, vehiclename=vehicle.shortUserName),
         'tradeInCrewCheckbox': i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_TRADEIN_TANKMENCHECKBOX),
         'tradeInVehiclePrices': self._getVehiclePrice(vehicle),
         'tradeInVehiclePricesActionData': self._getItemPriceActionData(vehicle),
         'tradeInStudyLabel': i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_TRADEIN_STUDYLABEL, count=text_styles.stats(str(len(vehicle.crew)))),
         'hasTradeOffVehicles': self.tradeIn.getTradeInInfo(vehicle) is not None,
         'selectedTab': self.selectedTab}

    def _isSubmitBtnEnabled(self, vehicle):
        if vehicle.isPurchased:
            return False
        money = g_itemsCache.items.stats.money
        canBuy, _ = vehicle.mayObtainForMoney(money)
        return canBuy

    def _initData(self, *args):
        stats = g_itemsCache.items.stats
        self.as_setGoldS(stats.gold)
        self.as_setCreditsS(stats.credits)
        self.vehicle = g_itemsCache.items.getItem(GUI_ITEM_TYPE.VEHICLE, self.nationID, self.inNationID)
        self.as_setEnabledSubmitBtnS(self._isSubmitBtnEnabled(self.vehicle))
        if self.vehicle is None:
            LOG_ERROR("Vehicle Item mustn't be None!", 'NationID:', self.nationID, 'InNationID:', self.inNationID)
        elif self.vehicle.isInInventory and not self.vehicle.isRented:
            self.onWindowClose()
        else:
            isTradeIn = self._isTradeIn()
            initData = {'headerData': self._getOptainHeaderData(self.vehicle),
             'isTradeIn': isTradeIn,
             'contentData': self._getByuContentData(self.vehicle, stats, isTradeIn)}
            initData.update(self._getGuiFields(self.vehicle))
            if isTradeIn:
                initData.update(self.__getTradeInGuiFields(self.vehicle))
            self.as_setInitDataS(initData)
        return

    def _getOptainHeaderData(self, vehicle):
        from helpers import int2roman
        from helpers.i18n import makeString as _ms
        from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
        levelStr = text_styles.concatStylesWithSpace(text_styles.stats(int2roman(vehicle.level)), text_styles.main(_ms(DIALOGS.VEHICLESELLDIALOG_VEHICLE_LEVEL)))
        if vehicle.isElite:
            description = TOOLTIPS.tankcaruseltooltip_vehicletype_elite(vehicle.type)
        else:
            description = DIALOGS.vehicleselldialog_vehicletype(vehicle.type)
        return {'userName': vehicle.userName,
         'levelStr': levelStr,
         'description': description,
         'intCD': vehicle.intCD,
         'icon': vehicle.icon,
         'level': vehicle.level,
         'isElite': vehicle.isElite,
         'isPremium': vehicle.isPremium,
         'type': vehicle.type,
         'nationID': self.nationID}

    def _getByuContentData(self, vehicle, stats, isTradeIn):
        shop = g_itemsCache.items.shop
        shopDefaults = shop.defaults
        tankMenCount = len(vehicle.crew)
        vehiclePricesActionData = self._getItemPriceActionData(vehicle)
        ammoPrice = ZERO_MONEY
        defAmmoPrice = ZERO_MONEY
        for shell in vehicle.gun.defaultAmmo:
            ammoPrice += shell.buyPrice * shell.defaultCount
            defAmmoPrice += shell.defaultPrice * shell.defaultCount

        ammoActionPriceData = None
        if ammoPrice != defAmmoPrice:
            ammoActionPriceData = packActionTooltipData(ACTION_TOOLTIPS_TYPE.AMMO, str(vehicle.intCD), True, ammoPrice, defAmmoPrice)
        slotPrice = shop.getVehicleSlotsPrice(stats.vehicleSlots)
        slotDefaultPrice = shopDefaults.getVehicleSlotsPrice(stats.vehicleSlots)
        slotActionPriceData = None
        if slotPrice != slotDefaultPrice:
            slotActionPriceData = packActionTooltipData(ACTION_TOOLTIPS_TYPE.ECONOMICS, 'slotsPrices', True, Money(gold=slotPrice), Money(gold=slotDefaultPrice))
        tankmenTotalLabel = i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_TANKMENTOTALLABEL, count=str(tankMenCount))
        studyData = []
        for index, (tCost, defTCost, typeID) in enumerate(zip(shop.tankmanCostWithGoodyDiscount, shopDefaults.tankmanCost, ('free', 'school', 'academy'))):
            if tCost['isPremium']:
                currency = Currency.GOLD
            else:
                currency = Currency.CREDITS
            price = tCost[currency] * tankMenCount
            defPrice = defTCost[currency] * tankMenCount
            totalPrice = Money.makeFrom(currency, price)
            totalDefPrice = Money.makeFrom(currency, defPrice)
            if typeID is 'free':
                formatedPrice = i18n.makeString(MENU.TANKMANTRAININGWINDOW_FREE_PRICE)
            else:
                formatedPrice = moneyWithIcon(totalPrice, currType=currency)
            studyPriceActionData = None
            if price != defPrice:
                studyPriceActionData = packActionTooltipData(ACTION_TOOLTIPS_TYPE.ECONOMICS, '%sTankmanCost' % currency, True, totalPrice, totalDefPrice)
            studyData.insert(0, {'id': typeID,
             'price': price,
             'crewType': index,
             'actionPrice': studyPriceActionData,
             'label': '%d%% - %s' % (tCost['roleLevel'], formatedPrice)})

        initData = {'tankmenTotalLabel': tankmenTotalLabel,
         'vehiclePrices': self._getVehiclePrice(vehicle),
         'vehiclePricesActionData': vehiclePricesActionData,
         'isRentable': vehicle.isRentable,
         'rentDataDD': self._getRentData(vehicle, vehiclePricesActionData),
         'ammoPrice': ammoPrice.credits,
         'ammoActionPriceData': ammoActionPriceData,
         'slotPrice': slotPrice,
         'slotActionPriceData': slotActionPriceData,
         'isStudyDisabled': vehicle.hasCrew,
         'isNoAmmo': not vehicle.hasShells,
         'studyData': studyData,
         'nation': self.nationID}
        initData.update(self._getContentFields(vehicle))
        if isTradeIn:
            initData.update(self.__getTradeInContentFields(vehicle))
        return initData

    def _getVehiclePrice(self, vehicle):
        return vehicle.buyPrice

    def _getItemPriceActionData(self, vehicle):
        if vehicle.buyPrice != vehicle.defaultPrice:
            return packItemActionTooltipData(vehicle)
        else:
            return None

    def _getRentData(self, vehicle, vehiclePricesActionData):
        result = []
        rentPackages = vehicle.rentPackages
        for rentPackage in rentPackages:
            days = rentPackage['days']
            actionRentPrice = None
            if rentPackage['rentPrice'] != rentPackage['defaultRentPrice']:
                actionRentPrice = packItemRentActionTooltipData(vehicle, rentPackage)
            result.append({'itemId': days,
             'label': i18n.makeString(MENU.SHOP_MENU_VEHICLE_RENT_DAYS, days=days),
             'price': rentPackage['rentPrice'],
             'enabled': vehicle.maxRentDuration - vehicle.rentLeftTime >= days * time_utils.ONE_DAY,
             'actionPrice': actionRentPrice})

        result = self._addPriceBlock(result, vehicle, vehiclePricesActionData)
        selectedId = -1
        for ddItem in result:
            if ddItem['enabled']:
                selectedId = ddItem['itemId']
                break

        return {'data': result,
         'selectedId': selectedId}

    def _addPriceBlock(self, result, vehicle, vehiclePricesActionData):
        result.append({'itemId': -1,
         'label': i18n.makeString(MENU.SHOP_MENU_VEHICLE_RENT_FOREVER),
         'price': vehicle.buyPrice,
         'enabled': not vehicle.isDisabledForBuy and not vehicle.isHidden,
         'actionPrice': vehiclePricesActionData})
        return result

    def _getObtainVehicleProcessor(self, vehicle, data):
        return VehicleBuyer(vehicle, data.buySlot, data.buyAmmo, data.crewType)

    def __onRentChange(self, vehicles):
        vehicle = g_itemsCache.items.getItem(GUI_ITEM_TYPE.VEHICLE, self.nationID, self.inNationID)
        if vehicle and vehicle.intCD in vehicles:
            self._initData()

    @decorators.process('buyItem')
    def __requestForMoneyObtain(self, data):
        isTradeIn = data.tradeOff != -1
        if isTradeIn:
            tradeOffVehicle = g_itemsCache.items.getItemByCD(int(data.tradeOff))
            confirmationType = 'tradeInConfirmation'
            addition = ''
            operations = []
            if tradeOffVehicle.hasCrew:
                operations.append('crew')
            if tradeOffVehicle.hasShells:
                operations.append('shells')
            if tradeOffVehicle.hasEquipments:
                operations.append('equipments')
            if tradeOffVehicle.hasOptionalDevices:
                operations.append('optionalDevices')
            if operations:
                operationsStr = map(lambda o: i18n.makeString('#dialogs:%s/message/%s' % (confirmationType, o)), operations)
                addition = i18n.makeString('#dialogs:%s/message/addition' % confirmationType, operations=', '.join(operationsStr))
            ctx = {'vehName': neutral(tradeOffVehicle.userName),
             'addition': addition}
            result = yield showI18nConfirmDialog(confirmationType, meta=I18nConfirmDialogMeta(confirmationType, ctx, ctx), focusedID=DIALOG_BUTTON_ID.SUBMIT)
            if not result:
                return
            tradeOffVehicle = g_itemsCache.items.getItemByCD(int(data.tradeOff))
            result = yield VehicleTradeInProcessor(self.vehicle, tradeOffVehicle, data.buySlot, data.buyAmmo, data.crewType).request()
            if len(result.userMsg):
                SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)
            if not result.success:
                self.onWindowClose()
                return
        if data.buySlot:
            result = yield VehicleSlotBuyer(showConfirm=False, showWarning=False).request()
            if len(result.userMsg):
                SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)
            if not result.success:
                return
        if not isTradeIn:
            if data.rentId != -1:
                result = yield VehicleRenter(self.vehicle, data.rentId, data.buyAmmo, data.crewType).request()
            else:
                result = yield self._getObtainVehicleProcessor(self.vehicle, data).request()
            if len(result.userMsg):
                SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)
        self.onWindowClose()

    def __setGoldCallBack(self, gold):
        self.as_setGoldS(gold)

    def __setCreditsCallBack(self, credits):
        self.as_setCreditsS(credits)

    def __setTradeOffVehicle(self, event):
        selectedVehCD = int(event.ctx)
        self.tradeOffVehicle = g_itemsCache.items.getItemByCD(selectedVehCD)
        tradeOffVehicleHtml = moneyWithIcon(self.tradeOffVehicle.tradeOffPrice, currType=Currency.GOLD)
        tradeOffVehicleStatus = i18n.makeString(DIALOGS.BUYVEHICLEWINDOW_TRADEIN_INFO_SAVING, cost=tradeOffVehicleHtml)
        tradeOffVehicleVo = makeVehicleVO(self.tradeOffVehicle)
        tradeOffVehicleVo['actionPrice'] = self._getItemPriceActionData(self.tradeOffVehicle)
        tradeOffData = {'vehicleVo': tradeOffVehicleVo,
         'price': self.tradeOffVehicle.tradeOffPrice.gold,
         'status': tradeOffVehicleStatus}
        self.as_updateTradeOffVehicleS(tradeOffData)
        self.as_setTradeInWarningMessagegeS(i18n.makeString(DIALOGS.TRADEINCONFIRMATION_MESSAGE, vehName=self.tradeOffVehicle.userName, addition=''))


class VehicleRestoreWindow(VehicleBuyWindow):
    restore = dependency.descriptor(IRestoreController)

    def submit(self, data):
        super(VehicleRestoreWindow, self).submit(data)

    def _populate(self):
        super(VehicleRestoreWindow, self)._populate()
        self.restore.onRestoreChangeNotify += self.__onRestoreChange

    def _dispose(self):
        super(VehicleRestoreWindow, self)._dispose()
        self.restore.onRestoreChangeNotify -= self.__onRestoreChange

    def _addPriceBlock(self, result, vehicle, vehiclePricesActionData):
        disabled = not vehicle.isRestoreAvailable() or constants.IS_CHINA and vehicle.rentalIsActive
        result.insert(0, {'itemId': -1,
         'label': i18n.makeString(MENU.SHOP_MENU_VEHICLE_RESTORE),
         'price': vehicle.restorePrice,
         'enabled': not disabled,
         'actionPrice': vehiclePricesActionData})
        return result

    def _getObtainVehicleProcessor(self, vehicle, data):
        return VehicleRestoreProcessor(vehicle, data.buySlot, data.buyAmmo, data.crewType)

    def _getVehiclePrice(self, vehicle):
        return vehicle.restorePrice

    def _getItemPriceActionData(self, vehicle):
        return None

    def _getGuiFields(self, vehicle):
        return {'title': i18n.makeString(DIALOGS.RESTOREVEHICLEDIALOG_TITLE, vehiclename=vehicle.userName),
         'cancelBtnLabel': i18n.makeString(DIALOGS.RESTOREVEHICLEDIALOG_CANCELBTN),
         'submitBtnLabel': i18n.makeString(DIALOGS.RESTOREVEHICLEDIALOG_SUBMITBTN)}

    def _getContentFields(self, vehicle):
        return {'priceLabel': i18n.makeString(DIALOGS.RESTOREVEHICLEDIALOG_PRICELABEL, vehiclename=vehicle.userName),
         'crewCheckbox': i18n.makeString(DIALOGS.RESTOREVEHICLEDIALOG_TANKMENCHECKBOX),
         'warningMsg': i18n.makeString(DIALOGS.RESTOREVEHICLEDIALOG_WARNING) if constants.IS_KOREA else None}

    def _isTradeIn(self):
        return False

    def __onRestoreChange(self, _):
        vehicle = g_itemsCache.items.getItem(GUI_ITEM_TYPE.VEHICLE, self.nationID, self.inNationID)
        if vehicle and not vehicle.isRestoreAvailable():
            self.onWindowClose()
            SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.VEHICLE_RESTORE_FINISHED, vehicleName=vehicle.userName)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\vehicle_obtain_windows.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:58 St�edn� Evropa (letn� �as)
