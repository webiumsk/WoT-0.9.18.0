# 2017.05.04 15:23:13 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/eliteWindow/EliteWindow.py
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleVO
from gui.Scaleform.daapi.view.meta.EliteWindowMeta import EliteWindowMeta
from gui.shared import g_itemsCache

class EliteWindow(EliteWindowMeta):

    def __init__(self, ctx = None):
        super(EliteWindow, self).__init__()
        self.vehInvID = ctx['vehTypeCompDescr']

    def _populate(self):
        super(EliteWindow, self)._populate()
        self.as_setVehicleS(makeVehicleVO(g_itemsCache.items.getItemByCD(self.vehInvID)))

    def onWindowClose(self):
        self.destroy()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\eliteWindow\EliteWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:13 Støední Evropa (letní èas)
