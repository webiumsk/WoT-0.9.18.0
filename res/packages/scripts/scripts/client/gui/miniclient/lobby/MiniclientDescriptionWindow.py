# 2017.05.04 15:21:49 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/lobby/MiniclientDescriptionWindow.py
import os
from gui import GUI_SETTINGS
from gui.shared import g_eventBus, events
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.game_control import IBrowserController

class MiniclientDescriptionWindow(object):
    browserCtrl = dependency.descriptor(IBrowserController)

    def __init__(self):
        g_eventBus.addListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__openDescriptionInBrowser)

    def __openDescriptionInBrowser(self, event):
        current_working_dir = os.getcwd()
        self.browserCtrl.load(url='{0}/$LANGUAGE_CODE/greeting/mini_wot/'.format(GUI_SETTINGS.miniclient['webBridgeRootURL']), title=_ms('#miniclient:hangar/miniclient_description_window/title'), browserSize=(780, 450), showCloseBtn=True, showActionBtn=False, isAsync=True, showWaiting=False)(lambda success: True)
        g_eventBus.removeListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.__openDescriptionInBrowser)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\MiniclientDescriptionWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:49 Støední Evropa (letní èas)
