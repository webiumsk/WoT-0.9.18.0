# 2017.05.04 15:26:03 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/mixins/Quest.py
from gui.shared.gui_items.dossier.achievements import validators

class Quest(object):

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.questHasThisAchievementAsBonus(name, block) or validators.alreadyAchieved(cls, name, block, dossier)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\abstract\mixins\Quest.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:03 Støední Evropa (letní èas)
