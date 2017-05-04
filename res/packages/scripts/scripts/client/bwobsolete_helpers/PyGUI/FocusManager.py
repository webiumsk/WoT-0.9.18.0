# 2017.05.04 15:20:45 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/FocusManager.py
_focusedComponent = None

def getFocusedComponent():
    global _focusedComponent
    return _focusedComponent


def setFocusedComponent(newFocus):
    global _focusedComponent
    if newFocus != _focusedComponent:
        if _focusedComponent is not None:
            _focusedComponent.focus = False
        _focusedComponent = newFocus
        if newFocus is not None:
            newFocus.focus = True
    return


def isFocusedComponent(component):
    if _focusedComponent is None or component is None:
        return _focusedComponent is component
    else:
        return _focusedComponent.__str__() == component.__str__()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bwobsolete_helpers\PyGUI\FocusManager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:45 Støední Evropa (letní èas)
