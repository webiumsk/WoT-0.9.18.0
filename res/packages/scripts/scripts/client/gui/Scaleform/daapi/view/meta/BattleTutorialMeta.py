# 2017.05.04 15:24:18 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleTutorialMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleTutorialMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_populateProgressBarS(self, currentChapter, totalChapters):
        if self._isDAAPIInited():
            return self.flashObject.as_populateProgressBar(currentChapter, totalChapters)

    def as_setTrainingProgressBarS(self, mask):
        if self._isDAAPIInited():
            return self.flashObject.as_setTrainingProgressBar(mask)

    def as_setChapterProgressBarS(self, totalSteps, mask):
        if self._isDAAPIInited():
            return self.flashObject.as_setChapterProgressBar(totalSteps, mask)

    def as_showGreetingS(self, targetID, title, description):
        if self._isDAAPIInited():
            return self.flashObject.as_showGreeting(targetID, title, description)

    def as_setChapterInfoS(self, description):
        if self._isDAAPIInited():
            return self.flashObject.as_setChapterInfo(description)

    def as_showNextTaskS(self, taskID, text, prevDone):
        if self._isDAAPIInited():
            return self.flashObject.as_showNextTask(taskID, text, prevDone)

    def as_showHintS(self, hintID, text, imagePath, imageAltPath):
        if self._isDAAPIInited():
            return self.flashObject.as_showHint(hintID, text, imagePath, imageAltPath)

    def as_hideGreetingS(self, targetID):
        if self._isDAAPIInited():
            return self.flashObject.as_hideGreeting(targetID)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BattleTutorialMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:18 St�edn� Evropa (letn� �as)
