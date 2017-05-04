# 2017.05.04 15:28:34 Støední Evropa (letní èas)
# Embedded file name: scripts/common/invites.py
from enumerations import Enumeration
INVITE_TYPES = Enumeration('InviteTypes', ['BARTER',
 'TEAM',
 'CLAN',
 'TRAINING_ROOM',
 'PREBATTLE'])
_g_invitesConfig = {INVITE_TYPES.BARTER.index(): {'TTL': 900,
                               'keepInArchive': 3600,
                               'checkIgnore': True},
 INVITE_TYPES.TEAM.index(): {'TTL': -1,
                             'keepInArchive': -1,
                             'checkIgnore': True},
 INVITE_TYPES.CLAN.index(): {'TTL': -1,
                             'keepInArchive': -1,
                             'checkIgnore': True},
 INVITE_TYPES.TRAINING_ROOM.index(): {'TTL': 900,
                                      'keepInArchive': 3600,
                                      'checkIgnore': True},
 INVITE_TYPES.PREBATTLE.index(): {'TTL': 900,
                                  'keepInArchive': 3600,
                                  'checkIgnore': True}}
_g_defaultInviteConfig = {'TTL': -1,
 'keepInArchive': -1,
 'checkIgnore': True}

def getInviteConfig(inviteTypeIdx):
    return _g_invitesConfig.get(inviteTypeIdx, _g_defaultInviteConfig)


INVITE_STATUS = Enumeration('Invite statuses', ['accepted',
 'rejected',
 'invalid',
 'invalidTTL'])
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\invites.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:35 Støední Evropa (letní èas)
