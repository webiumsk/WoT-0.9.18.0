# 2017.05.04 15:20:05 Støední Evropa (letní èas)
# Embedded file name: scripts/client/ReplayEvents.py
import Event

class _ReplayEvents(object):

    @property
    def isPlaying(self):
        return self.__isPlaying

    @property
    def isRecording(self):
        return self.__isRecording

    def __init__(self):
        self.onTimeWarpStart = Event.Event()
        self.onTimeWarpFinish = Event.Event()
        self.onPause = Event.Event()
        self.onMuteSound = Event.Event()
        self.onWatcherNotify = Event.Event()
        self.__isPlaying = False
        self.__isRecording = False

    def onRecording(self):
        self.__isRecording = True

    def onPlaying(self):
        self.__isPlaying = True


g_replayEvents = _ReplayEvents()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\ReplayEvents.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:05 Støední Evropa (letní èas)
