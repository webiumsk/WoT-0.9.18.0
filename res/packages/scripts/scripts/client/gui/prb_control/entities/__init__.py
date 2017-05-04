# 2017.05.04 15:21:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/__init__.py
from constants import IS_DEVELOPMENT
__all__ = ('initDevFunctional', 'finiDevFunctional')

def initDevFunctional():
    if IS_DEVELOPMENT:
        try:
            from gui.development.dev_prebattle import init
        except ImportError:

            def init():
                pass

        init()


def finiDevFunctional():
    if IS_DEVELOPMENT:
        try:
            from gui.development.dev_prebattle import fini
        except ImportError:

            def fini():
                pass

        fini()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:56 Støední Evropa (letní èas)
