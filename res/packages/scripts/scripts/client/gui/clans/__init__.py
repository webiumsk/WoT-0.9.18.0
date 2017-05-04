# 2017.05.04 15:21:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/clans/__init__.py
from skeletons.gui.clans import IClanController
__all__ = ('getClanServicesConfig',)

def getClanServicesConfig(manager):
    """ Configures services for package clans.
    :param manager: helpers.dependency.DependencyManager
    """
    from gui.clans.clan_controller import ClanController
    ctrl = ClanController()
    ctrl.init()
    manager.bindInstance(IClanController, ctrl, finalizer='fini')
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\clans\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:33 Støední Evropa (letní èas)
