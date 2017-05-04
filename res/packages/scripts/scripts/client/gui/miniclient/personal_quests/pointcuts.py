# 2017.05.04 15:21:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/personal_quests/pointcuts.py
import aspects
from helpers import aop

class OnViewPopulate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.server_events.QuestsPersonalWelcomeView', 'QuestsPersonalWelcomeView', '_populate', aspects=(aspects.OnViewPopulate,))


class PersonalQuestsTabSelect(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.server_events.EventsWindow', 'EventsWindow', 'onTabSelected', aspects=(aspects.PersonalQuestsTabSelect,))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\personal_quests\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:51 Støední Evropa (letní èas)
