# 2017.05.04 15:21:44 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/game_control/state_tracker.py
import operator
from gui.shared import g_eventBus, events
from shared_utils import forEach
from skeletons.gui.game_control import IGameStateTracker, IGameController

class GameStateTracker(IGameStateTracker):
    """ Controllers tracker class that supports theirs registration and
    notification when game is switches to new state.
    """

    def __init__(self):
        super(GameStateTracker, self).__init__()
        self._controllers = []

    def init(self):
        g_eventBus.addListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.onLobbyInited)

    def fini(self):
        g_eventBus.removeListener(events.GUICommonEvent.LOBBY_VIEW_LOADED, self.onLobbyInited)
        del self._controllers[:]

    def onAccountShowGUI(self, ctx):
        self.onLobbyStarted(ctx)

    def onConnected(self):
        self._invoke('onConnected')

    def onDisconnected(self):
        self._invoke('onDisconnected')

    def onAvatarBecomePlayer(self):
        self._invoke('onAvatarBecomePlayer')

    def onAccountBecomePlayer(self):
        self._invoke('onAccountBecomePlayer')

    def onLobbyStarted(self, ctx):
        self._invoke('onLobbyStarted', ctx)

    def onLobbyInited(self, event):
        self._invoke('onLobbyInited', event)

    def addController(self, controller):
        if not isinstance(controller, IGameController):
            print 'Controller should implements IGameController'
        self._controllers.append(controller)

    def _invoke(self, method, *args):
        forEach(operator.methodcaller(method, *args), self._controllers)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\game_control\state_tracker.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:44 Støední Evropa (letní èas)
