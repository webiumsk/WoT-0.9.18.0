# 2017.05.04 15:26:54 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/formatters/chat_message.py
from gui.LobbyContext import g_lobbyContext
from helpers import dependency
from helpers import i18n
from messenger import g_settings
from messenger.ext.player_helpers import isCurrentPlayer
from messenger.formatters import TimeFormatter
from messenger.storage import storage_getter
from skeletons.gui.battle_session import IBattleSessionProvider

class _BattleMessageBuilder(object):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(_BattleMessageBuilder, self).__init__()
        self._ctx = {'playerColor': '',
         'playerName': '',
         'messageColor': '',
         'messageText': ''}

    def setColors(self, dbID):
        getter = g_settings.getColorScheme
        self._ctx['playerColor'] = getter('battle/player').getHexStr('unknown')
        self._ctx['messageColor'] = getter('battle/message').getHexStr('unknown')
        return self

    def setName(self, dbID, pName = None):
        if pName is not None:
            pName = i18n.encodeUtf8(pName)
        name = self.sessionProvider.getCtx().getPlayerFullName(accID=dbID, pName=pName)
        self._ctx['playerName'] = unicode(name, 'utf-8')
        return self

    def setText(self, text):
        self._ctx['messageText'] = text
        return self

    def build(self):
        return g_settings.battle.messageFormat % self._ctx


class TeamMessageBuilder(_BattleMessageBuilder):

    def setColors(self, dbID):
        pColorScheme = g_settings.getColorScheme('battle/player')
        pColor = pColorScheme.getHexStr('teammate')
        ctx = self.sessionProvider.getCtx()
        if isCurrentPlayer(dbID):
            pColor = pColorScheme.getHexStr('himself')
        elif ctx.isTeamKiller(accID=dbID):
            pColor = pColorScheme.getHexStr('teamkiller')
        elif ctx.isSquadMan(accID=dbID):
            pColor = pColorScheme.getHexStr('squadman')
        self._ctx['playerColor'] = pColor
        self._ctx['messageColor'] = g_settings.getColorScheme('battle/message').getHexStr('team')
        return self


class CommonMessageBuilder(_BattleMessageBuilder):

    def setColors(self, dbID):
        pColorScheme = g_settings.getColorScheme('battle/player')
        pColor = pColorScheme.getHexStr('unknown')
        if isCurrentPlayer(dbID):
            pColor = pColorScheme.getHexStr('himself')
        else:
            ctx = self.sessionProvider.getCtx()
            if ctx.isAlly(accID=dbID):
                if ctx.isTeamKiller(accID=dbID):
                    pColor = pColorScheme.getHexStr('teamkiller')
                elif ctx.isSquadMan(accID=dbID):
                    pColor = pColorScheme.getHexStr('squadman')
                else:
                    pColor = pColorScheme.getHexStr('teammate')
            elif ctx.isEnemy(accID=dbID):
                pColor = pColorScheme.getHexStr('enemy')
        self._ctx['playerColor'] = pColor
        self._ctx['messageColor'] = g_settings.getColorScheme('battle/message').getHexStr('common')
        return self


class SquadMessageBuilder(_BattleMessageBuilder):

    def setColors(self, dbID):
        pColorScheme = g_settings.getColorScheme('battle/player')
        pColor = pColorScheme.getHexStr('squadman')
        if isCurrentPlayer(dbID):
            pColor = pColorScheme.getHexStr('himself')
        elif self.sessionProvider.getCtx().isTeamKiller(accID=dbID):
            pColor = pColorScheme.getHexStr('teamkiller')
        self._ctx['playerColor'] = pColor
        self._ctx['messageColor'] = g_settings.getColorScheme('battle/message').getHexStr('squad')
        return self


class LobbyMessageBuilder(object):

    def __init__(self):
        super(LobbyMessageBuilder, self).__init__()
        self.__templateKey = ''
        self.__name = ''
        self.__time = 0.0
        self.__text = ''

    @storage_getter('users')
    def usersStorage(self):
        return None

    def setTime(self, time_):
        self.__time = TimeFormatter.getMessageTimeFormat(time_)
        return self

    def setGroup(self, group):
        self.__templateKey = group
        return self

    def setGuiType(self, dbID):
        self.__templateKey = self.usersStorage.getUserGuiType(dbID)
        return self

    def setName(self, dbID, nickName, clanAbbrev = None):
        self.__name = g_lobbyContext.getPlayerFullName(nickName, pDBID=dbID, clanAbbrev=clanAbbrev)
        return self

    def setText(self, text):
        self.__text = text
        return self

    def build(self):
        return g_settings.lobby.getMessageFormat(self.__templateKey).format(self.__name, self.__time, self.__text)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\formatters\chat_message.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:55 St�edn� Evropa (letn� �as)
