# 2017.05.04 15:26:26 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/utils/requesters/common.py
import BigWorld

class RequestProcessor(object):
    """
    Incapsulates delayed server request
    """

    def __init__(self, delay, callback):
        """
        :param delay: delay before calling the callback(in seconds)
        :param callback: callback to be called
        """
        self.__callback = callback
        self.__fired = False
        self.__bwCallbackID = BigWorld.callback(delay, self.__cooldownCallback)

    @property
    def isFired(self):
        """
        Returns to be called flag
        :return: boolean value
        """
        return self.__fired

    def cancel(self):
        """
        Cancel delayed callback
        """
        if self.__bwCallbackID is not None:
            BigWorld.cancelCallback(self.__bwCallbackID)
            self.__bwCallbackID = None
        return

    def __cooldownCallback(self):
        """
        Proxy-function for delayed callback. Cancel callback and return result
        """
        self.__bwCallbackID = None
        self.__fired = True
        self.__callback()
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\utils\requesters\common.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:26 Støední Evropa (letní èas)
