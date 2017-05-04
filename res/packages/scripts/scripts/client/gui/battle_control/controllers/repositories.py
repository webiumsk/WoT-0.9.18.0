# 2017.05.04 15:21:14 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/battle_control/controllers/repositories.py
from debug_utils import LOG_ERROR, LOG_DEBUG
from gui.battle_control.arena_info.interfaces import IArenaController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID, REUSABLE_BATTLE_CTRL_IDS
from gui.battle_control.battle_constants import getBattleCtrlName
from gui.battle_control.controllers import arena_load_ctrl
from gui.battle_control.controllers import avatar_stats_ctrl
from gui.battle_control.controllers import chat_cmd_ctrl
from gui.battle_control.controllers import consumables
from gui.battle_control.controllers import debug_ctrl
from gui.battle_control.controllers import drr_scale_ctrl
from gui.battle_control.controllers import dyn_squad_functional
from gui.battle_control.controllers import feedback_adaptor
from gui.battle_control.controllers import finish_sound_ctrl
from gui.battle_control.controllers import flag_nots_ctrl
from gui.battle_control.controllers import gas_attack_ctrl
from gui.battle_control.controllers import hit_direction_ctrl
from gui.battle_control.controllers import msgs_ctrl
from gui.battle_control.controllers import period_ctrl
from gui.battle_control.controllers import repair_ctrl
from gui.battle_control.controllers import respawn_ctrl
from gui.battle_control.controllers import team_bases_ctrl
from gui.battle_control.controllers import vehicle_state_ctrl
from gui.battle_control.controllers import personal_efficiency_ctrl
from gui.battle_control.controllers import interfaces
from gui.battle_control.controllers import tmp_ignore_list_ctrl
from gui.battle_control.controllers import view_points_ctrl
from skeletons.gui.battle_session import ISharedControllersLocator, IDynamicControllersLocator

class BattleSessionSetup(object):
    __slots__ = ('avatar', 'replayCtrl', 'gasAttackMgr', 'sessionProvider')

    def __init__(self, avatar = None, replayCtrl = None, gasAttackMgr = None, sessionProvider = None):
        super(BattleSessionSetup, self).__init__()
        self.avatar = avatar
        self.replayCtrl = replayCtrl
        self.gasAttackMgr = gasAttackMgr
        self.sessionProvider = sessionProvider

    @property
    def isReplayPlaying(self):
        if self.replayCtrl is not None:
            return self.replayCtrl.isPlaying and not self.replayCtrl.isBattleSimulation
        else:
            return False
            return

    @property
    def isReplayRecording(self):
        if self.replayCtrl is not None:
            return self.replayCtrl.isRecording
        else:
            return False
            return

    @property
    def battleCtx(self):
        raise self.sessionProvider is not None or AssertionError
        return self.sessionProvider.getCtx()

    @property
    def arenaDP(self):
        raise self.sessionProvider is not None or AssertionError
        return self.sessionProvider.getArenaDP()

    @property
    def arenaVisitor(self):
        raise self.sessionProvider is not None or AssertionError
        return self.sessionProvider.arenaVisitor

    @property
    def arenaEntity(self):
        raise self.avatar is not None or AssertionError
        return self.avatar.arena

    def registerArenaCtrl(self, controller):
        raise self.sessionProvider is not None or AssertionError
        return self.sessionProvider.addArenaCtrl(controller)

    def registerViewComponentsCtrl(self, controller):
        raise self.sessionProvider is not None or AssertionError
        return self.sessionProvider.registerViewComponentsCtrl(controller)

    def clear(self):
        self.avatar = None
        self.replayCtrl = None
        self.gasAttackMgr = None
        self.sessionProvider = None
        return


class _ControllersLocator(object):
    __slots__ = ('_repository',)

    def __init__(self, repository = None):
        super(_ControllersLocator, self).__init__()
        if not (repository is not None and isinstance(repository, interfaces.IBattleControllersRepository)):
            raise AssertionError('Repository is not valid')
            self._repository = repository
        else:
            self._repository = _EmptyRepository()
        return

    def destroy(self):
        self._repository.destroy()


class SharedControllersLocator(_ControllersLocator, ISharedControllersLocator):
    __slots__ = ()

    @property
    def ammo(self):
        return self._repository.getController(BATTLE_CTRL_ID.AMMO)

    @property
    def equipments(self):
        return self._repository.getController(BATTLE_CTRL_ID.EQUIPMENTS)

    @property
    def optionalDevices(self):
        return self._repository.getController(BATTLE_CTRL_ID.OPTIONAL_DEVICES)

    @property
    def vehicleState(self):
        return self._repository.getController(BATTLE_CTRL_ID.OBSERVED_VEHICLE_STATE)

    @property
    def hitDirection(self):
        return self._repository.getController(BATTLE_CTRL_ID.HIT_DIRECTION)

    @property
    def arenaLoad(self):
        return self._repository.getController(BATTLE_CTRL_ID.ARENA_LOAD_PROGRESS)

    @property
    def arenaPeriod(self):
        return self._repository.getController(BATTLE_CTRL_ID.ARENA_PERIOD)

    @property
    def feedback(self):
        return self._repository.getController(BATTLE_CTRL_ID.FEEDBACK)

    @property
    def chatCommands(self):
        return self._repository.getController(BATTLE_CTRL_ID.CHAT_COMMANDS)

    @property
    def messages(self):
        return self._repository.getController(BATTLE_CTRL_ID.MESSAGES)

    @property
    def drrScale(self):
        return self._repository.getController(BATTLE_CTRL_ID.DRR_SCALE)

    @property
    def privateStats(self):
        return self._repository.getController(BATTLE_CTRL_ID.AVATAR_PRIVATE_STATS)

    @property
    def crosshair(self):
        return self._repository.getController(BATTLE_CTRL_ID.CROSSHAIR)

    @property
    def personalEfficiencyCtrl(self):
        return self._repository.getController(BATTLE_CTRL_ID.PERSONAL_EFFICIENCY)

    @property
    def battleCacheCtrl(self):
        return self._repository.getController(BATTLE_CTRL_ID.TMP_IGNORE_LIST_CTRL)

    @property
    def viewPoints(self):
        return self._repository.getController(BATTLE_CTRL_ID.VIEW_POINTS)


class DynamicControllersLocator(_ControllersLocator, IDynamicControllersLocator):
    __slots__ = ()

    @property
    def debug(self):
        return self._repository.getController(BATTLE_CTRL_ID.DEBUG)

    @property
    def teamBases(self):
        return self._repository.getController(BATTLE_CTRL_ID.TEAM_BASES)

    @property
    def repair(self):
        return self._repository.getController(BATTLE_CTRL_ID.REPAIR)

    @property
    def respawn(self):
        return self._repository.getController(BATTLE_CTRL_ID.RESPAWN)

    @property
    def dynSquads(self):
        return self._repository.getController(BATTLE_CTRL_ID.DYN_SQUADS)

    @property
    def gasAttack(self):
        return self._repository.getController(BATTLE_CTRL_ID.GAS_ATTACK)

    @property
    def finishSound(self):
        return self._repository.getController(BATTLE_CTRL_ID.FINISH_SOUND)


class _EmptyRepository(interfaces.IBattleControllersRepository):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        return cls()

    def destroy(self):
        pass

    def getController(self, ctrlID):
        return None

    def addController(self, ctrl):
        raise NotImplementedError


class _ControllersRepository(interfaces.IBattleControllersRepository):
    __slots__ = ('_ctrls',)

    def __init__(self):
        super(_ControllersRepository, self).__init__()
        self._ctrls = {}

    @classmethod
    def create(cls, setup):
        return cls()

    def destroy(self):
        while self._ctrls:
            _, ctrl = self._ctrls.popitem()
            ctrl.stopControl()
            LOG_DEBUG('GUI Controller is stopped', getBattleCtrlName(ctrl.getControllerID()))

    def getController(self, ctrlID):
        if ctrlID in self._ctrls:
            return self._ctrls[ctrlID]
        else:
            return None
            return None

    def addController(self, ctrl):
        if not isinstance(ctrl, interfaces.IBattleController):
            raise AssertionError('Controller is not valid')
            ctrlID = ctrl.getControllerID()
            if ctrlID in REUSABLE_BATTLE_CTRL_IDS:
                LOG_ERROR('Controller can not be added to repository, controllerID is not unique', ctrlID)
                return
            if ctrlID in self._ctrls:
                LOG_ERROR('Controller with given ID already exists', ctrlID)
                return
            self._ctrls[ctrlID] = ctrl
            isinstance(ctrl, IArenaController) or ctrl.startControl()
        LOG_DEBUG('GUI Controller is started', getBattleCtrlName(ctrlID))

    def addArenaController(self, ctrl, setup):
        if setup.registerArenaCtrl(ctrl):
            self.addController(ctrl)

    def addViewController(self, ctrl, setup):
        if setup.registerViewComponentsCtrl(ctrl):
            self.addController(ctrl)

    def addArenaViewController(self, ctrl, setup):
        if setup.registerArenaCtrl(ctrl) and setup.registerViewComponentsCtrl(ctrl):
            self.addController(ctrl)


class SharedControllersRepository(_ControllersRepository):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        repository = cls()
        from gui.battle_control.controllers import crosshair_proxy
        repository.addController(crosshair_proxy.CrosshairDataProxy())
        ammo = consumables.createAmmoCtrl(setup)
        repository.addController(ammo)
        repository.addController(consumables.createEquipmentCtrl(setup))
        repository.addController(consumables.createOptDevicesCtrl())
        state = vehicle_state_ctrl.createCtrl(setup)
        repository.addController(state)
        repository.addController(avatar_stats_ctrl.AvatarStatsController())
        feedback = feedback_adaptor.createFeedbackAdaptor(setup)
        messages = msgs_ctrl.createBattleMessagesCtrl(setup)
        repository.addController(feedback)
        repository.addController(messages)
        repository.addController(chat_cmd_ctrl.ChatCommandsController(setup, feedback, ammo))
        repository.addController(drr_scale_ctrl.DRRScaleController(messages))
        repository.addController(personal_efficiency_ctrl.createEfficiencyCtrl(setup, feedback, state))
        tmpIgnoreListCtrl = tmp_ignore_list_ctrl.createTmpIgnoreListCtrl(setup)
        if tmpIgnoreListCtrl is not None:
            repository.addController(tmpIgnoreListCtrl)
        repository.addArenaController(view_points_ctrl.ViewPointsController(setup), setup)
        repository.addArenaController(arena_load_ctrl.ArenaLoadController(), setup)
        repository.addArenaViewController(period_ctrl.createPeriodCtrl(setup), setup)
        repository.addViewController(hit_direction_ctrl.createHitDirectionController(setup), setup)
        return repository


class _ControllersRepositoryByBonuses(_ControllersRepository):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        repository = super(_ControllersRepositoryByBonuses, cls).create(setup)
        gasAttackMgr = setup.gasAttackMgr
        arenaVisitor = setup.arenaVisitor
        if arenaVisitor.hasRepairPoints():
            repository.addController(repair_ctrl.RepairController())
        if arenaVisitor.hasRespawns():
            repository.addArenaViewController(respawn_ctrl.RespawnsController(setup), setup)
        if arenaVisitor.hasFlags():
            repository.addViewController(flag_nots_ctrl.NotificationsController(setup), setup)
        if arenaVisitor.hasGasAttack() and gasAttackMgr is not None:
            repository.addViewController(gas_attack_ctrl.GasAttackController(setup), setup)
        return repository


class ClassicControllersRepository(_ControllersRepositoryByBonuses):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        repository = super(ClassicControllersRepository, cls).create(setup)
        repository.addArenaViewController(team_bases_ctrl.createTeamsBasesCtrl(setup), setup)
        repository.addArenaController(dyn_squad_functional.DynSquadFunctional(setup), setup)
        repository.addViewController(debug_ctrl.DebugController(), setup)
        if not setup.isReplayPlaying:
            repository.addArenaController(finish_sound_ctrl.FinishSoundController(), setup)
        return repository


class FalloutControllersRepository(_ControllersRepositoryByBonuses):
    __slots__ = ()

    @classmethod
    def create(cls, setup):
        repository = super(FalloutControllersRepository, cls).create(setup)
        repository.addViewController(debug_ctrl.DebugController(), setup)
        return repository
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_control\controllers\repositories.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:14 St�edn� Evropa (letn� �as)
