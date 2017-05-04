# 2017.05.04 15:22:23 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/windows.py
from debug_utils import LOG_DEBUG, LOG_WARNING

class UIInterface(object):

    def __init__(self):
        self.uiHolder = None
        return

    def __del__(self):
        LOG_DEBUG('Deleted: %s' % self)

    def populateUI(self, proxy):
        self.uiHolder = proxy

    def dispossessUI(self):
        self.uiHolder = None
        return

    def call(self, methodName, args = None):
        if self.uiHolder:
            self.uiHolder.call(methodName, args)
        else:
            LOG_WARNING('Error to %s.call("%s", ...), check for possible memory leaks' % (self.__class__, methodName))

    def callNice(self, methodName, args = None):
        if self.uiHolder:
            self.uiHolder.callNice(methodName, args)
        else:
            LOG_WARNING('Error to %s.callJson("%s", ...), check for possible memory leaks' % (self.__class__, methodName))

    def respond(self, args = None):
        if self.uiHolder:
            self.uiHolder.respond(args)
        else:
            LOG_WARNING('Error to %s.respond(), check for possible memory leaks' % self.__class__)

    def setMovieVariable(self, path, value):
        if self.uiHolder:
            self.uiHolder.setMovieVariable(path, value)
        else:
            LOG_WARNING('Error to %s.setMovieVariable("%s", ...), check for possible memory leaks' % (self.__class__, path))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\windows.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:23 St�edn� Evropa (letn� �as)
