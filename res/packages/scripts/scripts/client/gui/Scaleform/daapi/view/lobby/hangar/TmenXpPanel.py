# 2017.05.04 15:23:35 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/TmenXpPanel.py
from debug_utils import LOG_DEBUG
from gui import SystemMessages
from gui.Scaleform.daapi.view.meta.TmenXpPanelMeta import TmenXpPanelMeta
from gui.shared.gui_items.processors.vehicle import VehicleTmenXPAccelerator
from gui.shared.utils import decorators
from CurrentVehicle import g_currentVehicle

class TmenXpPanel(TmenXpPanelMeta):

    def __init__(self):
        super(TmenXpPanel, self).__init__()

    def _populate(self):
        super(TmenXpPanel, self)._populate()
        g_currentVehicle.onChanged += self._onVehicleChange
        self._onVehicleChange()

    def _dispose(self):
        g_currentVehicle.onChanged -= self._onVehicleChange
        super(TmenXpPanel, self)._dispose()

    @decorators.process('updateTankmen')
    def accelerateTmenXp(self, selected):
        vehicle = g_currentVehicle.item
        result = yield VehicleTmenXPAccelerator(vehicle, bool(selected)).request()
        if not result.success:
            self.as_setTankmenXpPanelS(vehicle.isElite, vehicle.isXPToTman)
        if len(result.userMsg):
            SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)

    def _onVehicleChange(self):
        vehicle = g_currentVehicle.item
        if vehicle is None:
            self.as_setTankmenXpPanelS(False, False)
            LOG_DEBUG('Do not show TMenXPPanel: No current vehicle')
            return
        else:
            self.as_setTankmenXpPanelS(vehicle.isElite, vehicle.isXPToTman)
            return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\hangar\TmenXpPanel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:35 St�edn� Evropa (letn� �as)
