# 2017.05.04 15:27:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/notification/tutorial_helper.py
try:
    from tutorial import GlobalStorage as TutorialGlobalStorage
    from tutorial.control.context import GLOBAL_VAR as TUTORIAL_GLOBAL_VAR
except ImportError:

    class TutorialGlobalStorage(object):

        def __init__(self, *args):
            pass

        def __get__(self, instance, owner = None):
            if instance is None:
                return self
            else:
                return 0


    class TUTORIAL_GLOBAL_VAR(object):
        LAST_HISTORY_ID = ''
        SERVICE_MESSAGES_IDS = ''
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\notification\tutorial_helper.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:37 Støední Evropa (letní èas)
