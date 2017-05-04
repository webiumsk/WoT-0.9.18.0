# 2017.05.04 15:23:45 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileAchievementSection.py
from gui.Scaleform.daapi.view.meta.ProfileAchievementSectionMeta import ProfileAchievementSectionMeta
from gui.shared.utils.RareAchievementsCache import g_rareAchievesCache

class ProfileAchievementSection(ProfileAchievementSectionMeta):

    def __init__(self, *args):
        super(ProfileAchievementSection, self).__init__(*args)
        g_rareAchievesCache.onImageReceived += self._onRareImageReceived

    def _onRareImageReceived(self, imgType, rareID, imageData):
        pass

    def _disposeRequester(self):
        g_rareAchievesCache.onImageReceived -= self._onRareImageReceived
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\profile\ProfileAchievementSection.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:45 Støední Evropa (letní èas)
