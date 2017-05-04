# 2017.05.04 15:21:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/login/pointcuts.py
import aspects
from helpers import aop

class ShowBGWallpaper(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.login.LoginView', 'BackgroundMode', 'show$', aspects=(aspects.ShowBGWallpaper,))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\login\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:51 Støední Evropa (letní èas)
