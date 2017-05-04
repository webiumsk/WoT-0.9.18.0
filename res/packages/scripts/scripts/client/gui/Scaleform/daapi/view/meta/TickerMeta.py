# 2017.05.04 15:24:39 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TickerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TickerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def showBrowser(self, entryID):
        self._printOverrideError('showBrowser')

    def as_setItemsS(self, items):
        """
        :param items: Represented by Vector.<RSSEntryVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setItems(items)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\TickerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:39 Støední Evropa (letní èas)
