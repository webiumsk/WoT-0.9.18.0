# 2017.05.04 15:20:59 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/DialogsInterface.py
from gui.Scaleform.Waiting import Waiting
from gui.shared import events, g_eventBus
from gui.shared.utils.decorators import dialog
from gui.Scaleform.daapi.view.dialogs import I18nInfoDialogMeta, I18nConfirmDialogMeta, DisconnectMeta

@dialog
def showDialog(meta, callback):
    g_eventBus.handleEvent(events.ShowDialogEvent(meta, callback))


@dialog
def showI18nInfoDialog(i18nKey, callback, meta = None):
    showDialog(I18nInfoDialogMeta(i18nKey, meta=meta), callback)


@dialog
def showI18nConfirmDialog(i18nKey, callback, meta = None, focusedID = None):
    showDialog(I18nConfirmDialogMeta(i18nKey, meta=meta, focusedID=focusedID), callback)


__ifDisconnectDialogShown = False

def showDisconnect(reason = None, isBan = False, expiryTime = None):
    global __ifDisconnectDialogShown
    if __ifDisconnectDialogShown:
        return
    Waiting.close()

    def callback(_):
        global __ifDisconnectDialogShown
        __ifDisconnectDialogShown = False

    __ifDisconnectDialogShown = True
    showDialog(DisconnectMeta(reason, isBan, expiryTime), callback)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\DialogsInterface.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:59 St�edn� Evropa (letn� �as)
