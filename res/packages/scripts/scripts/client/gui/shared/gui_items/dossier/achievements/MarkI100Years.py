# 2017.05.04 15:25:57 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/MarkI100Years.py
from abstract import ClassProgressAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from gui.shared.gui_items.dossier.achievements import validators

class MarkI100Years(ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        super(MarkI100Years, self).__init__('markI100Years', _AB.TOTAL, dossier, value)

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\MarkI100Years.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:25:57 Støední Evropa (letní èas)
