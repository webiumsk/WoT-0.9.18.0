# 2017.05.04 15:26:04 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/processors/module.py
import BigWorld
import AccountCommands
from gui import makeHtmlString
from gui.shared.gui_items.vehicle_modules import VehicleTurret, VehicleGun
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE, ACTION_TOOLTIPS_STATE
from debug_utils import LOG_DEBUG
from gui.SystemMessages import SM_TYPE
from gui.shared import g_itemsCache
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.processors import ItemProcessor, makeI18nSuccess, makeI18nError, VehicleItemProcessor, plugins, makeSuccess
from gui.shared.formatters import formatPrice
from gui.shared.money import Money
from gui.shared.tooltips.formatters import packActionTooltipData
from gui.shared.utils.requesters.ItemsRequester import ItemsRequester
from helpers import i18n

class ModuleProcessor(ItemProcessor):
    """
    Root module processor
    """
    ITEMS_MSG_PREFIXES = {GUI_ITEM_TYPE.SHELL: 'shell',
     GUI_ITEM_TYPE.EQUIPMENT: 'artefact',
     GUI_ITEM_TYPE.OPTIONALDEVICE: 'artefact'}
    DEFAULT_PREFIX = 'module'

    def __init__(self, item, opType, plugs = tuple()):
        """
        Ctor.
        
        @param item: module to install
        @param opType: operation type
        @param plugs: plugins list
        """
        ItemProcessor.__init__(self, item, plugs + (plugins.ModuleValidator(item),))
        self.opType = opType

    def _getMsgCtx(self):
        raise NotImplemented

    def _formMessage(self, msg):
        LOG_DEBUG('Generating response for ModuleProcessor: ', self.opType, msg)
        return '%(itemType)s_%(opType)s/%(msg)s' % {'itemType': self.ITEMS_MSG_PREFIXES.get(self.item.itemTypeID, self.DEFAULT_PREFIX),
         'opType': self.opType,
         'msg': msg}

    def _errorHandler(self, code, errStr = '', ctx = None):
        if not len(errStr):
            if code != AccountCommands.RES_CENTER_DISCONNECTED:
                msg = 'server_error'
            else:
                msg = 'server_error_centerDown'
        else:
            msg = errStr
        return makeI18nError(self._formMessage(msg), defaultSysMsgKey=self._formMessage('server_error'), **self._getMsgCtx())


class ModuleTradeProcessor(ModuleProcessor):
    """
    Root module trade
    """

    def __init__(self, item, count, opType, plugs = tuple()):
        """
        Ctor.
        
        @param item: module to install
        @param count: buying count
        @param opType: operation type
        @param plugs: plugins list
        """
        super(ModuleTradeProcessor, self).__init__(item, opType, plugs)
        self.count = count

    def _getMsgCtx(self):
        return {'name': self.item.userName,
         'kind': self.item.userType,
         'count': BigWorld.wg_getIntegralFormat(int(self.count)),
         'money': formatPrice(self._getOpPrice())}

    def _getOpPrice(self):
        """
        @return Returns an instance of Money
        """
        raise NotImplemented


class ModuleBuyer(ModuleTradeProcessor):
    """
    Module buyer
    """

    def __init__(self, item, count, buyForCredits):
        """
        Ctor.
        
        @param item: module to install
        @param count: buying count
        @param buyForCredits: buy gold item for credits
        """
        super(ModuleBuyer, self).__init__(item, count, 'buy')
        self.buyForCredits = buyForCredits
        self.addPlugins((plugins.MoneyValidator(self._getOpPrice()),))

    def _isItemBuyingForCredits(self):
        if self.buyForCredits:
            shop = g_itemsCache.items.shop
            if self.item.itemTypeID == GUI_ITEM_TYPE.SHELL and shop.isEnabledBuyingGoldShellsForCredits:
                return True
            if self.item.itemTypeID == GUI_ITEM_TYPE.EQUIPMENT and shop.isEnabledBuyingGoldEqsForCredits:
                return True
        return False

    def _getOpPrice(self):
        price = self.item.altPrice or self.item.buyPrice
        if self.buyForCredits:
            return self.count * Money(credits=price.credits)
        return self.count * Money(gold=price.gold)

    def _successHandler(self, code, ctx = None):
        sysMsgType = SM_TYPE.PurchaseForCredits if self.buyForCredits else SM_TYPE.PurchaseForGold
        return makeI18nSuccess(self._formMessage('success'), type=sysMsgType, **self._getMsgCtx())

    def _request(self, callback):
        LOG_DEBUG('Make server request to buy module', self.item, self.count, self._isItemBuyingForCredits())
        BigWorld.player().shop.buy(self.item.itemTypeID, self.item.nationID, self.item.intCD, self.count, int(self._isItemBuyingForCredits()), lambda code: self._response(code, callback))


class ModuleSeller(ModuleTradeProcessor):
    """
    Module seller
    """

    def __init__(self, item, count):
        """
        Ctor.
        
        @param item: module to install
        @param count: module buying count
        """
        super(ModuleSeller, self).__init__(item, count, 'sell')

    def _getOpPrice(self):
        return self.item.sellPrice * self.count

    def _successHandler(self, code, ctx = None):
        return makeI18nSuccess(self._formMessage('success'), type=SM_TYPE.Selling, **self._getMsgCtx())

    def _request(self, callback):
        LOG_DEBUG('Make server request to sell item', self.item, self.count)
        BigWorld.player().inventory.sell(self.item.itemTypeID, self.item.intCompactDescr, self.count, lambda code: self._response(code, callback))


class ModuleInstallProcessor(ModuleProcessor, VehicleItemProcessor):
    """
    Root modules installer.
    """

    def __init__(self, vehicle, item, itemType, slotIdx, install = True, conflictedEqs = None, plugs = tuple()):
        """
        Ctor.
        
        @param vehicle: vehicle
        @param item: module to install
        @param slotIdx: vehicle equipment slot index to install
        @param itemType: item type
        @param install: flag to designated process
        @param conflictedEqs: conflicted items
        @param plugs: plugins list
        """
        opType = 'apply' if install else 'remove'
        conflictedEqs = conflictedEqs or tuple()
        ModuleProcessor.__init__(self, item=item, opType=opType, plugs=plugs)
        VehicleItemProcessor.__init__(self, vehicle=vehicle, module=item, allowableTypes=itemType)
        addPlugins = []
        if install:
            addPlugins += (plugins.CompatibilityInstallValidator(vehicle, item, slotIdx), plugins.MessageConfirmator('removeIncompatibleEqs', ctx={'name': "', '".join([ eq.userName for eq in conflictedEqs ])}, isEnabled=bool(conflictedEqs)))
        else:
            addPlugins += (plugins.CompatibilityRemoveValidator(vehicle, item),)
        self.install = install
        self.slotIdx = slotIdx
        self.addPlugins(addPlugins)

    def _getMsgCtx(self):
        return {'name': self.item.userName,
         'kind': self.item.userType}

    def _successHandler(self, code, ctx = None):
        return makeI18nSuccess(self._formMessage('success'), type=SM_TYPE.Information, **self._getMsgCtx())


class OptDeviceInstaller(ModuleInstallProcessor):
    """
    Vehicle opt devices installer.
    """

    def __init__(self, vehicle, item, slotIdx, install = True, isUseGold = False, conflictedEqs = None):
        """
        Ctor.
        
        @param vehicle: vehicle
        @param item: module to install
        @param slotIdx: vehicle equipment slot index to install
        @param install: flag to designated process
        @param conflictedEqs: conflicted items
        """
        super(OptDeviceInstaller, self).__init__(vehicle, item, (GUI_ITEM_TYPE.OPTIONALDEVICE,), slotIdx, install, conflictedEqs)
        self.cost = g_itemsCache.items.shop.paidRemovalCost
        defaultCost = g_itemsCache.items.shop.defaults.paidRemovalCost
        action = None
        if self.cost != defaultCost:
            action = packActionTooltipData(ACTION_TOOLTIPS_TYPE.ECONOMICS, 'paidRemovalCost', True, Money(gold=self.cost), Money(gold=defaultCost))
        addPlugins = []
        if install:
            addPlugins += (plugins.MessageConfirmator('installConfirmationNotRemovable', ctx={'name': item.userName}, isEnabled=not item.isRemovable),)
        else:
            addPlugins += (plugins.DemountDeviceConfirmator('removeConfirmationNotRemovableGold', ctx={'name': item.userName,
              'price': self.cost,
              'action': action}, isEnabled=not item.isRemovable and isUseGold), plugins.DestroyDeviceConfirmator('removeConfirmationNotRemovable', itemName=item.userName, isEnabled=not item.isRemovable and not isUseGold))
        self.addPlugins(addPlugins)
        self.useGold = isUseGold
        return

    def _successHandler(self, code, ctx = None):
        item = self.item if self.install else None
        self.vehicle.optDevices[self.slotIdx] = item
        if not self.install and not self.item.isRemovable and self.useGold:
            return makeI18nSuccess(self._formMessage('gold_success'), type=SM_TYPE.DismantlingForGold, **self._getMsgCtx())
        else:
            return super(OptDeviceInstaller, self)._successHandler(code, ctx)

    def _request(self, callback):
        itemCD = self.item.intCD if self.install else 0
        BigWorld.player().inventory.equipOptionalDevice(self.vehicle.invID, itemCD, self.slotIdx, self.useGold, lambda code: self._response(code, callback))

    def _getMsgCtx(self):
        return {'name': self.item.userName,
         'kind': self.item.userType,
         'money': self.cost}


class EquipmentInstaller(ModuleInstallProcessor):
    """
    Vehicle equipment installer.
    """

    def __init__(self, vehicle, item, slotIdx, install = True, conflictedEqs = None):
        """
        Ctor.
        
        @param vehicle: vehicle
        @param item: equipment to install
        @param slotIdx: vehicle equipment slot index to install
        @param install: flag to designated process
        @param conflictedEqs: conflicted items
        """
        super(EquipmentInstaller, self).__init__(vehicle, item, (GUI_ITEM_TYPE.EQUIPMENT,), slotIdx, install, conflictedEqs)

    def _successHandler(self, code, ctx = None):
        item = self.item if self.install else None
        self.vehicle.eqs[self.slotIdx] = item
        return super(EquipmentInstaller, self)._successHandler(code, ctx)

    def _request(self, callback):
        itemCD = self.item.intCD if self.install else 0
        newEqsLayout = map(lambda item: (item.intCD if item is not None else 0), self.vehicle.eqs)
        newEqsLayout[self.slotIdx] = itemCD
        BigWorld.player().inventory.equipEquipments(self.vehicle.invID, newEqsLayout, lambda code: self._response(code, callback))


class CommonModuleInstallProcessor(ModuleProcessor, VehicleItemProcessor):
    """
    Vehicle other modules installer.
    """

    def __init__(self, vehicle, item, itemType, install = True, conflictedEqs = None, plugs = tuple()):
        """
        Ctor.
        
        @param vehicle: vehicle
        @param item: equipment to install
        @param itemType: vehicle module type
        @param install: flag to designated process
        @param conflictedEqs: conflicted items
        @param plugs: plugins list
        """
        opType = 'apply' if install else 'remove'
        conflictedEqs = conflictedEqs or tuple()
        ModuleProcessor.__init__(self, item=item, opType=opType, plugs=plugs)
        VehicleItemProcessor.__init__(self, vehicle=vehicle, module=item, allowableTypes=itemType)
        if install:
            self.addPlugin(plugins.MessageConfirmator('removeIncompatibleEqs', ctx={'name': "', '".join([ eq.userName for eq in conflictedEqs ])}, isEnabled=bool(conflictedEqs)))
        self.install = install

    def _getMsgCtx(self):
        return {'name': self.item.userName,
         'kind': self.item.userType}

    def _successHandler(self, code, ctx = None):
        additionalMessages = []
        removedItems = []
        for eqKd in ctx.get('incompatibleEqs', []):
            item = g_itemsCache.items.getItemByCD(eqKd)
            removedItems.append(item.name)

        if removedItems:
            additionalMessages.append(makeI18nSuccess(self._formMessage('incompatibleEqs'), items="', '".join(removedItems), type=SM_TYPE.Information))
        additionalMessages.append(makeI18nSuccess(self._formMessage('success'), type=SM_TYPE.Information, auxData=additionalMessages, **self._getMsgCtx()))
        return makeSuccess(auxData=additionalMessages)


class TurretInstaller(CommonModuleInstallProcessor):
    """
    Vehicle turret installer.
    """

    def __init__(self, vehicle, item, conflictedEqs = None):
        """
        Ctor.
        
        @param vehicle: vehicle
        @param item: equipment to install
        @param conflictedEqs: conflicted items
        """
        super(TurretInstaller, self).__init__(vehicle, item, (GUI_ITEM_TYPE.TURRET,), True, conflictedEqs)
        self.gunCD = 0
        mayInstallCurrent = item.mayInstall(vehicle, gunCD=self.gunCD)
        if not mayInstallCurrent[0]:
            self._findAvailableGun(vehicle, item)
        self.addPlugin(plugins.TurretCompatibilityInstallValidator(vehicle, item, self.gunCD))

    def _findAvailableGun(self, vehicle, item):
        for gun in item.descriptor['guns']:
            gunItem = g_itemsCache.items.getItemByCD(gun['compactDescr'])
            if gunItem.isInInventory:
                mayInstall = item.mayInstall(vehicle, slotIdx=0, gunCD=gun['compactDescr'])
                if mayInstall[0]:
                    self.gunCD = gun['compactDescr']
                    break

    def _request(self, callback):
        BigWorld.player().inventory.equipTurret(self.vehicle.invID, self.item.intCD, self.gunCD, lambda code, ext: self._response(code, callback, ctx=ext))

    def _successHandler(self, code, ctx = None):
        if self.gunCD:
            gun = g_itemsCache.items.getItemByCD(self.gunCD)
            return makeI18nSuccess(self._formMessage('success_gun_change'), type=SM_TYPE.Information, gun=gun.userName, **self._getMsgCtx())
        return super(TurretInstaller, self)._successHandler(code, ctx)


class PreviewVehicleTurretInstaller(TurretInstaller):

    def _findAvailableGun(self, vehicle, item):
        for gun in item.descriptor['guns']:
            mayInstall = item.mayInstall(vehicle, slotIdx=0, gunCD=gun['compactDescr'])
            if mayInstall[0]:
                self.gunCD = gun['compactDescr']
                break

    def _request(self, callback):
        vehDescr = self.vehicle.descriptor
        vehDescr.installTurret(self.item.intCD, self.gunCD)
        self.vehicle.turret = VehicleTurret(vehDescr.turret['compactDescr'], descriptor=vehDescr.turret)
        if self.gunCD:
            self.vehicle.descriptor.installComponent(self.gunCD)
            self.vehicle.gun = VehicleGun(self.gunCD, descriptor=self.vehicle.descriptor.gun)
        callback(makeSuccess())


class OtherModuleInstaller(CommonModuleInstallProcessor):
    """
    Vehicle rest modules installer: sheels, fuel tanks, etc.
    """

    def __init__(self, vehicle, item, conflictedEqs = None):
        """
        Ctor.
        
        @param vehicle: vehicle
        @param item: equipment to install
        @param conflictedEqs: conflicted items
        """
        super(OtherModuleInstaller, self).__init__(vehicle, item, (GUI_ITEM_TYPE.CHASSIS,
         GUI_ITEM_TYPE.GUN,
         GUI_ITEM_TYPE.ENGINE,
         GUI_ITEM_TYPE.FUEL_TANK,
         GUI_ITEM_TYPE.RADIO,
         GUI_ITEM_TYPE.SHELL), True, conflictedEqs)
        self.addPlugin(plugins.CompatibilityInstallValidator(vehicle, item, 0))

    def _request(self, callback):
        LOG_DEBUG('Request to equip module', self.vehicle, self.item)
        BigWorld.player().inventory.equip(self.vehicle.invID, self.item.intCD, lambda code, ext: self._response(code, callback, ctx=ext))


class PreviewVehicleModuleInstaller(OtherModuleInstaller):
    OTHER_PREVIEW_MODULES = {GUI_ITEM_TYPE.GUN: 'gun',
     GUI_ITEM_TYPE.CHASSIS: 'chassis',
     GUI_ITEM_TYPE.ENGINE: 'engine',
     GUI_ITEM_TYPE.RADIO: 'radio'}

    def _request(self, callback):
        itemTypeID = self.item.itemTypeID
        moduleName = self.OTHER_PREVIEW_MODULES[itemTypeID]
        cls = ItemsRequester.ITEM_TYPES_MAPPING[itemTypeID]
        self.vehicle.descriptor.installComponent(self.item.intCD)
        itemDescr = getattr(self.vehicle.descriptor, moduleName)
        setattr(self.vehicle, moduleName, cls(itemDescr['compactDescr'], descriptor=itemDescr))
        callback(makeSuccess())


class BuyAndInstallItemProcessor(ModuleBuyer):

    def __init__(self, vehicle, item, slotIdx, gunCompDescr, conflictedEqs = None):
        self.__vehInvID = vehicle.inventoryID
        self.__slotIdx = int(slotIdx)
        self.__gunCompDescr = gunCompDescr
        self.__vehicle = vehicle
        conflictedEqs = conflictedEqs or tuple()
        conflictMsg = ''
        if conflictedEqs:
            self.__makeConflictMsg("', '".join([ eq.userName for eq in conflictedEqs ]))
        self.__mayInstall, installReason = item.mayInstall(vehicle, slotIdx)
        super(BuyAndInstallItemProcessor, self).__init__(item, 1, True)
        self.addPlugins([plugins.ModuleValidator(item)])
        if self.__mayInstall:
            self.addPlugins([plugins.VehicleValidator(vehicle, True, prop={'isBroken': True,
              'isLocked': True}), plugins.CompatibilityInstallValidator(vehicle, item, slotIdx), plugins.ModuleBuyerConfirmator('confirmBuyAndInstall', ctx={'userString': item.userName,
              'typeString': self.item.userType,
              'conflictedEqs': conflictMsg,
              'credits': BigWorld.wg_getIntegralFormat(self._getOpPrice().credits)})])
            if item.itemTypeID == GUI_ITEM_TYPE.TURRET:
                self.addPlugin(plugins.TurretCompatibilityInstallValidator(vehicle, item, self.__gunCompDescr))
            elif item.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE:
                self.addPlugin(plugins.MessageConfirmator('installConfirmationNotRemovable', ctx={'name': item.userName}, isEnabled=not item.isRemovable))
            self.addPlugin(plugins.MessageConfirmator('removeIncompatibleEqs', ctx={'name': "', '".join([ eq.userName for eq in conflictedEqs ])}, isEnabled=bool(conflictedEqs)))
        else:
            self.addPlugins([plugins.ModuleBuyerConfirmator('confirmBuyNotInstall', ctx={'userString': item.userName,
              'typeString': self.item.userType,
              'credits': BigWorld.wg_getIntegralFormat(self._getOpPrice().credits),
              'reason': self.__makeInstallReasonMsg(installReason)})])

    def __makeConflictMsg(self, conflictedText):
        attrs = {'conflicted': conflictedText}
        return makeHtmlString('html_templates:lobby/shop/system_messages', 'conflicted', attrs)

    def __makeInstallReasonMsg(self, installReason):
        reasonTxt = ''
        if installReason is not None:
            reasonTxt = '#menu:moduleFits/' + installReason.replace(' ', '_')
        return i18n.makeString(reasonTxt)

    def _successHandler(self, code, ctx = None):
        if self.__mayInstall:
            LOG_DEBUG('code, ctx', code, ctx)
            if self.item.itemTypeID == GUI_ITEM_TYPE.EQUIPMENT:
                auxData = [makeI18nSuccess(self._formApplyMessage('success'), type=SM_TYPE.Information, **self._getMsgCtx())]
            elif self.item.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE:
                auxData = [makeI18nSuccess(self._formApplyMessage('success'), type=SM_TYPE.Information, **self._getMsgCtx())]
            elif self.item.itemTypeID == GUI_ITEM_TYPE.TURRET:
                if self.__gunCompDescr:
                    gun = g_itemsCache.items.getItemByCD(self.__gunCompDescr)
                    auxData = [makeI18nSuccess(self._formApplyMessage('success_gun_change'), type=SM_TYPE.Information, gun=gun.userName, **self._getMsgCtx())]
                else:
                    auxData = self.__getAdditionalMessages(ctx)
            else:
                auxData = self.__getAdditionalMessages(ctx)
            sysMsgType = SM_TYPE.PurchaseForCredits if self.buyForCredits else SM_TYPE.PurchaseForGold
            return makeI18nSuccess(self._formMessage('success'), auxData=auxData, type=sysMsgType, **self._getMsgCtx())
        else:
            return super(BuyAndInstallItemProcessor, self)._successHandler(code, ctx)

    def __getAdditionalMessages(self, ctx):
        additionalMessages = []
        removedItems = []
        if ctx:
            for eqKd in ctx.get('incompatibleEqs', []):
                item = g_itemsCache.items.getItemByCD(eqKd)
                removedItems.append(item.name)

        if removedItems:
            additionalMessages.append(makeI18nSuccess(self._formApplyMessage('incompatibleEqs'), items="', '".join(removedItems), type=SM_TYPE.Information))
        additionalMessages.append(makeI18nSuccess(self._formApplyMessage('success'), type=SM_TYPE.Information, auxData=additionalMessages, **self._getMsgCtx()))
        return additionalMessages

    def _formApplyMessage(self, msg):
        return '%(itemType)s_%(opType)s/%(msg)s' % {'itemType': self.ITEMS_MSG_PREFIXES.get(self.item.itemTypeID, self.DEFAULT_PREFIX),
         'opType': 'apply',
         'msg': msg}

    def _request(self, callback):
        if self.__mayInstall:
            LOG_DEBUG('Make server request to buyAndInstallModule module', self.__vehInvID, self.item.intCD, self.__slotIdx, self.__gunCompDescr)
            BigWorld.player().shop.buyAndEquipItem(self.__vehInvID, self.item.intCD, self.__slotIdx, False, self.__gunCompDescr, lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr))
        else:
            super(BuyAndInstallItemProcessor, self)._request(callback)


def getInstallerProcessor(vehicle, newComponentItem, slotIdx = 0, install = True, isUseGold = False, conflictedEqs = None):
    """
    Select proper installer by type
    """
    if newComponentItem.itemTypeID == GUI_ITEM_TYPE.EQUIPMENT:
        return EquipmentInstaller(vehicle, newComponentItem, slotIdx, install, conflictedEqs)
    elif newComponentItem.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE:
        return OptDeviceInstaller(vehicle, newComponentItem, slotIdx, install, isUseGold, conflictedEqs)
    elif newComponentItem.itemTypeID == GUI_ITEM_TYPE.TURRET:
        return TurretInstaller(vehicle, newComponentItem, conflictedEqs)
    else:
        return OtherModuleInstaller(vehicle, newComponentItem, conflictedEqs)


def getPreviewInstallerProcessor(vehicle, newComponentItem, conflictedEqs = None):
    if newComponentItem.itemTypeID == GUI_ITEM_TYPE.TURRET:
        return PreviewVehicleTurretInstaller(vehicle, newComponentItem, conflictedEqs)
    else:
        return PreviewVehicleModuleInstaller(vehicle, newComponentItem, conflictedEqs)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\processors\module.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:05 St�edn� Evropa (letn� �as)
