# 2017.05.04 15:27:36 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/notification/NotificationMVC.py
from notification.AlertController import AlertController
from notification.NotificationsCounter import NotificationsCounter
from notification.NotificationsModel import NotificationsModel
from notification.actions_handlers import NotificationsActionsHandlers

class _NotificationMVC:

    def __init__(self):
        self.__model = None
        self.__alertsController = None
        self.__actionsHandlers = None
        self.__unreadMessagesCounter = NotificationsCounter()
        return

    def initialize(self):
        self.__model = NotificationsModel(self.__unreadMessagesCounter)
        self.__actionsHandlers = NotificationsActionsHandlers()
        self.__alertsController = AlertController(self.__model)

    def getModel(self):
        return self.__model

    def getAlertController(self):
        return self.__alertsController

    def handleAction(self, typeID, entityID, action):
        self.__actionsHandlers.handleAction(self.__model, int(typeID), long(entityID), action)

    def cleanUp(self, resetCounter = False):
        self.__alertsController.cleanUp()
        self.__actionsHandlers.cleanUp()
        self.__model.cleanUp()
        self.__alertsController = None
        self.__actionsHandlers = None
        if resetCounter:
            self.__unreadMessagesCounter.clear()
            self.__unreadMessagesCounter = NotificationsCounter()
        self.__model = None
        return


g_instance = _NotificationMVC()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\notification\NotificationMVC.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:36 St�edn� Evropa (letn� �as)
