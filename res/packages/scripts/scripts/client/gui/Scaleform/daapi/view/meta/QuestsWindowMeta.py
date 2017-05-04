# 2017.05.04 15:24:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class QuestsWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onTabSelected(self, tabID):
        self._printOverrideError('onTabSelected')

    def as_loadViewS(self, flashAlias, pyAlias):
        if self._isDAAPIInited():
            return self.flashObject.as_loadView(flashAlias, pyAlias)

    def as_selectTabS(self, tabID):
        if self._isDAAPIInited():
            return self.flashObject.as_selectTab(tabID)

    def as_initS(self, data):
        """
        :param data: Represented by TabsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\QuestsWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:35 Støední Evropa (letní èas)
