# 2017.05.04 15:28:09 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/web_client_api/commands/strongholds.py
from collections import namedtuple
from command import SchemeValidator, CommandHandler, instantiateObject
_StrongholdsBattleCommand = namedtuple('_StrongholdsBattleCommand', ('action', 'custom_parameters'))
_StrongholdsBattleCommand.__new__.__defaults__ = (None, None)
_StrongholdsBattleCommandScheme = {'required': (('action', basestring),)}
_StrongholdsJoinBattleCommand = namedtuple('_StrongholdsJoinBattleCommand', ('unit_id', 'periphery_id'))
_StrongholdsJoinBattleCommand.__new__.__defaults__ = (None, None)
_StrongholdsJoinBattleScheme = {'required': (('unit_id', (int, long)), ('periphery_id', (int, long)))}

class StrongholdsBattleCommand(_StrongholdsBattleCommand, SchemeValidator):
    """
    Represents web command for playing sound by id.
    """

    def __init__(self, *args, **kwargs):
        super(StrongholdsBattleCommand, self).__init__(_StrongholdsBattleCommandScheme)


class StrongholdsJoinBattleCommand(_StrongholdsJoinBattleCommand, SchemeValidator):
    """
    Represents web command for joining Strongholds battle.
    """

    def __init__(self, *args, **kwargs):
        super(StrongholdsJoinBattleCommand, self).__init__(_StrongholdsJoinBattleScheme)


def createStrongholdsBattleHandler(handlerFunc):
    data = {'name': 'strongholds_battle',
     'cls': StrongholdsBattleCommand,
     'handler': handlerFunc}
    return instantiateObject(CommandHandler, data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\web_client_api\commands\strongholds.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:09 St�edn� Evropa (letn� �as)
