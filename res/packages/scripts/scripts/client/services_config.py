# 2017.05.04 15:20:05 Støední Evropa (letní èas)
# Embedded file name: scripts/client/services_config.py
import account_helpers
import gui
__all__ = ('getClientServicesConfig',)

def getClientServicesConfig(manager):
    """ Configures services for package gui.
    :param manager: helpers.dependency.DependencyManager
    """
    manager.install(gui.getGuiServicesConfig)
    manager.install(account_helpers.getAccountHelpersConfig)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\services_config.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:05 Støední Evropa (letní èas)
