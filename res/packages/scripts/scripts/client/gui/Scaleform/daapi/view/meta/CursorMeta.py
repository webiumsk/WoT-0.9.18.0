# 2017.05.04 15:24:22 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CursorMeta.py
from gui.Scaleform.framework.entities.View import View

class CursorMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def as_setCursorS(self, cursor):
        if self._isDAAPIInited():
            return self.flashObject.as_setCursor(cursor)

    def as_showCursorS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showCursor()

    def as_hideCursorS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideCursor()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\CursorMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:22 Støední Evropa (letní èas)
