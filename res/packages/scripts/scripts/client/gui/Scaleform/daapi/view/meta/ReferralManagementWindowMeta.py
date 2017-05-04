# 2017.05.04 15:24:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ReferralManagementWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ReferralManagementWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onInvitesManagementLinkClick(self):
        self._printOverrideError('onInvitesManagementLinkClick')

    def inviteIntoSquad(self, referralID):
        self._printOverrideError('inviteIntoSquad')

    def as_setDataS(self, data):
        """
        :param data: Represented by RefManagementWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setTableDataS(self, referrals):
        """
        :param referrals: Represented by DataProvider (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTableData(referrals)

    def as_setAwardDataDataS(self, data):
        """
        :param data: Represented by AwardDataDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setAwardDataData(data)

    def as_setProgressDataS(self, data):
        """
        :param data: Represented by ComplexProgressIndicatorVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressData(data)

    def as_showAlertS(self, alertStr):
        if self._isDAAPIInited():
            return self.flashObject.as_showAlert(alertStr)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ReferralManagementWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:36 Støední Evropa (letní èas)
