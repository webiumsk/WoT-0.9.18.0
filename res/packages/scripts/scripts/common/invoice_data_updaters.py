# 2017.05.04 15:28:35 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/invoice_data_updaters.py
from wotdecorators import singleton
from VersionUpdater import VersionUpdaterBase
_CURRENT_VERSION = 4
_UPDATE_FUNCTION_TEMPLATE = '_update%dTo%d'

def _update1To2(data):
    if 'slots' in data:
        return None
    elif 'berths' in data:
        return None
    else:
        data['version'] = 2
        vehicles = data.get('vehicles', [])
        slots = 0
        for cd in vehicles:
            if cd > 0:
                slots += 1

        data['slots'] = slots
        return (data['version'], data)


def _update2To3(data):
    data['version'] = 3
    vehicles = data.get('vehicles', [])
    if vehicles:
        data['vehicles'] = dict.fromkeys(vehicles, {})
    return (data['version'], data)


def _update3To4(data):
    data['version'] = 4
    if 'vehicles' not in data:
        return data
    for vehicleData in data['vehicles'].itervalues():
        if 'rent' not in vehicleData:
            continue
        rent = vehicleData['rent']
        if 'expires' not in rent:
            continue
        expires = rent['expires']
        if 'after' in expires:
            rent['time'] = expires['after']
        if 'at' in expires:
            rent['time'] = expires['at']
        if 'state' in expires:
            rent['time'] = float('-inf') if expires['state'] else float('inf')
        if 'battles' in expires:
            rent['battles'] = expires['battles']

    return (data['version'], data)


@singleton

class InvoiceVersionUpdater(VersionUpdaterBase):

    def __init__(self):
        super(self.__class__, self).__init__(_UPDATE_FUNCTION_TEMPLATE, _CURRENT_VERSION)

    def updateVersion(self, logID, data):
        if not isinstance(data, dict):
            return None
        else:
            return self._updateToLatestVersion(lambda data: data.get('version', 1), logID, data)[0]
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\invoice_data_updaters.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:35 St�edn� Evropa (letn� �as)
