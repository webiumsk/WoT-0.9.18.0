# 2017.05.04 15:20:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bwobsolete_helpers/CallbackHelpers.py
"""This module contains a number of helper functions intended simplify
implementing callback functions in a safe way.
"""
import BigWorld

def IgnoreCallbackIfDestroyed(function):

    def checkIfDestroyed(self, *args, **kwargs):
        if not isinstance(self, BigWorld.Entity):
            raise AssertionError
            return self.isDestroyed or function(self, *args, **kwargs)

    return checkIfDestroyed
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bwobsolete_helpers\CallbackHelpers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:41 Støední Evropa (letní èas)
