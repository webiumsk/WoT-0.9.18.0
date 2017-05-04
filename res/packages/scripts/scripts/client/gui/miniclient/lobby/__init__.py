# 2017.05.04 15:21:49 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/lobby/__init__.py
from gui.miniclient.lobby.user_cm_handlers import UserCmClanUnavailablePointCut, UserCmInviteClanUnavailablePointCut
import tank_carousel
from hangar import configure_pointcuts as _configure_hangar_pointcuts
from header import configure_pointcuts as _configure_header_pointcuts
from tank_carousel import configure_pointcuts as _configure_carousel_pointcuts
from profile import configure_pointcuts as _configure_profile_pointcuts
from strongholds import configure_pointcuts as _configure_strongholds_pointcuts
from MiniclientDescriptionWindow import MiniclientDescriptionWindow

def configure_pointcuts(config):
    _configure_carousel_pointcuts(config)
    _configure_hangar_pointcuts(config)
    _configure_header_pointcuts(config)
    _configure_profile_pointcuts()
    _configure_strongholds_pointcuts()
    MiniclientDescriptionWindow()
    UserCmClanUnavailablePointCut()
    UserCmInviteClanUnavailablePointCut()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:49 Støední Evropa (letní èas)
