# 2017.05.04 15:22:56 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/user_cm_handlers.py
import math
from adisp import process
from constants import DENUNCIATIONS_PER_DAY, ARENA_GUI_TYPE
from debug_utils import LOG_DEBUG
from gui import SystemMessages, DialogsInterface
from gui.LobbyContext import g_lobbyContext
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.clans.clan_helpers import showClanInviteSystemMsg
from gui.clans.contexts import CreateInviteCtx
from gui.prb_control import prbDispatcherProperty, prbEntityProperty
from gui.prb_control.entities.base.ctx import PrbAction, SendInvitesCtx
from gui.prb_control.settings import PREBATTLE_ACTION_NAME
from gui.shared import g_itemsCache, event_dispatcher as shared_events, utils
from gui.shared.ClanCache import ClanInfo
from gui.shared.denunciator import LobbyDenunciator, DENUNCIATIONS, DENUNCIATIONS_MAP
from gui.shared.utils.functions import showSentInviteMessage
from helpers import i18n, dependency
from helpers.i18n import makeString
from messenger import g_settings
from messenger.m_constants import PROTO_TYPE, USER_TAG
from messenger.proto import proto_getter
from messenger.storage import storage_getter
from skeletons.gui.clans import IClanController
from skeletons.gui.game_control import IVehicleComparisonBasket
from skeletons.gui.server_events import IEventsCache

class _EXTENDED_OPT_IDS(object):
    VEHICLE_COMPARE = 'userVehicleCompare'


class USER(object):
    INFO = 'userInfo'
    CLAN_INFO = 'clanInfo'
    SEND_CLAN_INVITE = 'sendClanInvite'
    CREATE_PRIVATE_CHANNEL = 'createPrivateChannel'
    ADD_TO_FRIENDS = 'addToFriends'
    ADD_TO_FRIENDS_AGAIN = 'addToFriendsAgain'
    REMOVE_FROM_FRIENDS = 'removeFromFriends'
    ADD_TO_IGNORED = 'addToIgnored'
    REMOVE_FROM_IGNORED = 'removeFromIgnored'
    COPY_TO_CLIPBOARD = 'copyToClipBoard'
    SET_MUTED = 'setMuted'
    UNSET_MUTED = 'unsetMuted'
    CREATE_SQUAD = 'createSquad'
    CREATE_EVENT_SQUAD = 'createEventSquad'
    INVITE = 'invite'
    REQUEST_FRIENDSHIP = 'requestFriendship'
    VEHICLE_INFO = 'vehicleInfoEx'
    VEHICLE_PREVIEW = 'vehiclePreview'


class BaseUserCMHandler(AbstractContextMenuHandler, EventSystemEntity):
    eventsCache = dependency.descriptor(IEventsCache)
    clanCtrl = dependency.descriptor(IClanController)

    def __init__(self, cmProxy, ctx = None):
        super(BaseUserCMHandler, self).__init__(cmProxy, ctx, handlers=self._getHandlers())

    @prbDispatcherProperty
    def prbDispatcher(self):
        return None

    @storage_getter('users')
    def usersStorage(self):
        return None

    @prbEntityProperty
    def prbEntity(self):
        return None

    @proto_getter(PROTO_TYPE.MIGRATION)
    def proto(self):
        return None

    def canInvite(self):
        if self.prbEntity is not None:
            return self.prbEntity.getPermissions().canSendInvite()
        else:
            return False
            return

    def isSquadCreator(self):
        return False

    def showUserInfo(self):

        def onDossierReceived(databaseID, userName):
            shared_events.showProfileWindow(databaseID, userName)

        shared_events.requestProfile(self.databaseID, self.userName, successCallback=onDossierReceived)

    def showClanInfo(self):
        if not g_lobbyContext.getServerSettings().clanProfile.isEnabled():
            SystemMessages.pushMessage(makeString(SYSTEM_MESSAGES.CLANS_ISCLANPROFILEDISABLED), type=SystemMessages.SM_TYPE.Error)
            return

        def onDossierReceived(databaseID, _):
            clanID, clanInfo = g_itemsCache.items.getClanInfo(databaseID)
            if clanID != 0:
                clanInfo = ClanInfo(*clanInfo)
                shared_events.showClanProfileWindow(clanID, clanInfo.getClanAbbrev())
            else:
                DialogsInterface.showI18nInfoDialog('clan_data_not_available', lambda result: None)

        shared_events.requestProfile(self.databaseID, self.userName, successCallback=onDossierReceived)

    @process
    def sendClanInvite(self):
        profile = self.clanCtrl.getAccountProfile()
        userName = self.userName
        context = CreateInviteCtx(profile.getClanDbID(), [self.databaseID])
        result = yield self.clanCtrl.sendRequest(context, allowDelay=True)
        showClanInviteSystemMsg(userName, result.isSuccess(), result.getCode())

    def createPrivateChannel(self):
        self.proto.contacts.createPrivateChannel(self.databaseID, self.userName)

    def addFriend(self):
        self.proto.contacts.addFriend(self.databaseID, self.userName)

    def requestFriendship(self):
        self.proto.contacts.requestFriendship(self.databaseID)

    def removeFriend(self):
        self.proto.contacts.removeFriend(self.databaseID)

    def setMuted(self):
        self.proto.contacts.setMuted(self.databaseID, self.userName)

    def unsetMuted(self):
        self.proto.contacts.unsetMuted(self.databaseID)

    def setIgnored(self):
        self.proto.contacts.addIgnored(self.databaseID, self.userName)

    def unsetIgnored(self):
        self.proto.contacts.removeIgnored(self.databaseID)

    def copyToClipboard(self):
        utils.copyToClipboard(self.userName)

    def createSquad(self):
        self._doSelect(PREBATTLE_ACTION_NAME.SQUAD, (self.databaseID,))

    def createEventSquad(self):
        self._doSelect(PREBATTLE_ACTION_NAME.EVENT_SQUAD, (self.databaseID,))

    def invite(self):
        user = self.usersStorage.getUser(self.databaseID)
        if self.prbEntity.getPermissions().canSendInvite():
            self.prbEntity.request(SendInvitesCtx([self.databaseID], ''))
            showSentInviteMessage(user)

    def getOptions(self, ctx = None):
        if not self._getUseCmInfo().isCurrentPlayer:
            return self._generateOptions(ctx)
        else:
            return None

    def _getHandlers(self):
        return {USER.INFO: 'showUserInfo',
         USER.CLAN_INFO: 'showClanInfo',
         USER.SEND_CLAN_INVITE: 'sendClanInvite',
         USER.CREATE_PRIVATE_CHANNEL: 'createPrivateChannel',
         USER.ADD_TO_FRIENDS: 'addFriend',
         USER.REMOVE_FROM_FRIENDS: 'removeFriend',
         USER.ADD_TO_IGNORED: 'setIgnored',
         USER.REMOVE_FROM_IGNORED: 'unsetIgnored',
         USER.COPY_TO_CLIPBOARD: 'copyToClipboard',
         USER.SET_MUTED: 'setMuted',
         USER.UNSET_MUTED: 'unsetMuted',
         USER.CREATE_SQUAD: 'createSquad',
         USER.CREATE_EVENT_SQUAD: 'createEventSquad',
         USER.INVITE: 'invite',
         USER.REQUEST_FRIENDSHIP: 'requestFriendship'}

    def _initFlashValues(self, ctx):
        self.databaseID = long(ctx.dbID)
        self.userName = ctx.userName
        self.wasInBattle = getattr(ctx, 'wasInBattle', True)
        self.showClanProfile = getattr(ctx, 'showClanProfile', True)

    def _clearFlashValues(self):
        self.databaseID = None
        self.userName = None
        self.wasInBattle = None
        return

    def _getUseCmInfo(self):
        return UserContextMenuInfo(self.databaseID, self.userName)

    def _generateOptions(self, ctx = None):
        userCMInfo = self._getUseCmInfo()
        if ctx is not None and not userCMInfo.hasClan:
            try:
                clanAbbrev = ctx.clanAbbrev
                userCMInfo.hasClan = bool(clanAbbrev)
            except:
                LOG_DEBUG('ctx has no property "clanAbbrev"')

        options = [self._makeItem(USER.INFO, MENU.contextmenu(USER.INFO))]
        options = self._addVehicleInfo(options)
        options = self._addClanProfileInfo(options, userCMInfo)
        options = self._addFriendshipInfo(options, userCMInfo)
        options = self._addChannelInfo(options, userCMInfo)
        options.append(self._makeItem(USER.COPY_TO_CLIPBOARD, MENU.contextmenu(USER.COPY_TO_CLIPBOARD)))
        options = self._addSquadInfo(options, userCMInfo.isIgnored)
        options = self._addPrebattleInfo(options, userCMInfo)
        options = self._addContactsNoteInfo(options, userCMInfo)
        options = self._addAppealInfo(options)
        options = self._addIgnoreInfo(options, userCMInfo)
        options = self._addMutedInfo(options, userCMInfo)
        options = self._addRejectFriendshipInfo(options, userCMInfo)
        options = self._addRemoveFromGroupInfo(options, userCMInfo)
        options = self._addRemoveFriendInfo(options, userCMInfo)
        options = self._addInviteClanInfo(options, userCMInfo)
        return options

    def _addIgnoreInfo(self, options, userCMInfo):
        ignoring = USER.REMOVE_FROM_IGNORED if userCMInfo.isIgnored else USER.ADD_TO_IGNORED
        options.append(self._makeItem(ignoring, MENU.contextmenu(ignoring), optInitData={'enabled': userCMInfo.isSameRealm}))
        return options

    def _addFriendshipInfo(self, options, userCMInfo):
        if not userCMInfo.isFriend:
            options.append(self._makeItem(USER.ADD_TO_FRIENDS, MENU.contextmenu(USER.ADD_TO_FRIENDS), optInitData={'enabled': userCMInfo.isSameRealm}))
        elif self.proto.contacts.isBidiFriendshipSupported():
            if USER_TAG.SUB_NONE in userCMInfo.getTags():
                options.append(self._makeItem(USER.REQUEST_FRIENDSHIP, MENU.contextmenu(USER.ADD_TO_FRIENDS_AGAIN), optInitData={'enabled': userCMInfo.isSameRealm}))
        return options

    def _addChannelInfo(self, options, userCMInfo):
        if not userCMInfo.isIgnored:
            options.append(self._makeItem(USER.CREATE_PRIVATE_CHANNEL, MENU.contextmenu(USER.CREATE_PRIVATE_CHANNEL), optInitData={'enabled': userCMInfo.canCreateChannel}))
        return options

    def _addSquadInfo(self, options, isIgnored):
        if not isIgnored and not self.isSquadCreator() and self.prbDispatcher is not None:
            canCreate = self.prbEntity.getPermissions().canCreateSquad()
            options.append(self._makeItem(USER.CREATE_SQUAD, MENU.contextmenu(USER.CREATE_SQUAD), optInitData={'enabled': canCreate}))
            if self.eventsCache.isEventEnabled():
                options.append(self._makeItem(USER.CREATE_EVENT_SQUAD, MENU.contextmenu(USER.CREATE_EVENT_SQUAD), optInitData={'enabled': canCreate,
                 'textColor': 13347959}))
        return options

    def _addPrebattleInfo(self, options, userCMInfo):
        if not userCMInfo.isIgnored and self.canInvite():
            options.append(self._makeItem(USER.INVITE, MENU.contextmenu(USER.INVITE)))
        return options

    def _addRemoveFriendInfo(self, options, userCMInfo):
        if userCMInfo.isFriend:
            options.append(self._makeItem(USER.REMOVE_FROM_FRIENDS, MENU.contextmenu(USER.REMOVE_FROM_FRIENDS), optInitData={'enabled': userCMInfo.isSameRealm}))
        return options

    def _addVehicleInfo(self, options):
        return options

    def _addContactsNoteInfo(self, options, userCMInfo):
        return options

    def _addAppealInfo(self, options):
        return options

    def _addMutedInfo(self, options, userCMInfo):
        return options

    def _addRemoveFromGroupInfo(self, options, isIgnored):
        return options

    def _addRejectFriendshipInfo(self, options, userCMInfo):
        return options

    def _addClanProfileInfo(self, options, userCMInfo):
        if g_lobbyContext.getServerSettings().clanProfile.isEnabled() and userCMInfo.hasClan and self.showClanProfile:
            options.append(self._makeItem(USER.CLAN_INFO, MENU.contextmenu(USER.CLAN_INFO), optInitData={'enabled': self.clanCtrl.isAvailable()}))
        return options

    def _addInviteClanInfo(self, options, userCMInfo):
        if g_lobbyContext.getServerSettings().clanProfile.isEnabled() and not userCMInfo.hasClan:
            profile = self.clanCtrl.getAccountProfile()
            canHandleClanInvites = profile.getMyClanPermissions().canHandleClanInvites()
            if profile.isInClan() and canHandleClanInvites:
                isEnabled = self.clanCtrl.isAvailable()
                canHandleClanInvites = profile.getMyClanPermissions().canHandleClanInvites()
                if isEnabled:
                    profile = self.clanCtrl.getAccountProfile()
                    dossier = profile.getClanDossier()
                    isEnabled = canHandleClanInvites and not dossier.isClanInviteSent(userCMInfo.databaseID) and not dossier.hasClanApplication(userCMInfo.databaseID)
                options.append(self._makeItem(USER.SEND_CLAN_INVITE, MENU.contextmenu(USER.SEND_CLAN_INVITE), optInitData={'enabled': isEnabled}))
        return options

    @process
    def _doSelect(self, prebattleActionName, accountsToInvite = None):
        yield self.prbDispatcher.doSelectAction(PrbAction(prebattleActionName, accountsToInvite=accountsToInvite))


class AppealCMHandler(BaseUserCMHandler):

    def __init__(self, cmProxy, ctx = None):
        super(AppealCMHandler, self).__init__(cmProxy, ctx)
        self._denunciator = LobbyDenunciator()

    def fini(self):
        self._denunciator = None
        super(AppealCMHandler, self).fini()
        return

    def appealIncorrectBehavior(self):
        self._denunciator.makeAppeal(self.databaseID, self.userName, DENUNCIATIONS.INCORRECT_BEHAVIOR, self._arenaUniqueID)

    def appealNotFairPlay(self):
        self._denunciator.makeAppeal(self.databaseID, self.userName, DENUNCIATIONS.NOT_FAIR_PLAY, self._arenaUniqueID)

    def appealForbiddenNick(self):
        self._denunciator.makeAppeal(self.databaseID, self.userName, DENUNCIATIONS.FORBIDDEN_NICK, self._arenaUniqueID)

    def appealBot(self):
        self._denunciator.makeAppeal(self.databaseID, self.userName, DENUNCIATIONS.BOT, self._arenaUniqueID)

    def showVehicleInfo(self):
        shared_events.showVehicleInfo(self._vehicleCD)

    def showVehiclePreview(self):
        shared_events.showVehiclePreview(self._vehicleCD)
        shared_events.hideBattleResults()

    def _initFlashValues(self, ctx):
        self._vehicleCD = None
        vehicleCD = getattr(ctx, 'vehicleCD', None)
        if vehicleCD is not None and not math.isnan(vehicleCD):
            self._vehicleCD = int(vehicleCD)
        clientArenaIdx = getattr(ctx, 'clientArenaIdx', 0)
        self._arenaUniqueID = g_lobbyContext.getArenaUniqueIDByClientID(clientArenaIdx)
        self._arenaGuiType = getattr(ctx, 'arenaType', ARENA_GUI_TYPE.UNKNOWN)
        self._isAlly = getattr(ctx, 'isAlly', False)
        super(AppealCMHandler, self)._initFlashValues(ctx)
        return

    def _clearFlashValues(self):
        super(AppealCMHandler, self)._clearFlashValues()
        self._vehicleCD = None
        self._arenaGuiType = None
        self._isAlly = None
        return

    def _getHandlers(self):
        handlers = super(AppealCMHandler, self)._getHandlers()
        handlers.update({DENUNCIATIONS.INCORRECT_BEHAVIOR: 'appealIncorrectBehavior',
         DENUNCIATIONS.NOT_FAIR_PLAY: 'appealNotFairPlay',
         DENUNCIATIONS.FORBIDDEN_NICK: 'appealForbiddenNick',
         DENUNCIATIONS.BOT: 'appealBot',
         USER.VEHICLE_INFO: 'showVehicleInfo',
         USER.VEHICLE_PREVIEW: 'showVehiclePreview'})
        return handlers

    def _addAppealInfo(self, options):
        if self.wasInBattle:
            options.append(self._createSubMenuItem())
        return options

    def _addVehicleInfo(self, options):
        if self._vehicleCD > 0:
            vehicle = g_itemsCache.items.getItemByCD(self._vehicleCD)
            if not vehicle.isSecret:
                isEnabled = True
                if vehicle.isPreviewAllowed():
                    isEnabled = not self.prbDispatcher.getFunctionalState().isNavigationDisabled()
                    action = USER.VEHICLE_PREVIEW
                    label = MENU.contextmenu(USER.VEHICLE_PREVIEW)
                else:
                    action = USER.VEHICLE_INFO
                    label = MENU.contextmenu(USER.VEHICLE_INFO)
                options.append(self._makeItem(action, label, optInitData={'enabled': isEnabled}))
        return options

    def _isAppealsForTopicEnabled(self, topic):
        topicID = DENUNCIATIONS_MAP[topic]
        return self._denunciator.isAppealsForTopicEnabled(self.databaseID, topicID, self._arenaUniqueID)

    def _getSubmenuData(self):
        if self._isAlly or self._arenaGuiType in (ARENA_GUI_TYPE.UNKNOWN, ARENA_GUI_TYPE.TRAINING):
            order = DENUNCIATIONS.ORDER
        else:
            order = DENUNCIATIONS.ENEMY_ORDER
        make = self._makeItem
        return [ make(denunciation, MENU.contextmenu(denunciation), optInitData={'enabled': self._isAppealsForTopicEnabled(denunciation)}) for denunciation in order ]

    def _createSubMenuItem(self):
        labelStr = '{} {}/{}'.format(i18n.makeString(MENU.CONTEXTMENU_APPEAL), self._denunciator.getDenunciationsLeft(), DENUNCIATIONS_PER_DAY)
        return self._makeItem(DENUNCIATIONS.APPEAL, labelStr, optInitData={'enabled': self._denunciator.isAppealsEnabled()}, optSubMenu=self._getSubmenuData())


class UserVehicleCMHandler(AppealCMHandler):
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)

    def compareVehicle(self):
        self.comparisonBasket.addVehicle(self._vehicleCD)

    def _getHandlers(self):
        handlers = super(UserVehicleCMHandler, self)._getHandlers()
        handlers.update({_EXTENDED_OPT_IDS.VEHICLE_COMPARE: 'compareVehicle'})
        return handlers

    def _generateOptions(self, ctx = None):
        options = super(AppealCMHandler, self)._generateOptions(ctx)
        self._manageVehCompareOptions(options)
        return options

    def _manageVehCompareOptions(self, options):
        if self.comparisonBasket.isEnabled():
            options.insert(2, self._makeItem(_EXTENDED_OPT_IDS.VEHICLE_COMPARE, MENU.contextmenu(_EXTENDED_OPT_IDS.VEHICLE_COMPARE), {'enabled': self.comparisonBasket.isReadyToAdd(g_itemsCache.items.getItemByCD(self._vehicleCD))}))


class UserContextMenuInfo(object):

    def __init__(self, databaseID, userName):
        self.user = self.usersStorage.getUser(databaseID)
        self.databaseID = databaseID
        self.canAddToIgnore = True
        self.canDoDenunciations = True
        self.isFriend = False
        self.isIgnored = False
        self.isTemporaryIgnored = False
        self.isMuted = False
        self.hasClan = False
        self.userName = userName
        self.displayName = userName
        self.isOnline = False
        self.isCurrentPlayer = False
        if self.user is not None:
            self.isFriend = self.user.isFriend()
            self.isIgnored = self.user.isIgnored()
            self.isTemporaryIgnored = self.user.isTemporaryIgnored()
            self.isMuted = self.user.isMuted()
            self.displayName = self.user.getFullName()
            self.isOnline = self.user.isOnline()
            self.isCurrentPlayer = self.user.isCurrentPlayer()
            self.hasClan = self.user.getClanInfo().isInClan()
        super(UserContextMenuInfo, self).__init__()
        return

    @storage_getter('users')
    def usersStorage(self):
        return None

    @property
    def isSameRealm(self):
        return g_lobbyContext.getServerSettings().roaming.isSameRealm(self.databaseID)

    @property
    def canCreateChannel(self):
        roaming = g_lobbyContext.getServerSettings().roaming
        if g_settings.server.XMPP.isEnabled():
            canCreate = roaming.isSameRealm(self.databaseID)
        else:
            canCreate = not roaming.isInRoaming() and not roaming.isPlayerInRoaming(self.databaseID) and self.isOnline
        return canCreate

    def getTags(self):
        if self.user is not None:
            return self.user.getTags()
        else:
            return set()

    def getNote(self):
        if self.user is not None:
            return self.user.getNote()
        else:
            return ''
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\user_cm_handlers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:57 St�edn� Evropa (letn� �as)
