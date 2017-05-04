# 2017.05.04 15:20:52 Støední Evropa (letní èas)
# Embedded file name: scripts/client/FX/Actors/Model.py
import BigWorld
from bwdebug import *
from FX.Actor import Actor
from FX import s_sectionProcessors

class Model(Actor):
    """
    This class implements an Actor that is a PyModel.
    """

    def load(self, pSection, prereqs = None):
        """
        This method loads the PyModel Actor from a data section. The
        the model resource ID is read from the section name.            
        """
        try:
            actor = prereqs.pop(pSection.asString)
        except:
            try:
                actor = BigWorld.Model(pSection.asString)
            except:
                ERROR_MSG('Could not create Model', pSection.asString)
                actor = None

        return actor

    def prerequisites(self, pSection):
        return [pSection.asString]


s_sectionProcessors['Model'] = Model
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\FX\Actors\Model.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:52 Støední Evropa (letní èas)
