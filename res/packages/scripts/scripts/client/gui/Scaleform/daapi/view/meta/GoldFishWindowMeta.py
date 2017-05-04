# 2017.05.04 15:24:30 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/GoldFishWindowMeta.py
from gui.Scaleform.daapi.view.meta.SimpleWindowMeta import SimpleWindowMeta

class GoldFishWindowMeta(SimpleWindowMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleWindowMeta
    """

    def eventHyperLinkClicked(self):
        self._printOverrideError('eventHyperLinkClicked')

    def as_setWindowTextsS(self, header, eventTitle, eventText, eventLink):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTexts(header, eventTitle, eventText, eventLink)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\GoldFishWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:30 Støední Evropa (letní èas)
