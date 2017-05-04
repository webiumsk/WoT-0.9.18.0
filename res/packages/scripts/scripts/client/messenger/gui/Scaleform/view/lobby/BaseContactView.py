# 2017.05.04 15:27:07 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/view/lobby/BaseContactView.py
from debug_utils import LOG_ERROR
from messenger.gui.Scaleform.meta.BaseContactViewMeta import BaseContactViewMeta

class BaseContactView(BaseContactViewMeta):

    def __init__(self):
        super(BaseContactView, self).__init__()

    def _dispose(self):
        super(BaseContactView, self)._dispose()

    def onCancel(self):
        pass

    def _populate(self):
        super(BaseContactView, self)._populate()
        self.as_setInitDataS(self._getInitDataObject())

    def _getInitDataObject(self):
        LOG_ERROR('this method have to be overridden!')
        return self._getDefaultInitData('', '', '', '', '')

    def _getDefaultInitData(self, mainLbl, btOkLbl, btnCancelLbl, btOkTooltip, btnCancelTooltip):
        return {'btOkLbl': btOkLbl,
         'btnCancelLbl': btnCancelLbl,
         'mainLbl': mainLbl,
         'btOkTooltip': btOkTooltip,
         'btnCancelTooltip': btnCancelTooltip}
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\gui\Scaleform\view\lobby\BaseContactView.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:07 Støední Evropa (letní èas)
