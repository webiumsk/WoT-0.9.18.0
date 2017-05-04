# 2017.05.04 15:21:39 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/game_control/browser_filters.py
from debug_utils import LOG_DEBUG
from gui.Scaleform.framework import g_entitiesFactories
from gui.shared import g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.events import OpenLinkEvent

def getFilters():
    return {_onShowInExternalBrowser, _onGoToHangar}


def _onShowInExternalBrowser(url, tags):
    """ Searches for custom tags 'external' and open given url in
    the external system browser. Do not return routine to the
    browser
    """
    if 'external' in tags:
        LOG_DEBUG('Browser url has been processed', url)
        g_eventBus.handleEvent(OpenLinkEvent(OpenLinkEvent.SPECIFIED, url))
        return True
    return False


def _onGoToHangar(url, tags):
    """ Does exactly what's said in name of function when founds tag written just bellow
    """
    if 'go_to_hangar' in tags:
        LOG_DEBUG('Browser url has been processed: going to hangar. Url: ', url)
        g_eventBus.handleEvent(g_entitiesFactories.makeLoadEvent('hangar'), scope=EVENT_BUS_SCOPE.LOBBY)
        return True
    return False
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\game_control\browser_filters.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:39 St�edn� Evropa (letn� �as)
