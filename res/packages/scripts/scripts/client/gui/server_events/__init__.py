# 2017.05.04 15:25:39 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/server_events/__init__.py
from gui.server_events.EventsCache import EventsCache
from skeletons.gui.server_events import IEventsCache
__all__ = ('getServerEventsConfig',)

def getServerEventsConfig(manager):
    """ Configures services for package server_events.
    :param manager: helpers.dependency.DependencyManager
    """
    cache = EventsCache()
    cache.init()
    manager.bindInstance(IEventsCache, cache, finalizer='fini')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\server_events\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:39 Støední Evropa (letní èas)
