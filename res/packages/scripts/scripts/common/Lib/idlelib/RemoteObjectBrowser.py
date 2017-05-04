# 2017.05.04 15:32:38 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/idlelib/RemoteObjectBrowser.py
from idlelib import rpc

def remote_object_tree_item(item):
    wrapper = WrappedObjectTreeItem(item)
    oid = id(wrapper)
    rpc.objecttable[oid] = wrapper
    return oid


class WrappedObjectTreeItem:

    def __init__(self, item):
        self.__item = item

    def __getattr__(self, name):
        value = getattr(self.__item, name)
        return value

    def _GetSubList(self):
        list = self.__item._GetSubList()
        return map(remote_object_tree_item, list)


class StubObjectTreeItem:

    def __init__(self, sockio, oid):
        self.sockio = sockio
        self.oid = oid

    def __getattr__(self, name):
        value = rpc.MethodProxy(self.sockio, self.oid, name)
        return value

    def _GetSubList(self):
        list = self.sockio.remotecall(self.oid, '_GetSubList', (), {})
        return [ StubObjectTreeItem(self.sockio, oid) for oid in list ]
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\idlelib\RemoteObjectBrowser.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:38 Støední Evropa (letní èas)
