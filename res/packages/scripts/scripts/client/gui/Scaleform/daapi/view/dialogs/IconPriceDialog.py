# 2017.05.04 15:22:49 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/IconPriceDialog.py
from gui.Scaleform.daapi.view.meta.IconPriceDialogMeta import IconPriceDialogMeta
from gui.Scaleform.locale.DIALOGS import DIALOGS
from helpers import i18n

class IconPriceDialog(IconPriceDialogMeta):

    def __init__(self, meta, handler):
        super(IconPriceDialog, self).__init__(meta, handler)

    def _populate(self):
        super(IconPriceDialog, self)._populate()
        self.as_setPriceLabelS(i18n.makeString(DIALOGS.REMOVECONFIRMATIONNOTREMOVABLEGOLD_MESSAGEPRICE))
        self.as_setMessagePriceS(self._meta.getMessagePrice(), 'gold', self._meta.getAction())
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\dialogs\IconPriceDialog.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:49 Støední Evropa (letní èas)
