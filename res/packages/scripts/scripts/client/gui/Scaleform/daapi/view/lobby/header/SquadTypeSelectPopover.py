# 2017.05.04 15:23:39 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/header/SquadTypeSelectPopover.py
from adisp import process
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items
from gui.Scaleform.daapi.view.meta.BattleTypeSelectPopoverMeta import BattleTypeSelectPopoverMeta
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.prb_control.entities.base.ctx import PrbAction
from gui.prb_control.entities.listener import IGlobalListener

class SquadTypeSelectPopover(BattleTypeSelectPopoverMeta, IGlobalListener):

    def __init__(self, _ = None):
        super(SquadTypeSelectPopover, self).__init__()

    def selectFight(self, actionName):
        if self.prbDispatcher:
            self.__doSelect(actionName)
        else:
            LOG_ERROR('Prebattle dispatcher is not defined')

    def getTooltipData(self, itemData, itemIsDisabled):
        tooltip = ''
        if itemData == 'eventSquad':
            tooltip = TOOLTIPS.HEADER_EVENTSQUAD
        elif itemData == 'squad':
            tooltip = TOOLTIPS.HEADER_SQUAD
        return tooltip

    def demoClick(self):
        pass

    def update(self):
        if not self.isDisposed():
            self.as_updateS(*battle_selector_items.getSquadItems().getVOs())

    def _populate(self):
        super(SquadTypeSelectPopover, self)._populate()
        self.update()

    def _dispose(self):
        super(SquadTypeSelectPopover, self)._dispose()

    @process
    def __doSelect(self, prebattleActionName):
        yield self.prbDispatcher.doSelectAction(PrbAction(prebattleActionName))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\header\SquadTypeSelectPopover.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:39 St�edn� Evropa (letn� �as)
