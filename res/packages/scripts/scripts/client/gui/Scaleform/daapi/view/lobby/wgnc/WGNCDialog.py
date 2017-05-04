# 2017.05.04 15:24:12 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/wgnc/WGNCDialog.py
from gui.Scaleform.daapi.view.meta.WGNCDialogMeta import WGNCDialogMeta
from gui.wgnc import g_wgncProvider

class WGNCDialog(WGNCDialogMeta):

    def __init__(self, ctx = None):
        super(WGNCDialog, self).__init__()
        raise ctx or AssertionError('Context can be defined')
        self.__notID = ctx['notID']
        self.__target = ctx['target']

    def onWindowClose(self):
        self.destroy()

    def doAction(self, actionID, isButtonClicked):
        g_wgncProvider.doAction(self.__notID, actionID, self.__target)
        if isButtonClicked:
            self.destroy()

    def _populate(self):
        super(WGNCDialog, self)._populate()
        item = g_wgncProvider.getNotItemByName(self.__notID, self.__target)
        self.as_setTextS(item.getBody())
        self.as_setTitleS(item.getTopic())
        self.as_setButtonsS(item.getButtonsMap())

    def _dispose(self):
        self.__notID = None
        self.__target = None
        super(WGNCDialogMeta, self)._dispose()
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\wgnc\WGNCDialog.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:13 Støední Evropa (letní èas)
