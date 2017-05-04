# 2017.05.04 15:20:27 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/arena_components/client_arena_component_assembler.py
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from debug_utils import LOG_WARNING
from client_arena_component_system import ClientArenaComponentSystem

def createComponentSystem(bonusType):
    componentSystem = ClientArenaComponentSystem(bonusType)
    from arena_components.assembler_helper import COMPONENT_ASSEMBLER
    if bonusType in COMPONENT_ASSEMBLER:
        COMPONENT_ASSEMBLER[bonusType].assembleComponents(componentSystem)
    return componentSystem


def destroyComponentSystem(componentSystem):
    if componentSystem is None:
        return
    else:
        from arena_components.assembler_helper import COMPONENT_ASSEMBLER
        if componentSystem.bonusType in COMPONENT_ASSEMBLER:
            COMPONENT_ASSEMBLER[componentSystem.bonusType].disassembleComponents(componentSystem)
        componentSystem.destroy()
        return


class ClientArenaComponentAssembler(object):

    @staticmethod
    def assembleComponents(componentSystem):
        pass

    @staticmethod
    def disassembleComponents(componentSystem):
        pass

    @staticmethod
    def _assembleBonusCapsComponents(componentSystem):
        from arena_components.assembler_helper import ARENA_BONUS_TYPE_CAP_COMPONENTS
        for name, (bonusFlag, componentClass) in ARENA_BONUS_TYPE_CAP_COMPONENTS.iteritems():
            isBonusTypeCapActive = ARENA_BONUS_TYPE_CAPS.checkAny(componentSystem.bonusType, bonusFlag)
            if isBonusTypeCapActive:
                ClientArenaComponentAssembler._addArenaComponent(componentSystem, name, componentClass)

    @staticmethod
    def _addArenaComponent(componentSystem, name, componentClass):
        comp = componentClass(componentSystem)
        if comp is not None:
            prevValue = getattr(componentSystem, name, None)
            if prevValue is not None:
                LOG_WARNING('componenent %s is already available, old component will be removed', name)
                componentSystem.removeComponent(prevValue)
            componentSystem.addComponent(comp)
            setattr(componentSystem, name, comp)
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\arena_components\client_arena_component_assembler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:27 St�edn� Evropa (letn� �as)
