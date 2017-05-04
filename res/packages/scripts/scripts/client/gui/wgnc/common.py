# 2017.05.04 15:26:34 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/wgnc/common.py
from debug_utils import LOG_WARNING

class WebHandlersContainer(object):
    """
    Allows to configure list of web-client handlers per-class externally
    """
    _webHandlers = {}

    @classmethod
    def addWebHandler(cls, name, handler):
        cls._webHandlers[name] = handler

    @classmethod
    def removeWebHandler(cls, name):
        if name in cls._webHandlers:
            del cls._webHandlers[name]

    @classmethod
    def getWebHandler(cls, name):
        if name:
            handler = cls._webHandlers.get(name)
        else:
            handler = None
        if not handler:
            LOG_WARNING("Wrong web-client handler's name '%s'" % name)
        return handler
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\wgnc\common.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:34 Støední Evropa (letní èas)
