# 2017.05.04 15:24:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsContentTabsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsContentTabsMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onSelectTab(self, id):
        self._printOverrideError('onSelectTab')

    def as_selectTabS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_selectTab(index)

    def as_setTabsS(self, data):
        """
        :param data: Represented by TabsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTabs(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\QuestsContentTabsMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:35 Støední Evropa (letní èas)
