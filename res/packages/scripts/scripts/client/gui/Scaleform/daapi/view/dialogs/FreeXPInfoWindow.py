# 2017.05.04 15:22:49 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/FreeXPInfoWindow.py
from gui.Scaleform.daapi.view.meta.FreeXPInfoWindowMeta import FreeXPInfoWindowMeta
__author__ = 'd_savitski'

class FreeXPInfoWindow(FreeXPInfoWindowMeta):

    def __init__(self, ctx = None):
        super(FreeXPInfoWindow, self).__init__()
        self.meta = ctx.get('meta')
        self.handler = ctx.get('handler')

    def _populate(self):
        super(FreeXPInfoWindow, self)._populate()
        self.as_setTitleS(self.meta.getTitle())
        self.as_setSubmitLabelS(self.meta.getSubmitLbl())
        self.as_setTextS(self.meta.getTextInfo())

    def onWindowClose(self):
        self.handler(True)
        self.destroy()

    def onSubmitButton(self):
        self.onWindowClose()

    def onCancelButton(self):
        self.onWindowClose()

    def _dispose(self):
        super(FreeXPInfoWindow, self)._dispose()
        self.handler = None
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\dialogs\FreeXPInfoWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:49 Støední Evropa (letní èas)
