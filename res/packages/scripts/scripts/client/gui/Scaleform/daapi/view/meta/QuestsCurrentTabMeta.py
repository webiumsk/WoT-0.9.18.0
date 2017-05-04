# 2017.05.04 15:24:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsCurrentTabMeta.py
from gui.Scaleform.daapi.view.lobby.server_events.QuestsTab import QuestsTab

class QuestsCurrentTabMeta(QuestsTab):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends QuestsTab
    """

    def sort(self, type, hideDone):
        self._printOverrideError('sort')

    def getSortedTableData(self, tableData):
        self._printOverrideError('getSortedTableData')

    def getQuestInfo(self, questID):
        self._printOverrideError('getQuestInfo')

    def collapse(self, id):
        self._printOverrideError('collapse')

    def as_showNoDataS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showNoData(text)

    def as_showWaitingS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showWaiting(value)

    def as_showNoSelectS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showNoSelect()

    def as_updateQuestInfoS(self, data):
        """
        :param data: Represented by QuestDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateQuestInfo(data)

    def as_setSelectedQuestS(self, questID):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedQuest(questID)

    def as_setTabBarDataS(self, value):
        """
        :param value: Represented by Vector.<TabBarDataVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTabBarData(value)

    def as_setTabBarCountersS(self, value):
        """
        :param value: Represented by Vector.<int> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTabBarCounters(value)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\QuestsCurrentTabMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:35 Støední Evropa (letní èas)
