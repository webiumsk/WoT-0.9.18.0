# 2017.05.04 15:27:51 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/tutorial/control/quests/triggers.py
import BigWorld
from account_helpers.AccountSettings import AccountSettings
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
from gui.shared import g_eventBus, events
from gui.shared.event_bus import EVENT_BUS_SCOPE
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from tutorial import doc_loader
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP
from gui.shared.ItemsCache import g_itemsCache
from gui.shared.gui_items import GUI_ITEM_TYPE_INDICES
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA, RESEARCH_CRITERIA
from tutorial.control import g_tutorialWeaver
from tutorial.control.lobby import aspects
from tutorial.control.triggers import Trigger, TriggerWithValidateVar, TriggerWithSubscription
from tutorial.settings import createSettingsCollection

class AllTutorialBonusesTrigger(TriggerWithValidateVar):

    def __init__(self, triggerID, validateVarID, setVarID = None, validateUpdateOnly = False):
        super(AllTutorialBonusesTrigger, self).__init__(triggerID, validateVarID, setVarID, validateUpdateOnly)
        self._tutorDescriptor = None
        return

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            g_clientUpdateManager.addCallbacks({'stats.tutorialsCompleted': self.__onTutorialCompleted})
            setting = createSettingsCollection().getSettings(self.getVar())
            self._tutorDescriptor = doc_loader.loadDescriptorData(setting)
        self.toggle(isOn=self.isOn(self._bonuses.getCompleted()))

    def isOn(self, completed):
        return self._tutorDescriptor.areAllBonusesReceived(completed)

    def clear(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.isSubscribed = False
        self.isRunning = False
        self._tutorDescriptor = None
        return

    def __onTutorialCompleted(self, completed):
        if completed is not None:
            self.toggle(isOn=self.isOn(completed))
        return


class InvalidateFlagsTrigger(Trigger):

    def __init__(self, triggerID):
        super(InvalidateFlagsTrigger, self).__init__(triggerID)

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            g_clientUpdateManager.addCallbacks({'stats.tutorialsCompleted': self.__onTutorialCompleted})
        self.toggle(isOn=self.isOn())

    def clear(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.isSubscribed = False
        self.isRunning = False
        self._battleDesc = None
        return

    def __onTutorialCompleted(self, _):
        self._tutorial.invalidateFlags()


class ChapterBonusTrigger(TriggerWithValidateVar):

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            g_clientUpdateManager.addCallbacks({'stats.tutorialsCompleted': self.__onTutorialCompleted})
        self.toggle(isOn=self.isOn(self._bonuses.getCompleted()))

    def isOn(self, completed):
        return self._descriptor.getChapter(self.getVar()).isBonusReceived(completed)

    def clear(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.isSubscribed = False
        self.isRunning = False

    def __onTutorialCompleted(self, completed):
        if completed is not None:
            self.toggle(isOn=self.isOn(completed))
        return


class RandomBattlesCountTrigger(Trigger):

    def __init__(self, triggerID):
        super(RandomBattlesCountTrigger, self).__init__(triggerID)

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            g_clientUpdateManager.addCallbacks({'stats.dossier': self.__dossierUpdateCallBack})
        self.toggle(isOn=self.isOn())

    def __dossierUpdateCallBack(self, *args):
        self.toggle(isOn=self.isOn())

    def isOn(self):
        randomStats = g_itemsCache.items.getAccountDossier().getRandomStats()
        return randomStats.getBattlesCount() > 0

    def clear(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.isSubscribed = False
        self.isRunning = False


class ResearchModuleTrigger(Trigger):

    def __init__(self, triggerID):
        super(ResearchModuleTrigger, self).__init__(triggerID)

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            g_clientUpdateManager.addCallbacks({'stats.unlocks': self.__unlocksUpdateCallBack})
        self.toggle(isOn=self.isOn())

    def isOn(self):
        vehicles = g_itemsCache.items.getVehicles(criteria=REQ_CRITERIA.VEHICLE.LEVELS([1]) | ~REQ_CRITERIA.SECRET | ~REQ_CRITERIA.HIDDEN | ~REQ_CRITERIA.VEHICLE.PREMIUM | ~REQ_CRITERIA.VEHICLE.IS_PREMIUM_IGR | ~REQ_CRITERIA.VEHICLE.EVENT)
        unlocks = g_itemsCache.items.stats.unlocks
        unlockedItemsGetter = g_techTreeDP.getUnlockedVehicleItems
        for vehCD, vehicle in vehicles.iteritems():
            if len(unlockedItemsGetter(vehicle, unlocks)):
                return True

        return False

    def clear(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.isSubscribed = False
        self.isRunning = False

    def __unlocksUpdateCallBack(self, *args):
        self.toggle(isOn=self.isOn())


class InstallModuleTrigger(Trigger):

    def __init__(self, triggerID):
        super(InstallModuleTrigger, self).__init__(triggerID)

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            g_clientUpdateManager.addCallbacks({'inventory': self.__onInventoryChange})
        self.toggle(isOn=self.isOn())

    def isOn(self):
        vehicles = g_itemsCache.items.getVehicles(criteria=RESEARCH_CRITERIA.VEHICLE_TO_UNLOCK)
        unlocks = g_itemsCache.items.stats.unlocks
        unlockedItemsGetter = g_techTreeDP.getUnlockedVehicleItems
        for vehCD, vehicle in vehicles.iteritems():
            items = unlockedItemsGetter(vehicle, unlocks)
            for itemCD in items.iterkeys():
                item = g_itemsCache.items.getItemByCD(itemCD)
                if item.isInstalled(vehicle):
                    return True

        return False

    def clear(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.isSubscribed = False
        self.isRunning = False

    def __onInventoryChange(self, *args):
        self.toggle(isOn=self.isOn())


class ResearchVehicleTrigger(TriggerWithValidateVar):

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            g_clientUpdateManager.addCallbacks({'stats.unlock': self.__unlocksUpdateCallBack})
        self.toggle(isOn=self.isOn())

    def __unlocksUpdateCallBack(self, *args):
        self.toggle(isOn=self.isOn())

    def isOn(self):
        return bool(len(g_itemsCache.items.getVehicles(criteria=REQ_CRITERIA.UNLOCKED | REQ_CRITERIA.VEHICLE.LEVELS([self.getVar()]) | ~REQ_CRITERIA.SECRET | ~REQ_CRITERIA.HIDDEN | ~REQ_CRITERIA.VEHICLE.PREMIUM | ~REQ_CRITERIA.VEHICLE.IS_PREMIUM_IGR | ~REQ_CRITERIA.VEHICLE.EVENT)))

    def clear(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.isSubscribed = False
        self.isRunning = False


class BuyVehicleTrigger(TriggerWithValidateVar):

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            g_clientUpdateManager.addCallbacks({'inventory': self.__inventoryUpdateCallBack})
        self.toggle(isOn=self.isOn())

    def isOn(self):
        return bool(len(g_itemsCache.items.getVehicles(criteria=REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.LEVELS([self.getVar()]) | ~REQ_CRITERIA.SECRET | ~REQ_CRITERIA.HIDDEN | ~REQ_CRITERIA.VEHICLE.PREMIUM | ~REQ_CRITERIA.VEHICLE.IS_PREMIUM_IGR | ~REQ_CRITERIA.VEHICLE.EVENT)))

    def clear(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.isSubscribed = False
        self.isRunning = False

    def __inventoryUpdateCallBack(self, *args):
        self.toggle(isOn=self.isOn())


class InventoryVehicleTrigger(BuyVehicleTrigger):

    def isOn(self):
        vehicleCriteria = self.getVar()
        minLvl, maxLvl = vehicleCriteria.get('levelsRange', (1, 10))
        criteria = REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.LEVELS(range(minLvl, maxLvl)) | ~REQ_CRITERIA.VEHICLE.EXPIRED_RENT | ~REQ_CRITERIA.VEHICLE.EVENT_BATTLE
        return bool(len(g_itemsCache.items.getVehicles(criteria)))


class PermanentVehicleOwnTrigger(BuyVehicleTrigger):

    def isOn(self):
        vehicle = g_itemsCache.items.getItemByCD(self.getVar()['vehicle'])
        return vehicle.isPurchased


class VehicleBattleCountTrigger(TriggerWithValidateVar):

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            g_clientUpdateManager.addCallbacks({'stats.dossier': self.__dossierUpdateCallBack})
        self.toggle(isOn=self.isOn())

    def isOn(self):
        vehicleDossier = g_itemsCache.items.getVehicleDossier(self.getVar()['vehicle'])
        return vehicleDossier.getTotalStats().getBattlesCount() >= self.getVar()['battlesCount']

    def clear(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.isSubscribed = False
        self.isRunning = False

    def __dossierUpdateCallBack(self, *args):
        self.toggle(isOn=self.isOn())


class TutorialIntSettingsTrigger(TriggerWithValidateVar):
    settingsCore = dependency.descriptor(ISettingsCore)

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            self.settingsCore.onSettingsChanged += self.__onSettingsChanged
        self.toggle(isOn=self.isOn())

    def isOn(self):
        return self.settingsCore.serverSettings.getSectionSettings(SETTINGS_SECTIONS.TUTORIAL, self.getVar(), False)

    def clear(self):
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
        self.isSubscribed = False
        self.isRunning = False

    def __onSettingsChanged(self, diff):
        if self.getVar() in diff:
            self.toggle(isOn=bool(diff[self.getVar()]))


class TutorialAccountSettingsTrigger(TriggerWithValidateVar):

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            AccountSettings.onSettingsChanging += self.__onSettingsChanged
        self.toggle(isOn=self.isOn())

    def isOn(self):
        var = self.getVar()
        if var:
            return var['value'] == AccountSettings.getSettings(var['key'])
        return False

    def clear(self):
        AccountSettings.onSettingsChanging -= self.__onSettingsChanged
        self.isSubscribed = False
        self.isRunning = False

    def __onSettingsChanged(self, key, value):
        if key in self.getVar():
            self.toggle(isOn=self.isOn())


class XpExchangeTrigger(Trigger):

    def __init__(self, triggerID):
        super(XpExchangeTrigger, self).__init__(triggerID)
        self.__startProcessPointcutId = -1

    def run(self):
        if not self.isSubscribed:
            self.__startProcessPointcutId = g_tutorialWeaver.weave(pointcut=aspects.StartXpExchangePointcut, aspects=[aspects.StartXpExchangeAspect(self)])
            self.isSubscribed = True
        self.isRunning = True

    def clear(self):
        g_tutorialWeaver.clear(self.__startProcessPointcutId)
        self.__startProcessPointcutId = -1
        self.isSubscribed = False
        self.isRunning = False


class InstallItemsTrigger(TriggerWithValidateVar):

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            g_clientUpdateManager.addCallbacks({'inventory': self.__inventoryUpdateCallBack})
        self.toggle(isOn=self.isOn())

    def isOn(self):
        conditionVar = self.getVar()
        itemsList = conditionVar.get('items', [])
        itemType = conditionVar.get('itemType', None)
        criteria = REQ_CRITERIA.EMPTY
        if itemsList:
            criteria = REQ_CRITERIA.IN_CD_LIST(itemsList)
        vehicles = g_itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY).values()
        items = g_itemsCache.items.getItems(itemTypeID=GUI_ITEM_TYPE_INDICES[itemType], criteria=criteria).values()
        for item in items:
            if len(item.getInstalledVehicles(vehicles)) > 0:
                return True

        return False

    def clear(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.isSubscribed = False
        self.isRunning = False

    def __inventoryUpdateCallBack(self, *args):
        self.toggle(isOn=self.isOn())


class TimerTrigger(TriggerWithValidateVar):

    def __init__(self, triggerID, validateVarID, setVarID = None, validateUpdateOnly = False):
        super(TimerTrigger, self).__init__(triggerID, validateVarID, setVarID, validateUpdateOnly)
        self.__timerCallback = None
        return

    def run(self):
        self.isRunning = True
        if self.__timerCallback is None:
            self.isSubscribed = True
            self.__timerCallback = BigWorld.callback(self.getVar(), self.__updateTimer)
        self.toggle(isOn=False)
        return

    def clear(self):
        if self.__timerCallback is not None:
            BigWorld.cancelCallback(self.__timerCallback)
            self.__timerCallback = None
        self.isSubscribed = False
        self.isRunning = False
        return

    def __updateTimer(self, *args):
        self.__timerCallback = None
        self.toggle(isOn=True)
        return


class SimpleWindowCloseTrigger(TriggerWithSubscription):

    def isOn(self, targetID = None):
        return targetID == self.getVar()

    def _subscribe(self):
        g_eventBus.addListener(events.TutorialEvent.SIMPLE_WINDOW_CLOSED, self.__onCloseSimpleWindow, scope=EVENT_BUS_SCOPE.GLOBAL)

    def _unsubscribe(self):
        g_eventBus.removeListener(events.TutorialEvent.SIMPLE_WINDOW_CLOSED, self.__onCloseSimpleWindow, scope=EVENT_BUS_SCOPE.GLOBAL)

    def __onCloseSimpleWindow(self, event):
        self.toggle(isOn=self.isOn(event.targetID))


class SimpleWindowProcessTrigger(TriggerWithSubscription):

    def isOn(self, targetID = None):
        return targetID == self.getVar()

    def _subscribe(self):
        g_eventBus.addListener(events.TutorialEvent.SIMPLE_WINDOW_PROCESSED, self.__onProcessSimpleWindow, scope=EVENT_BUS_SCOPE.GLOBAL)

    def _unsubscribe(self):
        g_eventBus.removeListener(events.TutorialEvent.SIMPLE_WINDOW_PROCESSED, self.__onProcessSimpleWindow, scope=EVENT_BUS_SCOPE.GLOBAL)

    def __onProcessSimpleWindow(self, event):
        self.toggle(isOn=self.isOn(event.targetID))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\control\quests\triggers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:51 St�edn� Evropa (letn� �as)
