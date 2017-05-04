# 2017.05.04 15:20:54 Støední Evropa (letní èas)
# Embedded file name: scripts/client/FX/Events/ClearParticles.py
from FX import s_sectionProcessors
from ParticleSubSystem import ParticleSubSystem
import Pixie

class ClearParticles(ParticleSubSystem):
    """
    This class implements an Event that clears a particle system.
    This is useful if an effect is to be reused, to make sure no
    particles are left over from a previous instantiation of the effect.
    It only works on ParticleSystem actors.
    """

    def __init__(self):
        ParticleSubSystem.__init__(self)

    def clearSubSystem(self, actor, source, target, subSystem):
        subSystem.clear()

    def go(self, effect, actor, source, target, **kargs):
        self.subSystemIterate(actor, source, target, self.clearSubSystem)
        return 0.0


s_sectionProcessors['ClearParticles'] = ClearParticles
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\FX\Events\ClearParticles.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:54 Støední Evropa (letní èas)
