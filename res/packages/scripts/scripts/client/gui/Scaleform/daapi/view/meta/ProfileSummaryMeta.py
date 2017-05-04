# 2017.05.04 15:24:34 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileSummaryMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileAchievementSection import ProfileAchievementSection

class ProfileSummaryMeta(ProfileAchievementSection):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ProfileAchievementSection
    """

    def getPersonalScoreWarningText(self, data):
        self._printOverrideError('getPersonalScoreWarningText')

    def getGlobalRating(self, userName):
        self._printOverrideError('getGlobalRating')

    def as_setUserDataS(self, data):
        """
        :param data: Represented by ProfileUserVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setUserData(data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ProfileSummaryMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:34 Støední Evropa (letní èas)
