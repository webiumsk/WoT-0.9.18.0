# 2017.05.04 15:27:58 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/battle_v2/proxy.py
import weakref
from debug_utils import LOG_CURRENT_EXCEPTION
from gui import makeHtmlString
from gui.Scaleform.daapi.view.battle.shared import indicators
from gui.Scaleform.framework import g_entitiesFactories, ViewTypes
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from gui.app_loader.decorators import sf_battle
from gui.battle_control.arena_info import player_format
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from helpers import dependency
from helpers import i18n
from skeletons.gui.battle_session import IBattleSessionProvider
from tutorial.doc_loader import gui_config
from tutorial.gui import GUIProxy, GUI_EFFECT_NAME
from tutorial.gui.Scaleform import effects_player as _shared_player
from tutorial.gui.Scaleform.battle_v2 import settings, effects
_Event = events.ComponentEvent
_COMPONENT_EFFECTS = (GUI_EFFECT_NAME.SHOW_GREETING, GUI_EFFECT_NAME.SHOW_HINT, GUI_EFFECT_NAME.NEXT_TASK)
_REQUIRED_BATTLE_ALIASES = {BATTLE_VIEW_ALIASES.BATTLE_TUTORIAL, BATTLE_VIEW_ALIASES.MINIMAP, BATTLE_VIEW_ALIASES.MARKERS_2D}

class TutorialFullNameFormatter(player_format.PlayerFullNameFormatter):

    @staticmethod
    def _normalizePlayerName(name):
        if name.startswith('#battle_tutorial:'):
            name = i18n.makeString(name)
        return name


class SfBattleProxy(GUIProxy):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(SfBattleProxy, self).__init__()
        self.__config = None
        self.__effects = _shared_player.EffectsPlayer({GUI_EFFECT_NAME.SHOW_DIALOG: _shared_player.ShowDialogEffect(settings.DIALOG_ALIAS_MAP),
         GUI_EFFECT_NAME.SHOW_GREETING: effects.ShowGreetingEffect(),
         GUI_EFFECT_NAME.SHOW_HINT: effects.ShowHintEffect(),
         GUI_EFFECT_NAME.NEXT_TASK: effects.NextTaskEffect()})
        self.__tutorial = None
        self.__minimap = None
        self.__markers2D = None
        self.__registered = set()
        self.__isGuiLoaded = False
        return

    @sf_battle
    def app(self):
        return None

    @property
    def config(self):
        return self.__config

    @property
    def effects(self):
        return self.__effects

    @staticmethod
    def getViewSettings():
        return settings.BATTLE_VIEW_SETTINGS

    def getMarkers2DPlugin(self):
        return self.__markers2D

    def getMinimapPlugin(self):
        return self.__minimap

    @staticmethod
    def getDirectionIndicator():
        """
        Gets object of direction indicator GUI component.
        :return: instance of DirectionIndicator or None.
        """
        indicator = None
        try:
            indicator = indicators.createDirectIndicator()
        except:
            LOG_CURRENT_EXCEPTION()

        return indicator

    def init(self):
        """
        Initializes GUI.
        :return: True if gui proxy is inited, otherwise - False.
        """
        result = False
        addListener = g_eventBus.addListener
        addListener(_Event.COMPONENT_REGISTERED, self.__onComponentRegistered, scope=EVENT_BUS_SCOPE.GLOBAL)
        addListener(_Event.COMPONENT_UNREGISTERED, self.__onComponentUnregistered, scope=EVENT_BUS_SCOPE.GLOBAL)
        if self.app is not None:
            proxy = weakref.proxy(self.app)
            for effect in self.__effects.filterByName(GUI_EFFECT_NAME.SHOW_DIALOG):
                effect.setApplication(proxy)

            addSettings = g_entitiesFactories.addSettings
            try:
                for item in self.getViewSettings():
                    addSettings(item)

                result = True
            except Exception:
                LOG_CURRENT_EXCEPTION()

        if result:
            self.sessionProvider.getCtx().setPlayerFullNameFormatter(TutorialFullNameFormatter())
        return result

    def fini(self):
        """
        Finalizes GUI.
        """
        self.eManager.clear()
        self.__effects.clear()
        self.__registered.clear()
        self.__tutorial = None
        self.__minimap = None
        self.__markers2D = None
        removeSettings = g_entitiesFactories.removeSettings
        for item in self.getViewSettings():
            removeSettings(item.alias)

        removeListener = g_eventBus.removeListener
        removeListener(_Event.COMPONENT_REGISTERED, self.__onComponentRegistered, scope=EVENT_BUS_SCOPE.GLOBAL)
        removeListener(_Event.COMPONENT_UNREGISTERED, self.__onComponentUnregistered, scope=EVENT_BUS_SCOPE.GLOBAL)
        self.sessionProvider.getCtx().resetPlayerFullNameFormatter()
        return

    def clear(self):
        """
        GUI clear: stops effects, clear information of current chapter in
        header, close all opened windows.
        """
        self.__effects.stopAll()

    def loadConfig(self, filePath):
        """
        Reads specified config by given GUI API.
        :param filePath: relative file path to GUI config.
        """
        self.__config = gui_config.readConfig(filePath)

    def reloadConfig(self, filePath):
        """
        Clear file cache and reads specified config by given GUI API.
        :param filePath: relative file path to GUI config.
        """
        self.__config = gui_config.readConfig(filePath, forced=True)

    def getSceneID(self):
        """
        Gets scene ID for current view.
        :return: string containing unique name of scene. Battle tutorial has
        one scene only.
        """
        return 'Battle'

    def goToScene(self, sceneID):
        """
        Go to scene by sceneID.
        :param sceneID: string containing unique name of scene.
        """
        raise RuntimeError('Battle tutorial has one scene only.')

    def playEffect(self, effectName, args, itemRef = None, containerRef = None):
        """
        Play effect: show dialog, show hint, ...
        :param effectName: name of effect - PopUp, Hint, ...
        :param args: list of effect arguments.
        :param itemRef: gui item ID, if it is not None than effect is applied
            to element.
        :param containerRef: gui item ID for container. Visible effect attaches
            to container, if it defined.
        """
        return self.__effects.play(effectName, args)

    def stopEffect(self, effectName, effectID):
        """
        Stop playing effect.
        :param effectName: name of effect - PopUp, Hint, ...
        :param effectID: effect unique name.
        """
        self.__effects.stop(effectName, effectID)

    def isEffectRunning(self, effectName, effectID = None):
        """
        Is effect still running.
        :param effectName: string unique name of effect. One of GUI_EFFECT_NAME.
        :param effectID: string unique ID of effect.
        :return: True if effect is playing, otherwise - False.
        """
        return self.__effects.isStillRunning(effectName, effectID=effectID)

    def clearScene(self):
        """
        Removes all pup-ups from stage.
        """
        app = self.app
        if app is None or app.containerManager is None:
            return
        else:
            app.containerManager.clear()
            return

    def isGuiDialogDisplayed(self):
        """
        Is standard gui dialog displayed.
        :return: bool.
        """
        app = self.app
        if app is None or app.containerManager is None:
            return False
        else:
            container = app.containerManager.getContainer(ViewTypes.TOP_WINDOW)
            result = False
            if container is not None:
                dialogCount = container.getViewCount(isModal=True)
                if dialogCount > 0:
                    if self.__effects.isStillRunning(GUI_EFFECT_NAME.SHOW_DIALOG):
                        dialogCount -= 1
                    result = dialogCount > 0
            return result

    def isTutorialDialogDisplayed(self, dialogID):
        """
        Is tutorial dialog displayed.
        :param dialogID: string containing unique name of dialog.
        :return: bool.
        """
        return self.__effects.isStillRunning(GUI_EFFECT_NAME.SHOW_DIALOG, effectID=dialogID)

    def isTutorialWindowDisplayed(self, windowID):
        """
        Is tutorial window displayed.
        :param windowID: string containing unique name of window.
        :return: bool.
        """
        return self.__effects.isStillRunning(GUI_EFFECT_NAME.SHOW_WINDOW, effectID=windowID)

    def setChapterInfo(self, title, description):
        if self.__tutorial is not None:
            try:
                text = makeHtmlString('html_templates:battle/tutorial', 'chapterDescription', ctx={'title': title,
                 'description': description})
                self.__tutorial.as_setChapterInfoS(text)
            except:
                LOG_CURRENT_EXCEPTION()

        return

    def setTrainingPeriod(self, currentIdx, total):
        if self.__tutorial is not None:
            self.__tutorial.as_populateProgressBarS(currentIdx, total)
        return

    def setTrainingProgress(self, mask):
        if self.__tutorial is not None:
            self.__tutorial.as_setTrainingProgressBarS(mask)
        return

    def setChapterProgress(self, total, mask):
        if self.__tutorial is not None:
            self.__tutorial.as_setChapterProgressBarS(total, mask)
        return

    def __onComponentRegistered(self, event):
        alias = event.alias
        self.__registered.add(alias)
        if alias == BATTLE_VIEW_ALIASES.BATTLE_TUTORIAL:
            proxy = weakref.proxy(event.componentPy)
            for effect in self.__effects.filterByName(*_COMPONENT_EFFECTS):
                effect.setComponent(proxy)

            self.__tutorial = proxy
        elif alias == BATTLE_VIEW_ALIASES.MINIMAP:
            plugin = event.componentPy.getPlugin('tutorial')
            if plugin is not None:
                self.__minimap = plugin
        elif alias == BATTLE_VIEW_ALIASES.MARKERS_2D:
            plugin = event.componentPy.getPlugin('tutorial')
            if plugin is not None:
                self.__markers2D = plugin
        if not self.__isGuiLoaded and self.__registered.issuperset(_REQUIRED_BATTLE_ALIASES):
            self.__isGuiLoaded = True
            self.onGUILoaded()
        return

    def __onComponentUnregistered(self, event):
        alias = event.alias
        if alias == BATTLE_VIEW_ALIASES.BATTLE_TUTORIAL:
            for effect in self.__effects.filterByName(*_COMPONENT_EFFECTS):
                effect.clear()

            self.__tutorial = None
        elif alias == BATTLE_VIEW_ALIASES.MINIMAP and self.__minimap is not None:
            self.__minimap.stop()
            self.__minimap = None
        elif alias == BATTLE_VIEW_ALIASES.MARKERS_2D and self.__markers2D is not None:
            self.__markers2D.stop()
            self.__markers2D = None
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\gui\Scaleform\battle_v2\proxy.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:59 St�edn� Evropa (letn� �as)
