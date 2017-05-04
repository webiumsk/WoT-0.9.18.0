# 2017.05.04 15:26:33 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/sounds/filters.py
import WWISE
from gui.sounds.sound_constants import SoundFilters

class _SoundFilterAbstract(object):

    def start(self):
        pass

    def stop(self):
        pass


class EmptySoundFilter(_SoundFilterAbstract):

    def __repr__(self):
        return 'EmptyFilter'


class _WWISEStateAmbient(_SoundFilterAbstract):

    def __init__(self, stateID):
        self._stateID = stateID

    def start(self):
        WWISE.WW_setState(self._stateID, '%s_on' % self._stateID)

    def stop(self):
        WWISE.WW_setState(self._stateID, '%s_off' % self._stateID)

    def __repr__(self):
        return 'WWISE(%s)' % self._stateID


class _FortAmbientFilter(object):

    def getBuildNumberField(self):
        raise NotImplementedError

    def getTransportModeField(self):
        raise NotImplementedError

    def getDefencePeriodField(self):
        raise NotImplementedError


class WWISEFortAmbientFilter(_FortAmbientFilter, _WWISEStateAmbient):

    def __init__(self):
        _FortAmbientFilter.__init__(self)
        _WWISEStateAmbient.__init__(self, 'STATE_fortified_area')

    def getBuildNumberField(self):
        return 'RTPC_ext_buildings_number'

    def getTransportModeField(self):
        return 'RTPC_ext_transport_mode'

    def getDefencePeriodField(self):
        return 'RTPC_ext_defence_period'

    def __repr__(self):
        return 'WWISEFort'


class WWISEFilteredHangarFilter(_WWISEStateAmbient):

    def __init__(self):
        _WWISEStateAmbient.__init__(self, 'STATE_hangar_filtered')


def getEmptyFilter():
    return EmptySoundFilter()


def get(filterID):
    if filterID in _filters:
        return _filters[filterID]
    return EmptySoundFilter()


def _selectFilter(wwise):
    if WWISE.enabled:
        return wwise
    return EmptySoundFilter()


_filters = {SoundFilters.FORT_FILTER: _selectFilter(WWISEFortAmbientFilter()),
 SoundFilters.FILTERED_HANGAR: _selectFilter(WWISEFilteredHangarFilter())}
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\sounds\filters.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:33 St�edn� Evropa (letn� �as)
