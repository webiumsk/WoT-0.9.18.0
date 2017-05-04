# 2017.05.04 15:25:58 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/MoonSphereAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import RegularAchievement
from abstract.mixins import NoProgressBar
from gui.shared.gui_items.dossier.achievements import validators

class MoonSphereAchievement(RegularAchievement, NoProgressBar):

    def __init__(self, dossier, value = None):
        super(MoonSphereAchievement, self).__init__('moonSphere', _AB.SINGLE, dossier, value)

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\MoonSphereAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:58 Støední Evropa (letní èas)
