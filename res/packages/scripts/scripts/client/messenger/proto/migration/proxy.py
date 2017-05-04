# 2017.05.04 15:27:18 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/proto/migration/proxy.py


class MigrationProxy(object):
    __slots__ = ('_proto',)

    def __init__(self, proto):
        super(MigrationProxy, self).__init__()
        self._proto = proto

    def clear(self):
        self._proto = None
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\migration\proxy.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:18 Støední Evropa (letní èas)
