# 2017.05.04 15:23:57 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/server_events/QuestsTab.py
from gui.Scaleform.daapi.view.meta.QuestsTabMeta import QuestsTabMeta
from gui.server_events import caches

class QuestsTab(QuestsTabMeta):

    def __init__(self):
        super(QuestsTab, self).__init__()
        self._navInfo = caches.getNavInfo()

    def _selectQuest(self, questID):
        raise NotImplementedError

    def _invalidateEventsData(self):
        raise NotImplementedError

    def _dispose(self):
        self._navInfo = None
        super(QuestsTab, self)._dispose()
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\server_events\QuestsTab.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:57 Støední Evropa (letní èas)
