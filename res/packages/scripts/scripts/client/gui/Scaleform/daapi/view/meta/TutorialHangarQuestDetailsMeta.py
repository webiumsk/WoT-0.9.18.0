# 2017.05.04 15:24:40 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TutorialHangarQuestDetailsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TutorialHangarQuestDetailsMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def requestQuestInfo(self, questID):
        self._printOverrideError('requestQuestInfo')

    def showTip(self, id, type):
        self._printOverrideError('showTip')

    def getSortedTableData(self, data):
        self._printOverrideError('getSortedTableData')

    def as_updateQuestInfoS(self, data):
        """
        :param data: Represented by TutorialHangarQuestDetailsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateQuestInfo(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\TutorialHangarQuestDetailsMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:40 Støední Evropa (letní èas)
