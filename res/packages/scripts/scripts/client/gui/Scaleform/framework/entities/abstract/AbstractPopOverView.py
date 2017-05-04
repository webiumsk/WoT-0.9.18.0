# 2017.05.04 15:24:45 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/AbstractPopOverView.py
from gui.Scaleform.daapi.view.meta.PopOverViewMeta import PopOverViewMeta
from gui.shared.events import HidePopoverEvent

class AbstractPopOverView(PopOverViewMeta):

    def __init__(self, ctx = None):
        super(AbstractPopOverView, self).__init__()

    def _populate(self):
        super(AbstractPopOverView, self)._populate()
        self.addListener(HidePopoverEvent.HIDE_POPOVER, self.__handlerHidePopover)

    def __handlerHidePopover(self, event):
        self.destroy()

    def _dispose(self):
        self.removeListener(HidePopoverEvent.HIDE_POPOVER, self.__handlerHidePopover)
        super(AbstractPopOverView, self)._dispose()
        self.fireEvent(HidePopoverEvent(HidePopoverEvent.POPOVER_DESTROYED))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\AbstractPopOverView.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:45 Støední Evropa (letní èas)
