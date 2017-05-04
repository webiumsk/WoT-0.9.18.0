# 2017.05.04 15:24:44 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/WaitingView.py
import Keys
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
from gui import InputHandler
from gui.Scaleform.framework.entities.View import View
from gui.Scaleform.daapi.view.meta.WaitingViewMeta import WaitingViewMeta

class WaitingView(WaitingViewMeta):

    def __init__(self):
        super(WaitingView, self).__init__()
        InputHandler.g_instance.onKeyUp += self.handleKeyUpEvent
        self.__callback = None
        return

    def handleKeyUpEvent(self, event):
        if event.key == Keys.KEY_ESCAPE:
            if self.__callback:
                self.__callback()

    def close(self):
        self.__callback = None
        try:
            self.hideS(None)
        except Exception:
            LOG_ERROR('There is error while trying to close waiting')
            LOG_CURRENT_EXCEPTION()

        return

    def destroy(self):
        self.__callback = None
        InputHandler.g_instance.onKeyUp -= self.handleKeyUpEvent
        super(WaitingView, self).destroy()
        return

    def setCallback(self, value):
        self.__callback = value

    def cancelCallback(self):
        self.__callback = None
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\WaitingView.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:44 St�edn� Evropa (letn� �as)
