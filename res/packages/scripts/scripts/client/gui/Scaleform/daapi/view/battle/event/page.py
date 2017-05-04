# 2017.05.04 15:22:27 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/page.py
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage
from debug_utils import LOG_DEBUG

class EventBattlePage(ClassicPage):

    def _populate(self):
        super(EventBattlePage, self)._populate()
        LOG_DEBUG('Event battle page is created.')

    def _dispose(self):
        super(EventBattlePage, self)._dispose()
        LOG_DEBUG('Event battle page is destroyed.')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\event\page.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:27 Støední Evropa (letní èas)
