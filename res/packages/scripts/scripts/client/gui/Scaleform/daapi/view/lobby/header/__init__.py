# 2017.05.04 15:23:39 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/header/__init__.py
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, GroupedViewSettings, ViewTypes, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.header.AccountPopover import AccountPopover
    from gui.Scaleform.daapi.view.lobby.header.BattleTypeSelectPopover import BattleTypeSelectPopover
    from gui.Scaleform.daapi.view.lobby.header.SquadTypeSelectPopover import SquadTypeSelectPopover
    from gui.Scaleform.daapi.view.lobby.header.QuestsControl import QuestsControl
    from gui.Scaleform.daapi.view.lobby.header.LobbyTicker import LobbyTicker
    from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import LobbyHeader
    return (GroupedViewSettings(VIEW_ALIAS.ACCOUNT_POPOVER, AccountPopover, 'accountPopover.swf', ViewTypes.WINDOW, 'accountPopover', VIEW_ALIAS.ACCOUNT_POPOVER, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.BATTLE_TYPE_SELECT_POPOVER, BattleTypeSelectPopover, 'itemSelectorPopover.swf', ViewTypes.WINDOW, VIEW_ALIAS.BATTLE_TYPE_SELECT_POPOVER, VIEW_ALIAS.BATTLE_TYPE_SELECT_POPOVER, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.SQUAD_TYPE_SELECT_POPOVER, SquadTypeSelectPopover, 'itemSelectorPopover.swf', ViewTypes.WINDOW, VIEW_ALIAS.SQUAD_TYPE_SELECT_POPOVER, VIEW_ALIAS.SQUAD_TYPE_SELECT_POPOVER, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.QUESTS_CONTROL, QuestsControl, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.LOBBY_HEADER, LobbyHeader, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.TICKER, LobbyTicker, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (HeaderPackageBusinessHandler(),)


class HeaderPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = ((VIEW_ALIAS.ACCOUNT_POPOVER, self.loadViewByCtxEvent), (VIEW_ALIAS.BATTLE_TYPE_SELECT_POPOVER, self.loadViewByCtxEvent), (VIEW_ALIAS.SQUAD_TYPE_SELECT_POPOVER, self.loadViewByCtxEvent))
        super(HeaderPackageBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\header\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:39 St�edn� Evropa (letn� �as)
