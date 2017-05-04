# 2017.05.04 15:24:48 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/VoiceChatManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class VoiceChatManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def isPlayerSpeaking(self, accountDBID):
        self._printOverrideError('isPlayerSpeaking')

    def isVivox(self):
        self._printOverrideError('isVivox')

    def isYY(self):
        self._printOverrideError('isYY')

    def isVOIPEnabled(self):
        self._printOverrideError('isVOIPEnabled')

    def as_onPlayerSpeakS(self, accountDBID, isSpeak, isHimseljoinUnitButtonf):
        if self._isDAAPIInited():
            return self.flashObject.as_onPlayerSpeak(accountDBID, isSpeak, isHimseljoinUnitButtonf)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\VoiceChatManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:48 Støední Evropa (letní èas)
