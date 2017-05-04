# 2017.05.04 15:26:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/helpers/CallbackDelayer.py
import BigWorld
import functools

class CallbackDelayer(object):

    def __init__(self):
        self.__callbacks = {}

    def destroy(self):
        self.clearCallbacks()

    def clearCallbacks(self):
        for callbackFunc, callbackId in self.__callbacks.iteritems():
            if callbackId is not None:
                BigWorld.cancelCallback(callbackId)

        self.__callbacks = {}
        return

    def __funcWrapper(self, func, *args, **kwargs):
        del self.__callbacks[func]
        desiredDelay = func(*args, **kwargs)
        if desiredDelay is not None and desiredDelay >= 0:
            curId = BigWorld.callback(desiredDelay, functools.partial(self.__funcWrapper, func, *args, **kwargs))
            self.__callbacks[func] = curId
        return

    def delayCallback(self, seconds, func, *args, **kwargs):
        curId = self.__callbacks.get(func)
        if curId is not None:
            BigWorld.cancelCallback(curId)
            del self.__callbacks[func]
        curId = BigWorld.callback(seconds, functools.partial(self.__funcWrapper, func, *args, **kwargs))
        self.__callbacks[func] = curId
        return

    def stopCallback(self, func):
        curId = self.__callbacks.get(func)
        if curId is not None:
            BigWorld.cancelCallback(curId)
            del self.__callbacks[func]
        return

    def hasDelayedCallback(self, func):
        return func in self.__callbacks


class TimeDeltaMeter(object):

    def __init__(self, timeFunc = BigWorld.time):
        self.__timeFunc = timeFunc
        self.__prevTime = timeFunc()

    def measureDeltaTime(self):
        time = self.__timeFunc()
        deltaTime = time - self.__prevTime
        self.__prevTime = time
        return deltaTime
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\helpers\CallbackDelayer.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:37 Støední Evropa (letní èas)
