# 2017.05.04 15:28:01 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/quests/proxy.py
from tutorial.gui import GUI_EFFECT_NAME
from tutorial.gui.Scaleform import effects_player
from tutorial.gui.Scaleform.lobby.proxy import SfLobbyProxy
from tutorial.gui.Scaleform.quests import settings
from tutorial.gui.commands import GUICommandsFactory

class SfQuestsProxy(SfLobbyProxy):

    def __init__(self):
        effects = {GUI_EFFECT_NAME.SHOW_WINDOW: effects_player.ShowWindowEffect(settings.WINDOW_ALIAS_MAP),
         GUI_EFFECT_NAME.UPDATE_CONTENT: effects_player.UpdateContentEffect(),
         GUI_EFFECT_NAME.SHOW_HINT: effects_player.ShowChainHint()}
        super(SfQuestsProxy, self).__init__(effects_player.EffectsPlayer(effects))
        self._commands = GUICommandsFactory()

    def fini(self):
        self._commands = None
        super(SfQuestsProxy, self).fini()
        return

    def getViewSettings(self):
        return settings.QUESTS_VIEW_SETTINGS

    def getViewsAliases(self):
        return settings.WINDOW_ALIAS_MAP

    def invokeCommand(self, command):
        self._commands.invoke(None, command)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\gui\Scaleform\quests\proxy.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:01 St�edn� Evropa (letn� �as)
