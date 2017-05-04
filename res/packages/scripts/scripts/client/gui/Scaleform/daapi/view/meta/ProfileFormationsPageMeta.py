# 2017.05.04 15:24:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileFormationsPageMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection

class ProfileFormationsPageMeta(ProfileSection):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ProfileSection
    """

    def showFort(self):
        self._printOverrideError('showFort')

    def createFort(self):
        self._printOverrideError('createFort')

    def onClanLinkNavigate(self, code):
        self._printOverrideError('onClanLinkNavigate')

    def as_setClanInfoS(self, clanInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanInfo(clanInfo)

    def as_setFortInfoS(self, fortInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setFortInfo(fortInfo)

    def as_setClanEmblemS(self, clanIcon):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(clanIcon)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ProfileFormationsPageMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:33 Støední Evropa (letní èas)
