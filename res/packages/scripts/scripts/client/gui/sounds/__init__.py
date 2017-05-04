# 2017.05.04 15:26:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/sounds/__init__.py
from gui.sounds.sounds_ctrl import SoundsController
from skeletons.gui.sounds import ISoundsController
__all__ = ('getSoundsConfig',)

def getSoundsConfig(manager):
    """ Configures services for package sounds.
    :param manager: helpers.dependency.DependencyManager
    """
    ctrl = SoundsController()
    ctrl.init()
    manager.bindInstance(ISoundsController, ctrl, finalizer='fini')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\sounds\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:33 Støední Evropa (letní èas)
