# 2017.05.04 15:26:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/helpers/LobbyAutomation.py
import BigWorld
from ConnectionManager import connectionManager
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewTypes
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA
from gui.app_loader.loader import g_appLoader
from gui.app_loader.settings import APP_NAME_SPACE as _SPACE
from AccountCommands import CMD_PRB_TEAM_READY

def _getLobby():
    return g_appLoader.getApp(_SPACE.SF_LOBBY)


_isConnecting = False
_server = ''
_login = ''
_password = ''
_battleTime = 10
_arenaId = 1
_justLogin = True

def setServerName(name):
    global _server
    _server = name


def setLogin(login):
    global _login
    _login = login


def setPassword(password):
    global _password
    _password = password


def setBattleTime(time):
    global _battleTime
    _battleTime = time


def setArenaId(arenaId):
    global _arenaId
    _arenaId = arenaId


def configure(serverName, login, password, battleTime, arenaId):
    setServerName(serverName)
    setLogin(login)
    setPassword(password)
    setBattleTime(battleTime)
    setArenaId(arenaId)


def logIn():
    global _isConnecting
    global _justLogin
    _isConnecting = False
    _justLogin = True
    _detectCurrentScreen()


def startBattle():
    global _isConnecting
    global _justLogin
    _isConnecting = False
    _justLogin = False
    _detectCurrentScreen()


def _detectCurrentScreen():
    global _isConnecting
    if Waiting.isVisible():
        BigWorld.callback(0.2, lambda : _detectCurrentScreen())
        return
    else:
        lobby = _getLobby()
        if lobby is None or lobby.containerManager is None:
            BigWorld.callback(0.2, lambda : _detectCurrentScreen())
            return
        dialogsContainer = lobby.containerManager.getContainer(ViewTypes.TOP_WINDOW)
        if dialogsContainer is not None:
            dialog = dialogsContainer.getView(criteria={POP_UP_CRITERIA.VIEW_ALIAS: VIEW_ALIAS.EULA})
            if dialog is not None:
                dialog.onApply()
            dialog = dialogsContainer.getView(criteria={POP_UP_CRITERIA.VIEW_ALIAS: 'tGreetingDialog'})
            if dialog is not None:
                dialog.cancel()
        view = lobby.containerManager.getView(ViewTypes.DEFAULT)
        if view and view.settings.alias == VIEW_ALIAS.LOGIN and view.isCreated() and connectionManager.isDisconnected() and not _isConnecting:
            _isConnecting = True
            _connect()
            BigWorld.callback(0.2, lambda : _detectCurrentScreen())
            return
        view = lobby.containerManager.getView(ViewTypes.DEFAULT)
        if view is not None and view.settings.alias == 'lobby':
            if _justLogin:
                return
            subView = lobby.containerManager.getView(ViewTypes.LOBBY_SUB)
            if subView.settings.alias == 'hangar':
                _leaveDevRoom()
                BigWorld.callback(0.2, lambda : _detectCurrentScreen())
                return
            if subView.settings.alias == 'trainingRoom':
                _enterBattle()
                return
        BigWorld.callback(0.2, lambda : _detectCurrentScreen())
        return


def _connect():
    connectionManager.connect(_server, _login, _password, isNeedSavingPwd=True)


def _leaveDevRoom():
    BigWorld.player().prb_leave(lambda result: _enterDevRoom())


def _enterDevRoom():
    BigWorld.player().prb_createDev(_arenaId, _battleTime, '')


def _enterBattle():
    BigWorld.player()._doCmdInt3(CMD_PRB_TEAM_READY, 1, 1, 0, _battleCallback)
    BigWorld.player()._doCmdInt3(CMD_PRB_TEAM_READY, 2, 1, 0, _battleCallback)


def _battleCallback(p1, p2, p3):
    pass
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\helpers\LobbyAutomation.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:46 St�edn� Evropa (letn� �as)
