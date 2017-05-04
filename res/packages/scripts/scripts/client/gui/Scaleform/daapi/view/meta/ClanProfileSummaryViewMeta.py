# 2017.05.04 15:24:20 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileSummaryViewMeta.py
from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileBaseView import ClanProfileBaseView

class ClanProfileSummaryViewMeta(ClanProfileBaseView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ClanProfileBaseView
    """

    def hyperLinkGotoMap(self):
        self._printOverrideError('hyperLinkGotoMap')

    def hyperLinkGotoDetailsMap(self):
        self._printOverrideError('hyperLinkGotoDetailsMap')

    def sendRequestHandler(self):
        self._printOverrideError('sendRequestHandler')

    def as_updateStatusS(self, data):
        """
        :param data: Represented by ClanProfileSummaryViewStatusVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateStatus(data)

    def as_updateGeneralBlockS(self, data):
        """
        :param data: Represented by ClanProfileSummaryBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateGeneralBlock(data)

    def as_updateFortBlockS(self, data):
        """
        :param data: Represented by ClanProfileSummaryBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateFortBlock(data)

    def as_updateGlobalMapBlockS(self, data):
        """
        :param data: Represented by ClanProfileSummaryBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateGlobalMapBlock(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ClanProfileSummaryViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:20 Støední Evropa (letní èas)
