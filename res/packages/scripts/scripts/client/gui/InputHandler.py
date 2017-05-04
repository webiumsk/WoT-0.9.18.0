# 2017.05.04 15:21:00 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/InputHandler.py
import Event
g_instance = None

class _InputHandler:
    onKeyDown = Event.Event()
    onKeyUp = Event.Event()

    def handleKeyEvent(self, event):
        if event.isKeyDown():
            self.onKeyDown(event)
        else:
            self.onKeyUp(event)


g_instance = _InputHandler()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\InputHandler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:00 Støední Evropa (letní èas)
