# 2017.05.04 15:24:38 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SquadPromoWindowMeta.py
from gui.Scaleform.daapi.view.meta.SimpleWindowMeta import SimpleWindowMeta

class SquadPromoWindowMeta(SimpleWindowMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleWindowMeta
    """

    def onHyperlinkClick(self):
        self._printOverrideError('onHyperlinkClick')

    def as_setHyperlinkS(self, label):
        if self._isDAAPIInited():
            return self.flashObject.as_setHyperlink(label)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\SquadPromoWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:38 Støední Evropa (letní èas)
