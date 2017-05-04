# 2017.05.04 15:20:52 Støední Evropa (letní èas)
# Embedded file name: scripts/client/FX/Actors/Light.py
import BigWorld
from bwdebug import *
from FX.Actor import Actor
from FX import s_sectionProcessors

class Light(Actor):
    """
    This class implements an Actor that is a PyChunkLight.
    """

    def load(self, pSection, prereqs = None):
        """
        This method loads a PyChunkLight from a data section. The
        the light reads its innerRadius, outerRadius and colour from the
        data section.
        """
        try:
            actor = BigWorld.PyChunkLight()
            actor.innerRadius = pSection.readFloat('innerRadius', 0)
            actor.outerRadius = pSection.readFloat('outerRadius', 10)
            actor.colour = pSection.readVector4('colour', (255, 255, 255, 255))
            actor.priority = pSection.readInt('priority', 0)
        except:
            ERROR_MSG('Could not create Light', pSection.asString)
            actor = None

        return actor


s_sectionProcessors['Light'] = Light
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\FX\Actors\Light.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:52 Støední Evropa (letní èas)
