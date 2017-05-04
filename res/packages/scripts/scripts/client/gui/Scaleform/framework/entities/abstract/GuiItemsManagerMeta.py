# 2017.05.04 15:24:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/GuiItemsManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class GuiItemsManagerMeta(BaseDAAPIModule):

    def _getItemAttribute(self, itemTypeIdx, id, attrName):
        self._printOverrideError('_getItemAttribute')

    def _callItemMethod(self, itemTypeIdx, id, methodName, kargs):
        self._printOverrideError('_callItemMethod')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\GuiItemsManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:47 Støední Evropa (letní èas)
