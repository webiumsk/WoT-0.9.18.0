# 2017.05.04 15:23:21 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/FortOrderConfirmationWindow.py
import BigWorld
from ClientFortifiedRegion import BUILDING_UPDATE_REASON
from gui.Scaleform.daapi.view.lobby.fortifications.fort_utils.FortSoundController import g_fortSoundController
from gui.Scaleform.genConsts.CONFIRM_DIALOG_ALIASES import CONFIRM_DIALOG_ALIASES
from gui.Scaleform.locale.MENU import MENU
from helpers import time_utils
from adisp import process
from gui import SystemMessages
from gui.Scaleform.daapi.view.lobby.fortifications.fort_utils.FortViewHelper import FortViewHelper
from gui.Scaleform.daapi.view.meta.FortOrderConfirmationWindowMeta import FortOrderConfirmationWindowMeta
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.shared.fortifications.context import OrderCtx
from helpers import i18n

class FortOrderConfirmationWindow(FortOrderConfirmationWindowMeta, FortViewHelper):

    def __init__(self, meta, handler):
        super(FortOrderConfirmationWindow, self).__init__()
        self.meta = meta
        self.handler = handler
        self._orderID = meta.getOrderID()

    def _populate(self):
        super(FortOrderConfirmationWindow, self)._populate()
        self._prepareAndSendData()
        self.startFortListening()
        self.as_setSettingsS({'title': self.meta.getTitle(),
         'submitBtnLabel': self.meta.getSubmitButtonLabel(),
         'cancelBtnLabel': self.meta.getCancelButtonLabel()})

    def _dispose(self):
        self.stopFortListening()
        if self.meta is not None:
            self.meta.destroy()
            self.meta = None
        self.handler = self._data = None
        super(FortOrderConfirmationWindow, self)._dispose()
        return

    def _prepareAndSendData(self):
        resultData = {}
        if self._orderID:
            orderTitle = i18n.makeString(FORTIFICATIONS.orders_orderpopover_ordertype(self._orderID))
            order = self.fortCtrl.getFort().getOrder(self.getOrderIDbyUID(self._orderID))
            building = self.fortCtrl.getFort().getBuilding(order.buildingID)
            defRes = building.storage
            maxPurchase = int(defRes / order.productionCost)
            maxAvailableCount = min(order.maxCount - order.count, maxPurchase, 100)
            resultData = {'icon': order.icon,
             'name': orderTitle,
             'description': order.description,
             'productionTime': order.productionTotalTime,
             'productionCost': order.productionCost,
             'level': order.level,
             'defaultValue': -1,
             'maxAvailableCount': maxAvailableCount,
             'linkage': CONFIRM_DIALOG_ALIASES.ORDER_ICON}
        self.as_setDataS(resultData)

    def onWindowClose(self):
        self.destroy()

    def submit(self, count):
        self.__requestToCreate(count)

    @process
    def __requestToCreate(self, count):
        orderTypeID = self.getOrderIDbyUID(self._orderID)
        count = int(count)
        result = yield self.fortProvider.sendRequest(OrderCtx(orderTypeID, count, waitingID='fort/order/add'))
        if result:
            g_fortSoundController.playCreateOrder()
            order = self.fortCtrl.getFort().getOrder(orderTypeID)
            SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.FORTIFICATION_ADDORDER, count=BigWorld.wg_getIntegralFormat(count), time=order.getProductionLeftTimeStr(), type=SystemMessages.SM_TYPE.Warning)
        self.destroy()

    def getTimeStr(self, time):
        return time_utils.getTillTimeString(time, MENU.TIME_TIMEVALUE)

    def onUpdated(self, isFullUpdate):
        self._prepareAndSendData()

    def onBuildingChanged(self, buildingTypeID, reason, ctx = None):
        if reason == BUILDING_UPDATE_REASON.DELETED:
            order = self.fortCtrl.getFort().getOrder(self.getOrderIDbyUID(self._orderID))
            if order.buildingID == buildingTypeID:
                self.destroy()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\fortifications\FortOrderConfirmationWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:21 St�edn� Evropa (letn� �as)
