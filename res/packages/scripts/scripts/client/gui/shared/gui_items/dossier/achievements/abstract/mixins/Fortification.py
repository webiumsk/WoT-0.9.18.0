# 2017.05.04 15:26:02 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/mixins/Fortification.py
from gui.shared.gui_items.dossier.achievements import validators

class Fortification(object):

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.requiresFortification()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\abstract\mixins\Fortification.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:02 St�edn� Evropa (letn� �as)
