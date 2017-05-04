# 2017.05.04 15:22:56 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/ServerStats.py
import constants
from adisp import process
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.servers_data_provider import ServersDataProvider
from gui.prb_control.entities.base.legacy.listener import ILegacyListener
from helpers import dependency
from helpers import i18n
from ConnectionManager import connectionManager
from predefined_hosts import g_preDefinedHosts, HOST_AVAILABILITY, REQUEST_RATE
from gui import GUI_SETTINGS, DialogsInterface, makeHtmlString
from gui.shared import events
from gui.shared.utils.functions import makeTooltip
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.Scaleform.daapi.view.meta.ServerStatsMeta import ServerStatsMeta
from skeletons.gui.game_control import IServerStatsController, IReloginController

class ServerStats(ServerStatsMeta, ILegacyListener):
    serverStats = dependency.descriptor(IServerStatsController)
    reloginCtrl = dependency.descriptor(IReloginController)

    def __init__(self):
        super(ServerStats, self).__init__()
        self.__isListSelected = False

    @process
    def relogin(self, peripheryID):
        if g_preDefinedHosts.isRoamingPeriphery(peripheryID):
            LOG_DEBUG('g_preDefinedHosts.isRoamingPeriphery(peripheryID)', peripheryID)
            success = yield DialogsInterface.showI18nConfirmDialog('changeRoamingPeriphery')
        else:
            success = yield DialogsInterface.showI18nConfirmDialog('changePeriphery')
        if success:
            self.reloginCtrl.doRelogin(peripheryID, self.__onReloing)
        else:
            self.as_changePeripheryFailedS()

    def startListenCsisUpdate(self, startListen):
        r"""
        Invokes by DAAPI when user open\close dropdown menu
        :param startListen: true - list has been opened, false - list has been closed
        """
        if GUI_SETTINGS.csisRequestRate == REQUEST_RATE.ON_REQUEST:
            if startListen:
                g_preDefinedHosts.startCSISUpdate()
            else:
                g_preDefinedHosts.stopCSISUpdate()
                self._updateServersList()
        if startListen:
            g_preDefinedHosts.requestPing(True)

    def _populate(self):
        super(ServerStats, self)._populate()
        self._serversDP = ServersDataProvider()
        self._serversDP.setFlashObject(self.as_getServersDPS())
        if constants.IS_SHOW_SERVER_STATS:
            self._updateCurrentServerInfo()
        self._updateServersList()
        self._updateRoamingCtrl()
        if not constants.IS_CHINA:
            if GUI_SETTINGS.csisRequestRate == REQUEST_RATE.ALWAYS:
                g_preDefinedHosts.startCSISUpdate()
            g_preDefinedHosts.onCsisQueryStart += self.__onServersUpdate
            g_preDefinedHosts.onCsisQueryComplete += self.__onServersUpdate
            g_preDefinedHosts.onPingPerformed += self.__onServersUpdate
        self.serverStats.onStatsReceived += self.__onStatsReceived
        self.addListener(events.FightButtonEvent.FIGHT_BUTTON_UPDATE, self._updateRoamingCtrl, scope=EVENT_BUS_SCOPE.LOBBY)

    def _dispose(self):
        self.removeListener(events.FightButtonEvent.FIGHT_BUTTON_UPDATE, self._updateRoamingCtrl, scope=EVENT_BUS_SCOPE.LOBBY)
        self.serverStats.onStatsReceived -= self.__onStatsReceived
        if not constants.IS_CHINA:
            g_preDefinedHosts.stopCSISUpdate()
            g_preDefinedHosts.onCsisQueryComplete -= self.__onServersUpdate
            g_preDefinedHosts.onCsisQueryStart -= self.__onServersUpdate
            g_preDefinedHosts.onPingPerformed -= self.__onServersUpdate
        self._serversDP.fini()
        self._serversDP = None
        super(ServerStats, self)._dispose()
        return

    def _updateCurrentServerInfo(self):
        from ConnectionManager import connectionManager
        if connectionManager.serverUserName:
            tooltipBody = i18n.makeString('#tooltips:header/info/players_online_full/body')
            tooltipFullData = makeTooltip('#tooltips:header/info/players_online_full/header', tooltipBody % {'servername': connectionManager.serverUserName})
            self.as_setServerStatsInfoS(tooltipFullData)
        self.__onStatsReceived()

    def _updateServersList(self):
        result = []
        simpleHostList = g_preDefinedHosts.getSimpleHostsList(g_preDefinedHosts.hostsWithRoaming())
        if len(simpleHostList):
            for idx, (hostName, name, csisStatus, peripheryID) in enumerate(simpleHostList):
                result.append({'label': self.__wrapServerName(name),
                 'data': hostName,
                 'id': peripheryID,
                 'csisStatus': csisStatus})

        if connectionManager.peripheryID == 0:
            result.insert(0, {'label': self.__wrapServerName(connectionManager.serverUserName),
             'id': 0,
             'csisStatus': HOST_AVAILABILITY.IGNORED,
             'data': connectionManager.url})
        if not self.__isListSelected:
            self.__isListSelected = True
            index = 0
            if connectionManager.peripheryID != 0:
                for idx, (hostName, name, csisStatus, peripheryID) in enumerate(simpleHostList):
                    if hostName == connectionManager.url:
                        index = idx
                        break

            self.as_setSelectedServerIndexS(index)
        self._serversDP.rebuildList(result)

    def _updateRoamingCtrl(self, event = None):
        isRoamingCtrlDisabled = False
        if self.prbDispatcher:
            isRoamingCtrlDisabled = self.prbDispatcher.getEntity().hasLockedState()
        self.as_disableRoamingDDS(isRoamingCtrlDisabled)

    def __onStatsReceived(self):
        if constants.IS_SHOW_SERVER_STATS:
            self.as_setServerStatsS(*self.serverStats.getFormattedStats())

    def __onServersUpdate(self, _ = None):
        self._updateServersList()

    def __wrapServerName(self, name):
        if constants.IS_CHINA:
            return makeHtmlString('html_templates:lobby/serverStats', 'serverName', {'name': name})
        return name

    def __onReloing(self, isCompleted):
        if not isCompleted:
            self.as_changePeripheryFailedS()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\ServerStats.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:56 St�edn� Evropa (letn� �as)
