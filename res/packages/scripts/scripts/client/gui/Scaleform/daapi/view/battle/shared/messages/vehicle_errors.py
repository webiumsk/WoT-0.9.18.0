# 2017.05.04 15:22:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/messages/vehicle_errors.py
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.battle.shared.messages import fading_messages

class VehicleErrorMessages(fading_messages.FadingMessages):

    def __init__(self):
        super(VehicleErrorMessages, self).__init__('VehicleErrorsPanel', 'vehicle_errors_panel.xml')

    def __del__(self):
        LOG_DEBUG('VehicleErrorMessages panel is deleted')

    def _addGameListeners(self):
        super(VehicleErrorMessages, self)._addGameListeners()
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleErrorByKey += self.__onShowVehicleErrorByKey
        return

    def _removeGameListeners(self):
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleErrorByKey -= self.__onShowVehicleErrorByKey
        super(VehicleErrorMessages, self)._removeGameListeners()
        return

    def __onShowVehicleErrorByKey(self, key, args = None, extra = None):
        self.showMessage(key, args, extra)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\shared\messages\vehicle_errors.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:41 Støední Evropa (letní èas)
