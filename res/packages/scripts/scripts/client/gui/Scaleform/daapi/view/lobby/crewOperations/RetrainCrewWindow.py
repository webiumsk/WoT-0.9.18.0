# 2017.05.04 15:23:08 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/crewOperations/RetrainCrewWindow.py
from CurrentVehicle import g_currentVehicle
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.RetrainCrewWindowMeta import RetrainCrewWindowMeta
from gui.shared.ItemsCache import g_itemsCache
from gui.shared.gui_items.processors.tankman import TankmanCrewRetraining
from gui.shared.utils import decorators
from gui.shared.money import Money
from gui import SystemMessages
from items import tankmen
from gui.shared.formatters import text_styles
from helpers.i18n import makeString as _ms
from gui.Scaleform.locale.RETRAIN_CREW import RETRAIN_CREW

class RetrainCrewWindow(RetrainCrewWindowMeta):
    AVAILABLE_OPERATIONS = range(3)

    def __init__(self, ctx = None):
        super(RetrainCrewWindow, self).__init__()

    def _populate(self):
        super(RetrainCrewWindow, self)._populate()
        vehicle = g_currentVehicle.item
        crewInfo = []
        g_clientUpdateManager.addCallbacks({'stats.credits': self.__updateDataCallBack,
         'stats.gold': self.__updateDataCallBack})
        for idx, tMan in vehicle.crew:
            if tMan is not None:
                if tMan.vehicleNativeDescr.type.compactDescr != tMan.vehicleDescr.type.compactDescr:
                    crewInfo.append(self.__getTankmanRoleInfo(tMan))
                elif tMan.efficiencyRoleLevel < tankmen.MAX_SKILL_LEVEL:
                    crewInfo.append(self.__getTankmanRoleInfo(tMan))

        self.as_setVehicleDataS({'nationID': vehicle.nationID,
         'vType': vehicle.type,
         'vIntCD': vehicle.intCD,
         'vLevel': vehicle.level,
         'vName': vehicle.shortUserName,
         'vIconSmall': vehicle.iconSmall})
        self.as_setAllCrewDataS({'crew': crewInfo})
        self.__updateDataCallBack()
        return

    def __updateDataCallBack(self, data = None):
        items = g_itemsCache.items
        shopPrices, actionPrc = items.shop.getTankmanCostWithDefaults()
        data = {'credits': items.stats.credits,
         'gold': items.stats.gold,
         'actionPrc': actionPrc,
         'tankmanCost': shopPrices}
        self.as_setCrewOperationDataS(data)

    def __getTankmanRoleInfo(self, tankman):
        vehicle = g_itemsCache.items.getItemByCD(tankman.vehicleNativeDescr.type.compactDescr)
        return {'realRoleLevel': tankman.efficiencyRoleLevel,
         'roleLevel': tankman.roleLevel,
         'nativeVehicleType': vehicle.type,
         'nativeVehicleIntCD': vehicle.intCD,
         'tankmanID': tankman.invID,
         'nationID': tankman.nationID,
         'iconPath': '../maps/icons/tankmen/roles/medium/%s' % tankman.iconRole}

    def submit(self, operationId):
        if operationId in self.AVAILABLE_OPERATIONS:
            self.__processCrewRetrianing(operationId)
            self.destroy()

    @decorators.process('crewRetraining')
    def __processCrewRetrianing(self, operationId):
        items = g_itemsCache.items
        vehicle = g_currentVehicle.item
        shopPrices = items.shop.tankmanCost
        currentSelection = shopPrices[operationId]
        crewInvIDs = []
        for idx, tMan in vehicle.crew:
            if tMan is not None:
                if tMan.vehicleNativeDescr.type.compactDescr != tMan.vehicleDescr.type.compactDescr:
                    crewInvIDs.append(tMan.invID)
                elif tMan.roleLevel != tankmen.MAX_SKILL_LEVEL and tMan.efficiencyRoleLevel < currentSelection['roleLevel']:
                    crewInvIDs.append(tMan.invID)

        result = yield TankmanCrewRetraining(crewInvIDs, vehicle, operationId).request()
        if len(result.userMsg):
            SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)
        return

    def onWindowClose(self):
        self.destroy()

    def changeRetrainType(self, operationId):
        operationId = int(operationId)
        items = g_itemsCache.items
        vehicle = g_currentVehicle.item
        shopPrices = items.shop.tankmanCost
        currentSelection = shopPrices[operationId]
        crewInfo = []
        for idx, tMan in vehicle.crew:
            if tMan is not None:
                if tMan.vehicleNativeDescr.type.compactDescr != tMan.vehicleDescr.type.compactDescr:
                    crewInfo.append(self.__getTankmanRoleInfo(tMan))
                elif tMan.roleLevel != tankmen.MAX_SKILL_LEVEL and tMan.efficiencyRoleLevel < currentSelection['roleLevel']:
                    crewInfo.append(self.__getTankmanRoleInfo(tMan))

        crewSize = len(crewInfo)
        price = crewSize * Money(**currentSelection)
        self.as_setCrewDataS({'price': price,
         'crew': crewInfo,
         'crewMembersText': text_styles.concatStylesWithSpace(_ms(RETRAIN_CREW.LABEL_CREWMEMBERS), text_styles.middleTitle(crewSize))})
        return

    def _dispose(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(RetrainCrewWindow, self)._dispose()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\crewOperations\RetrainCrewWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:08 St�edn� Evropa (letn� �as)
