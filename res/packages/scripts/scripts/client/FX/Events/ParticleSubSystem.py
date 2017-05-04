# 2017.05.04 15:20:54 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/FX/Events/ParticleSubSystem.py
from FX.Event import Event
from bwdebug import *
import Pixie
SOURCE_PSA = 1
SINK_PSA = 2
BARRIER_PSA = 3
FORCE_PSA = 4
STREAM_PSA = 5
JITTER_PSA = 6
SCALER_PSA = 7
TINT_SHADER_PSA = 8
NODE_CLAMP_PSA = 9
ORBITOR_PSA = 10
FLARE_PSA = 11
COLLIDE_PSA = 12
MATRIX_SWARM_PSA = 13
MAGNET_PSA = 14
SPLAT_PSA = 15

class ParticleSubSystem(Event):
    """
    ParticleSubSystem - This base class exists to provide a foundation
    for all events that deal with selected subSystems of a MetaParticleSystem.
    ParticleSubSystem-based events allow the user to specify the name of
    specific ParticleSystems within the MetaParticleSystem, by adding a list
    of "systemName" tags in the XML file.  If no system names are specified,
    then the entire MetaParticleSystem will be affected.
    """

    def __init__(self):
        self.subSystems = []

    def load(self, pSection, prereqs = None):
        self.subSystems = pSection.readStrings('systemName')
        return self

    def duration(self, actor, source, target):
        return 0.0

    def isInteresting(self, subSystem):
        return 1

    def populateSubSystemList(self, actor):
        if type(actor) == Pixie.MetaParticleSystem:
            if len(self.subSystems) == 0:
                self.subSystems = []
                for i in xrange(0, actor.nSystems()):
                    sys = actor.system(i)
                    if self.isInteresting(sys):
                        self.subSystems.append(i)

    def subSystemIterate(self, actor, source, target, callbackFn):
        if type(actor) == Pixie.MetaParticleSystem:
            if len(self.subSystems) == 0:
                self.populateSubSystemList(actor)
            for i in self.subSystems:
                sys = actor.system(i)
                callbackFn(actor, source, target, sys)

        else:
            try:
                callbackFn(actor, source, target, actor)
            except:
                ERROR_MSG('actor is not a particle system!', actor)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\FX\Events\ParticleSubSystem.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:54 St�edn� Evropa (letn� �as)
