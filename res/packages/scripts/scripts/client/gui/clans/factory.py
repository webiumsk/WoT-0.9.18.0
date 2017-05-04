# 2017.05.04 15:21:30 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/clans/factory.py
import BigWorld
from constants import TOKEN_TYPE
from client_request_lib.requester import Requester as WebRequester
from gui.clans.requests import ClanRequester, ClanRequestsController
from gui.shared.utils.requesters import TokenRequester, getTokenRequester
from helpers.ServerSettings import _ClanProfile

def _webUrlFetcher(url, callback, headers = None, timeout = 30.0, method = 'GET', postData = ''):
    return BigWorld.fetchURL(url, callback, headers, timeout, method, postData)


class _ClanFactory(object):

    def __init__(self):
        super(_ClanFactory, self).__init__()

    def createWebRequester(self, settings, *args, **kwargs):
        raise NotImplementedError

    def createTokenRequester(self):
        raise NotImplementedError

    def createClanRequester(self, webRequester):
        raise NotImplementedError

    def createClanRequestsController(self, clansCtrl, clanRequester):
        raise NotImplementedError


class WebClanFactory(_ClanFactory):

    def __init__(self):
        super(WebClanFactory, self).__init__()

    def createWebRequester(self, settings, *args, **kwargs):
        return WebRequester.create_requester(_webUrlFetcher, settings, *args, **kwargs)

    def createTokenRequester(self):
        return getTokenRequester(TOKEN_TYPE.WGNI)

    def createClanRequester(self, webRequester):
        return ClanRequester(webRequester)

    def createClanRequestsController(self, clansCtrl, clanRequester):
        return ClanRequestsController(clansCtrl, clanRequester)


class FakeClanFactory(_ClanFactory):

    def __init__(self):
        super(FakeClanFactory, self).__init__()

    def createWebRequester(self, settings, *args, **kwargs):
        return WebRequester.create_requester(_webUrlFetcher, _ClanProfile(True, None, 'fake'), *args, **kwargs)

    def createTokenRequester(self):
        return TokenRequester(TOKEN_TYPE.WGNI, cache=False)

    def createClanRequester(self, webRequester):
        return ClanRequester(webRequester)

    def createClanRequestsController(self, clansCtrl, clanRequester):
        return ClanRequestsController(clansCtrl, clanRequester)


g_clanFactory = WebClanFactory()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\clans\factory.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:30 St�edn� Evropa (letn� �as)
