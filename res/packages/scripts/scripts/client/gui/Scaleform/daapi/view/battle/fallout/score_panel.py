# 2017.05.04 15:22:29 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/fallout/score_panel.py
from gui.Scaleform.daapi.view.meta.FalloutBaseScorePanelMeta import FalloutBaseScorePanelMeta
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
_WARNING_RATIO = 0.8

class FalloutScorePanel(FalloutBaseScorePanelMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _populate(self):
        super(FalloutScorePanel, self)._populate()
        visitor = self.sessionProvider.arenaVisitor
        maxWinPoints = visitor.type.getWinPointsCAP()
        self.as_initS(maxWinPoints, maxWinPoints * _WARNING_RATIO)
        ctrl = self.sessionProvider.dynamic.gasAttack
        if ctrl is not None:
            ctrl.onPreparing += self.__onGasAttackPreparing
            ctrl.onStarted += self.__onGasAttackStarted
        return

    def _dispose(self):
        ctrl = self.sessionProvider.dynamic.gasAttack
        if ctrl is not None:
            ctrl.onPreparing -= self.__onGasAttackPreparing
            ctrl.onStarted -= self.__onGasAttackStarted
        super(FalloutScorePanel, self)._dispose()
        return

    def __onGasAttackPreparing(self, _):
        self.as_playScoreHighlightAnimS()

    def __onGasAttackStarted(self, _):
        self.as_stopScoreHighlightAnimS()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\fallout\score_panel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:30 Støední Evropa (letní èas)
