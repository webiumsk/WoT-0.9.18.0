# 2017.05.04 15:27:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/skeletons/gui/system_messages.py


class ISystemMessages(object):

    def init(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

    def pushMessage(self, text, type, priority = None):
        raise NotImplementedError

    def pushI18nMessage(self, key, *args, **kwargs):
        raise NotImplementedError
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\skeletons\gui\system_messages.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:41 Støední Evropa (letní èas)
