# 2017.05.04 15:27:40 Støední Evropa (letní èas)
# Embedded file name: scripts/client/skeletons/gui/login_manager.py


class ILoginManager(object):

    @property
    def servers(self):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def initiateLogin(self, email, password, serverName, isSocialToken2Login, rememberUser):
        raise NotImplementedError

    def initiateSocialLogin(self, socialNetworkName, serverName, rememberUser, isRegistration):
        raise NotImplementedError

    def initiateRelogin(self, login, token2, serverName):
        raise NotImplementedError

    def getPreference(self, key):
        raise NotImplementedError

    def clearPreferences(self):
        raise NotImplementedError

    def clearToken2Preference(self):
        raise NotImplementedError

    def writePreferences(self):
        raise NotImplementedError

    def writePeripheryLifetime(self):
        raise NotImplementedError

    @staticmethod
    def getAvailableSocialNetworks():
        raise NotImplementedError
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\skeletons\gui\login_manager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:40 Støední Evropa (letní èas)
