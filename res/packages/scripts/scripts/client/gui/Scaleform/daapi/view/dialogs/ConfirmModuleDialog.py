# 2017.05.04 15:22:48 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/ConfirmModuleDialog.py
from PlayerEvents import g_playerEvents
from adisp import process
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.view.meta.ConfirmItemWindowMeta import ConfirmItemWindowMeta
from gui.Scaleform.genConsts.CONFIRM_DIALOG_ALIASES import CONFIRM_DIALOG_ALIASES
from gui.shared import g_itemsCache
from gui.shared.utils import CLIP_ICON_PATH, EXTRA_MODULE_INFO
from items import vehicles

class ConfirmModuleDialog(ConfirmItemWindowMeta):
    """
    Basic implementation of window which provides operation with modules.
    """

    def __init__(self, meta, handler):
        super(ConfirmModuleDialog, self).__init__()
        self.meta = meta
        self.handler = handler

    def _populate(self):
        super(ConfirmModuleDialog, self)._populate()
        g_playerEvents.onShopResync += self._onShopResync
        self._prepareAndSendData()
        self.as_setSettingsS({'title': self.meta.getTitle(),
         'submitBtnLabel': self.meta.getSubmitButtonLabel(),
         'cancelBtnLabel': self.meta.getCancelButtonLabel()})
        self.meta.onInvalidate += self._prepareAndSendData

    def _dispose(self):
        g_playerEvents.onShopResync -= self._onShopResync
        if self.meta is not None:
            self.meta.onInvalidate -= self._prepareAndSendData
            self.meta.destroy()
            self.meta = None
        self.handler = self._data = None
        super(ConfirmModuleDialog, self)._dispose()
        return

    def _callHandler(self, success, *kargs):
        if self.handler is not None:
            self.handler((success, kargs))
        return

    def _onShopResync(self):
        self._prepareAndSendData()

    def _prepareAndSendData(self):
        """
        Create necessary object which expects flash component and
        pass it through DAAPI
        """
        items = g_itemsCache.items
        module = items.getItemByCD(self.meta.getTypeCompDescr())
        if module is not None:
            shop = g_itemsCache.items.shop
            actualPrice = self.meta.getActualPrice(module)
            defaultPrice = self.meta.getDefaultPrice(module)
            currency = self.meta.getCurrency(module)
            isAction = actualPrice.isAllSet() and (shop.isEnabledBuyingGoldShellsForCredits and module.itemTypeID == vehicles._SHELL or shop.isEnabledBuyingGoldEqsForCredits and module.itemTypeID == vehicles._EQUIPMENT)
            icon = self.__getIcon(module)
            extraData = None
            if module.itemTypeID == vehicles._GUN and module.isClipGun():
                extraData = CLIP_ICON_PATH
            action = None
            if actualPrice != defaultPrice:
                action = self.meta.getActionVO(module)
            resultData = {'id': self.meta.getTypeCompDescr(),
             'price': actualPrice,
             'actionPriceData': action,
             'icon': icon,
             'name': module.userName,
             'description': module.getShortInfo(),
             'currency': currency,
             'defaultValue': self.meta.getDefaultValue(module),
             'maxAvailableCount': self.meta.getMaxAvailableItemsCount(module),
             'isActionNow': isAction,
             'moduleLabel': module.getGUIEmblemID(),
             'level': module.level,
             'linkage': CONFIRM_DIALOG_ALIASES.MODULE_ICON,
             EXTRA_MODULE_INFO: extraData}
            self.as_setDataS(resultData)
        else:
            LOG_ERROR("Couldn't find module with given compact:", self.meta.getTypeCompDescr())
            self.onWindowClose()
        return

    def __getIcon(self, module):
        """
        @param module: target module received by int compact descriptor
        @return: For shells, option devices, equipment the value of icon
                                is the path to an icon file in the directory,
                                for vehicle modules the value of icon is the level of
                                particular module
        """
        if module.itemTypeID not in (vehicles._OPTIONALDEVICE, vehicles._SHELL, vehicles._EQUIPMENT):
            return str(module.level)
        return module.icon

    def onWindowClose(self):
        self._callHandler(False)
        self.destroy()

    def submit(self, count, currency):
        module = g_itemsCache.items.getItemByCD(self.meta.getTypeCompDescr())
        self.meta.submit(module, count, currency)
        self._callHandler(True, self.meta.getTypeCompDescr(), count, currency)
        self.destroy()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\dialogs\ConfirmModuleDialog.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:48 St�edn� Evropa (letn� �as)
