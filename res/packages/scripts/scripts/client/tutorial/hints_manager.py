# 2017.05.04 15:27:42 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/tutorial/hints_manager.py
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from tutorial import settings
from tutorial.control.functional import FunctionalConditions
from tutorial.data.hints import HintProps
from tutorial.doc_loader.parsers import HintsParser
from debug_utils import LOG_DEBUG
from tutorial.gui.Scaleform.hints.proxy import HintsProxy
_DESCRIPTOR_PATH = '{0:>s}/once-only-hints.xml'.format(settings.DOC_DIRECTORY)

class HintsManager(object):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(HintsManager, self).__init__()
        self._data = None
        self._gui = None
        self.__activeHints = {}
        return

    def start(self):
        self.__loadHintsData()
        if self._data.hintsCount == 0:
            return False
        self._gui = HintsProxy()
        self._gui.init()
        self._gui.loadConfig(self._data.getGuiFilePath())
        self._gui.onHintClicked += self.__onGUIInput
        self._gui.onHintItemFound += self.__onItemFound
        self._gui.onHintItemLost += self.__onItemLost
        return True

    def stop(self):
        if self._data is not None:
            self._data = None
        for itemID in self.__activeHints.keys():
            self.__hideHint(itemID)

        if self._gui is not None:
            self._gui.fini()
        self._gui = None
        return

    def stopOnceOnlyHint(self, itemID):
        if self._data is None:
            return
        else:
            hint = self._data.hintForItem(itemID)
            if hint is not None:
                self._data.markAsShown(hint)
                self.settingsCore.serverSettings.setOnceOnlyHintsSettings({hint['hintID']: 1})
            return

    def __loadHintsData(self):
        LOG_DEBUG('Hints are loading')
        shownHints = self.settingsCore.serverSettings.getOnceOnlyHintsSettings()
        shownHints = [ key for key, value in shownHints.iteritems() if value == 1 ]
        self._data = HintsParser.parse(_DESCRIPTOR_PATH, shownHints)

    def __showHint(self, hint):
        text = hint['text']
        uniqueID = hintID = hint['hintID']
        props = HintProps(uniqueID, hintID, hint['itemID'], text, True, hint['arrow'], None)
        self._gui.showHint(props)
        self.__activeHints[hint['itemID']] = hint
        return

    def __hideHint(self, itemID):
        if itemID in self.__activeHints:
            hint = self.__activeHints[itemID]
            self._gui.hideHint(hint['hintID'])
            del self.__activeHints[itemID]

    def __onGUIInput(self, event):
        itemID = event.getTargetID()
        if itemID in self.__activeHints:
            self.__hideHint(itemID)
            self.stopOnceOnlyHint(itemID)
            if self._data.hintsCount == 0:
                self.stop()

    def __onItemFound(self, itemID):
        hint = self._data.hintForItem(itemID)
        if hint is not None and itemID not in self.__activeHints and self.__checkConditions(hint):
            self.__showHint(hint)
        return

    def __onItemLost(self, itemID):
        if itemID in self.__activeHints:
            self.__hideHint(itemID)

    def __checkConditions(self, hint):
        conditions = hint['conditions']
        if conditions is None:
            return True
        else:
            return FunctionalConditions(conditions).allConditionsOk()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\hints_manager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:42 St�edn� Evropa (letn� �as)
