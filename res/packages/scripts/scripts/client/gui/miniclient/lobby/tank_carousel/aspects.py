# 2017.05.04 15:21:51 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/miniclient/lobby/tank_carousel/aspects.py
from helpers import aop
from helpers.i18n import makeString as _ms
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.formatters import text_styles

class VehicleTooltipStatus(aop.Aspect):

    def __init__(self, config):
        self.__vehicle_is_available = config['vehicle_is_available']
        aop.Aspect.__init__(self)

    def atCall(self, cd):
        if not self.__vehicle_is_available(cd.args[2]):
            cd.avoid()
            return {'header': _ms('#menu:tankCarousel/vehicleStates/%s' % Vehicle.VEHICLE_STATE.UNAVAILABLE),
             'text': '',
             'level': Vehicle.VEHICLE_STATE_LEVEL.CRITICAL}


class MakeTankUnavailableInCarousel(aop.Aspect):

    def __init__(self, config):
        self.__vehicle_is_available = config['vehicle_is_available']
        aop.Aspect.__init__(self)

    def atReturn(self, cd):
        original_return_value = cd.returned
        original_args = cd.args
        if not self.__vehicle_is_available(original_args[0]):
            state = _ms('#menu:tankCarousel/vehicleStates/%s' % Vehicle.VEHICLE_STATE.UNAVAILABLE)
            original_return_value['infoText'] = text_styles.vehicleStatusCriticalText(state)
            original_return_value['smallInfoText'] = text_styles.critical(state)
        return original_return_value
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\tank_carousel\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:51 St�edn� Evropa (letn� �as)
