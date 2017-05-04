# 2017.05.04 15:24:27 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortDeclarationOfWarWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortDeclarationOfWarWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onDirectonChosen(self, directionUID):
        self._printOverrideError('onDirectonChosen')

    def onDirectionSelected(self):
        self._printOverrideError('onDirectionSelected')

    def as_setupHeaderS(self, title, description):
        if self._isDAAPIInited():
            return self.flashObject.as_setupHeader(title, description)

    def as_setupClansS(self, myClan, enemyClan):
        """
        :param myClan: Represented by ClanInfoVO (AS)
        :param enemyClan: Represented by ClanInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setupClans(myClan, enemyClan)

    def as_setDirectionsS(self, data):
        """
        :param data: Represented by Vector.<ConnectedDirectionsVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDirections(data)

    def as_selectDirectionS(self, uid):
        if self._isDAAPIInited():
            return self.flashObject.as_selectDirection(uid)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FortDeclarationOfWarWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:27 St�edn� Evropa (letn� �as)
