# 2017.05.04 15:22:59 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/barracks/__init__.py
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, ViewTypes, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.barracks.Barracks import Barracks
    return (ViewSettings(VIEW_ALIAS.LOBBY_BARRACKS, Barracks, 'barracks.swf', ViewTypes.LOBBY_SUB, VIEW_ALIAS.LOBBY_BARRACKS, ScopeTemplates.LOBBY_SUB_SCOPE),)


def getBusinessHandlers():
    return (BarracksPackageBusinessHandler(),)


class BarracksPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = ((VIEW_ALIAS.LOBBY_BARRACKS, self.loadViewByCtxEvent),)
        super(BarracksPackageBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\barracks\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:59 Støední Evropa (letní èas)
