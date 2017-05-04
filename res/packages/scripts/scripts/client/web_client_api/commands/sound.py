# 2017.05.04 15:28:09 Støední Evropa (letní èas)
# Embedded file name: scripts/client/web_client_api/commands/sound.py
from collections import namedtuple
from command import SchemeValidator, CommandHandler, instantiateObject
_SoundCommand = namedtuple('_SoundCommand', ('sound_id',))
_SoundCommand.__new__.__defaults__ = (None,)
_SoundCommandScheme = {'required': (('sound_id', basestring),)}

class SoundCommand(_SoundCommand, SchemeValidator):
    """
    Represents web command for playing sound by id.
    """

    def __init__(self, *args, **kwargs):
        super(SoundCommand, self).__init__(_SoundCommandScheme)


def createSoundHandler(handlerFunc):
    data = {'name': 'sound',
     'cls': SoundCommand,
     'handler': handlerFunc}
    return instantiateObject(CommandHandler, data)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\web_client_api\commands\sound.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:09 Støední Evropa (letní èas)
