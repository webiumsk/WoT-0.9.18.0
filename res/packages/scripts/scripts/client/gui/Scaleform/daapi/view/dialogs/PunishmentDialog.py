# 2017.05.04 15:22:49 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/PunishmentDialog.py
from gui.Scaleform.daapi.view.meta.PunishmentDialogMeta import PunishmentDialogMeta

class PunishmentDialog(PunishmentDialogMeta):

    def __init__(self, meta, handler):
        super(PunishmentDialog, self).__init__(meta.getMessage(), meta.getTitle(), meta.getButtonLabels(), meta.getCallbackWrapper(handler))
        self.__msgTitle = meta.getMsgTitle()

    def _populate(self):
        super(PunishmentDialog, self)._populate()
        self.as_setMsgTitleS(self.__msgTitle)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\dialogs\PunishmentDialog.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:49 Støední Evropa (letní èas)
