# 2017.05.04 15:22:18 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/formatters/windows.py
from gui.LobbyContext import g_lobbyContext
from gui.Scaleform.locale.PREBATTLE import PREBATTLE
from gui.shared import actions
from gui.prb_control.settings import PREBATTLE_ACTION_NAME
from helpers import dependency
from predefined_hosts import g_preDefinedHosts
from skeletons.gui.server_events import IEventsCache

class SwitchPeripheryCtx(object):

    def getHeader(self):
        raise NotImplementedError

    def getDescription(self):
        raise NotImplementedError

    def getSelectServerLabel(self):
        raise NotImplementedError

    def getApplySwitchLabel(self):
        raise NotImplementedError

    def getExtraChainSteps(self):
        raise NotImplementedError

    def getForbiddenPeripherieIDs(self):
        raise NotImplementedError


class SwitchPeripheryCompanyCtx(SwitchPeripheryCtx):
    eventsCache = dependency.descriptor(IEventsCache)

    def getHeader(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_COMPANY_HEADER

    def getDescription(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_COMPANY_DESCRIPTION

    def getSelectServerLabel(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_COMPANY_SELECTSERVERLABEL

    def getApplySwitchLabel(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_COMPANY_APPLYSWITCHLABEL

    def getExtraChainSteps(self):

        def onLobbyInit():
            from gui.Scaleform.daapi.view.lobby.header import battle_selector_items
            battle_selector_items.getItems().select(PREBATTLE_ACTION_NAME.COMPANIES_LIST)

        return [actions.OnLobbyInitedAction(onInited=onLobbyInit)]

    def getForbiddenPeripherieIDs(self):
        validPeripheryIDs = set((host.peripheryID for host in g_preDefinedHosts.hosts() if host.peripheryID != 0))
        return validPeripheryIDs - self.eventsCache.getCompanyBattles().peripheryIDs


class SwitchPeripheryFortCtx(SwitchPeripheryCtx):

    def getHeader(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_FORT_HEADER

    def getDescription(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_FORT_DESCRIPTION

    def getSelectServerLabel(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_FORT_SELECTSERVERLABEL

    def getApplySwitchLabel(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_FORT_APPLYSWITCHLABEL

    def getExtraChainSteps(self):
        return None

    def getForbiddenPeripherieIDs(self):
        return g_lobbyContext.getServerSettings().getForbiddenSortiePeripheryIDs()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\formatters\windows.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:18 St�edn� Evropa (letn� �as)
