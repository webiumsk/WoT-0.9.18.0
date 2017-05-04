# 2017.05.04 15:24:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileAchievementSectionMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import ProfileSection

class ProfileAchievementSectionMeta(ProfileSection):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ProfileSection
    """

    def as_setRareAchievementDataS(self, rareID, rareIconId):
        if self._isDAAPIInited():
            return self.flashObject.as_setRareAchievementData(rareID, rareIconId)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ProfileAchievementSectionMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:33 Støední Evropa (letní èas)
