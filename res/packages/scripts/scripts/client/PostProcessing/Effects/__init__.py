# 2017.05.04 15:27:39 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/PostProcessing/Effects/__init__.py
"""PostProcessing.Effects python module
This module imports all Effects for ease-of-use by script programmers.
"""
s_effectFactories = {}

class implementEffectFactory:

    def __init__(self, name, desc, *defaultArgs):
        self.name = name
        self.desc = desc
        self.defaultArgs = defaultArgs

    def __call__(self, f):

        def callFn(*args):
            if len(args) > 0:
                return f(*args)
            else:
                return f(*self.defaultArgs)

        fn = callFn
        s_effectFactories[self.name] = [self.desc, fn]
        return fn


def getEffectNames():
    """
            This method returns a list of effect (names, descriptions)
            used by the World Editor.
    """
    ret = []
    for key in sorted(s_effectFactories.iterkeys()):
        desc = s_effectFactories[key][0]
        ret.append((key, desc))

    return ret


def effectFactory(name):
    """
            This method builds a effect, given the corresponding factory name.
    """
    return s_effectFactories[name][1]()


@implementEffectFactory('<new empty effect>', 'Create a new, empty effect.')
def empty():
    e = Effect()
    e.name = 'unnamed effect'
    e.phases = []
    return e


from DepthOfField import *
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\PostProcessing\Effects\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:39 St�edn� Evropa (letn� �as)
