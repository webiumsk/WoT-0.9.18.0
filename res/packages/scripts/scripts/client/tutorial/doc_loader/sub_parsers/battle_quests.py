# 2017.05.04 15:27:55 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/tutorial/doc_loader/sub_parsers/battle_quests.py
from tutorial.doc_loader import sub_parsers
from tutorial.doc_loader.sub_parsers import quests
from tutorial.control.quests.battle import triggers
from tutorial.data import effects
_EFFECT_TYPE = effects.EFFECT_TYPE

def _readUseItemsTriggerSection(xmlCtx, section, chapter, triggerID):
    return sub_parsers.readValidateVarTriggerSection(xmlCtx, section, triggerID, triggers.UseItemsTrigger)


def _readInstallItemsTriggerSection(xmlCtx, section, chapter, triggerID):
    return sub_parsers.readValidateVarTriggerSection(xmlCtx, section, triggerID, triggers.InstallItemsTrigger)


def init():
    sub_parsers.setEffectsParsers({'save-setting': quests.readSaveTutorialSettingSection})
    sub_parsers.setEntitiesParsers({'tutorial-setting': quests.readTutorialSettingSection})
    sub_parsers.setTriggersParsers({'tutorialIntSetting': quests.readTutorialIntSettingTriggerSection,
     'tutorialAccountSetting': quests.readTutorialAccountSettingTriggerSection,
     'useItem': _readUseItemsTriggerSection,
     'installItem': _readInstallItemsTriggerSection})
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\doc_loader\sub_parsers\battle_quests.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:55 St�edn� Evropa (letn� �as)
