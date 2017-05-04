# 2017.05.04 15:26:27 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/utils/requesters/GoodiesRequester.py
import BigWorld
from adisp import async
from collections import defaultdict, namedtuple
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
GoodieVariable = namedtuple('GoodieVariable', 'state finishTime count')

class GoodiesRequester(AbstractSyncDataRequester):

    @async
    def _requestCache(self, callback):
        BigWorld.player().goodies.getCache(lambda resID, value: self._response(resID, value, callback))

    @property
    def goodies(self):
        return self.getCacheValue('goodies', {})

    def _preprocessValidData(self, data):
        data = dict(data)
        formattedGoodies = defaultdict(dict)
        for goodieID, goodieData in data.get('goodies', {}).iteritems():
            formattedGoodies[goodieID] = GoodieVariable(*goodieData)

        data['goodies'] = formattedGoodies
        return data
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\utils\requesters\GoodiesRequester.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:27 Støední Evropa (letní èas)
