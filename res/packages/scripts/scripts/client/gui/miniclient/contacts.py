# 2017.05.04 15:21:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/contacts.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from helpers import aop

class _CreateSquadAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        g_eventBus.handleEvent(events.LoadViewEvent(VIEW_ALIAS.SQUAD_PROMO_WINDOW), scope=EVENT_BUS_SCOPE.LOBBY)


class CreateSquadPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.user_cm_handlers', 'BaseUserCMHandler', 'createSquad', aspects=(_CreateSquadAspect,))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\contacts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:47 Støední Evropa (letní èas)
