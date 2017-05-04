# 2017.05.04 15:21:43 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/game_control/relogin_controller.py
from debug_utils import LOG_DEBUG
from skeletons.gui.game_control import IReloginController

class ReloginController(IReloginController):

    def __init__(self):
        super(ReloginController, self).__init__()
        self.__reloginChain = None
        self.__reloginStoppedHandler = None
        return

    def fini(self):
        self.__clearReloginChain()
        super(ReloginController, self).fini()

    def doRelogin(self, peripheryID, onStoppedHandler = None, extraChainSteps = None):
        from gui.shared import actions
        LOG_DEBUG('Attempt to relogin to the another periphery', peripheryID)
        chain = [actions.LeavePrbModalEntity(), actions.DisconnectFromPeriphery(), actions.ConnectToPeriphery(peripheryID)]
        if extraChainSteps is not None:
            chain += extraChainSteps
        self.__reloginStoppedHandler = onStoppedHandler
        self.__reloginChain = actions.ActionsChain(chain)
        self.__reloginChain.onStopped += self.__onReloginStopped
        self.__reloginChain.start()
        return

    def __onReloginStopped(self, isCompleted):
        if self.__reloginStoppedHandler is not None:
            self.__reloginStoppedHandler(isCompleted)
        LOG_DEBUG('Relogin finished', isCompleted)
        return

    def __clearReloginChain(self):
        if self.__reloginChain is not None:
            self.__reloginChain.onStopped -= self.__onReloginStopped
            self.__reloginChain.stop()
            self.__reloginChain = None
            self.__reloginStoppedHandler = None
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\game_control\relogin_controller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:43 St�edn� Evropa (letn� �as)
