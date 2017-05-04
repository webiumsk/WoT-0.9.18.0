# 2017.05.04 15:24:08 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehiclePreview/__init__.py
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS
from gui.Scaleform.framework import ViewSettings, ViewTypes, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.hangar.VehicleParameters import VehiclePreviewParameters
    from gui.Scaleform.daapi.view.lobby.vehiclePreview.ModulesPanel import ModulesPanel
    return (ViewSettings(VEHPREVIEW_CONSTANTS.MODULES_PY_ALIAS, ModulesPanel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE), ViewSettings(VEHPREVIEW_CONSTANTS.PARAMETERS_PY_ALIAS, VehiclePreviewParameters, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (VehPreviewPackageBusinessHandler(),)


class VehPreviewPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        super(VehPreviewPackageBusinessHandler, self).__init__((), APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\vehiclePreview\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:08 Støední Evropa (letní èas)
