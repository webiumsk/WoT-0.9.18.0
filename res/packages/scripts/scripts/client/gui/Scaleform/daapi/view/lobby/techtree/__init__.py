# 2017.05.04 15:24:06 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/techtree/__init__.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, ViewTypes, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from gui.shared.events import LoadEvent

def getContextMenuHandlers():
    from gui.Scaleform.daapi.view.lobby.techtree import research_cm_handlers
    return ((CONTEXT_MENU_HANDLER_TYPE.RESEARCH_VEHICLE, research_cm_handlers.ResearchVehicleContextMenuHandler), (CONTEXT_MENU_HANDLER_TYPE.RESEARCH_ITEM, research_cm_handlers.ResearchItemContextMenuHandler))


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.techtree.Research import Research
    from gui.Scaleform.daapi.view.lobby.techtree.TechTree import TechTree
    return (ViewSettings(VIEW_ALIAS.LOBBY_TECHTREE, TechTree, 'techtree.swf', ViewTypes.LOBBY_SUB, VIEW_ALIAS.LOBBY_TECHTREE, ScopeTemplates.DEFAULT_SCOPE, True), ViewSettings(VIEW_ALIAS.LOBBY_RESEARCH, Research, 'research.swf', ViewTypes.LOBBY_SUB, VIEW_ALIAS.LOBBY_RESEARCH, ScopeTemplates.DEFAULT_SCOPE, True))


def getBusinessHandlers():
    return (_TechTreePackageBusinessHandler(),)


class _TechTreePackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = ((VIEW_ALIAS.LOBBY_TECHTREE, self.__loadTechTree), (VIEW_ALIAS.LOBBY_RESEARCH, self.__loadResearch), (LoadEvent.EXIT_FROM_RESEARCH, self.__exitFromResearch))
        super(_TechTreePackageBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
        self.__exitEvent = None
        return

    def __loadTechTree(self, event):
        self.loadViewWithDefName(VIEW_ALIAS.LOBBY_TECHTREE, ctx=event.ctx)

    def __loadResearch(self, event):
        ctx = event.ctx
        self.__exitEvent = ctx.get('exit')
        self.loadViewWithDefName(VIEW_ALIAS.LOBBY_RESEARCH, ctx=ctx)

    def __exitFromResearch(self, _):
        if self.__exitEvent is not None:
            g_eventBus.handleEvent(self.__exitEvent, scope=EVENT_BUS_SCOPE.LOBBY)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\techtree\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:06 St�edn� Evropa (letn� �as)
