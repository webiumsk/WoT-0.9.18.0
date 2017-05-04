# 2017.05.04 15:27:11 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/proto/__init__.py
import weakref
from helpers.ro_property import ROPropertyMeta
from messenger.m_constants import PROTO_TYPE, PROTO_TYPE_NAMES
from messenger.proto.bw import BWProtoPlugin
from messenger.proto.bw_chat2 import BWProtoPlugin as BWProtoPlugin_chat2
from messenger.proto.bw.BWServerSettings import BWServerSettings
from messenger.proto.bw_chat2.BWServerSettings import BWServerSettings as BWServerSettings_chat2
from messenger.proto.interfaces import IProtoPlugin
from messenger.proto.migration import MigrationPlugin
from messenger.proto.migration.MigrationServerSettings import MigrationServerSettings
from messenger.proto.xmpp import XmppPlugin, XmppServerSettings
from messenger.proto.xmpp.xmpp_constants import XMPP_MUC_CHANNEL_TYPE
__all__ = ('BWProtoPlugin', 'BWProtoPlugin_chat2', 'XmppPlugin', 'MigrationPlugin')
_SUPPORTED_PROTO_PLUGINS = {PROTO_TYPE.BW: BWProtoPlugin(),
 PROTO_TYPE.BW_CHAT2: BWProtoPlugin_chat2(),
 PROTO_TYPE.XMPP: XmppPlugin()}
_SUPPORTED_PROTO_PLUGINS[PROTO_TYPE.MIGRATION] = MigrationPlugin(_SUPPORTED_PROTO_PLUGINS)
_SUPPORTED_PROTO_SETTINGS = {PROTO_TYPE.BW: BWServerSettings(),
 PROTO_TYPE.BW_CHAT2: BWServerSettings_chat2(),
 PROTO_TYPE.XMPP: XmppServerSettings(),
 PROTO_TYPE.MIGRATION: MigrationServerSettings()}

class ProtoPluginsDecorator(IProtoPlugin):
    __metaclass__ = ROPropertyMeta
    __readonly__ = {PROTO_TYPE_NAMES[k]:v for k, v in _SUPPORTED_PROTO_PLUGINS.iteritems()}

    def __repr__(self):
        return 'ProtoPluginsDecorator(id=0x{0:08X}, ro={1!r:s})'.format(id(self), self.__readonly__.keys())

    def connect(self, scope):
        self._invoke('connect', scope)

    def disconnect(self):
        self._invoke('disconnect')

    def view(self, scope):
        self._invoke('view', scope)

    def setFilters(self, msgFilterChain):
        self._invoke('setFilters', weakref.proxy(msgFilterChain))

    def init(self):
        for plugin in self.__readonly__.itervalues():
            plugin.init()

    def clear(self):
        for plugin in self.__readonly__.itervalues():
            plugin.clear()

    def _invoke(self, method, *args):
        settings = ServerSettings.__readonly__
        for protoName, plugin in self.__readonly__.iteritems():
            if protoName in settings and settings[protoName].isEnabled():
                getattr(plugin, method)(*args)


class ServerSettings(object):
    __metaclass__ = ROPropertyMeta
    __readonly__ = {PROTO_TYPE_NAMES[k]:v for k, v in _SUPPORTED_PROTO_SETTINGS.iteritems()}

    def __repr__(self):
        return 'ServerSettings(id=0x{0:08X}, ro={1!r:s})'.format(id(self), self.__readonly__.keys())

    def update(self, data):
        for settings in self.__readonly__.itervalues():
            settings.update(data)

    def clear(self):
        for settings in self.__readonly__.itervalues():
            settings.clear()

    def useToShowContacts(self, protoType):
        result = False
        if protoType is PROTO_TYPE.BW:
            result = not self._isXmppEnabled()
        elif protoType is PROTO_TYPE.XMPP:
            result = self._isXmppEnabled()
        return result

    def isUserRoomsEnabled(self, protoType):
        result = False
        if protoType is PROTO_TYPE.BW:
            result = not self._isXmppUserRoomsEnabled()
        elif protoType is PROTO_TYPE.XMPP:
            result = self._isXmppUserRoomsEnabled()
        return result

    def getSystemChannels(self, protoType):
        if protoType is PROTO_TYPE.XMPP:
            return self._getSystemChannels()
        else:
            return None

    def isXmppClansEnabled(self):
        """Are clan channels over xmpp enabled
        :return: True if clan channels're enabled
        :rtype: bool
        """
        return self._isXmppMucChannelEnabled(XMPP_MUC_CHANNEL_TYPE.CLANS)

    def _isXmppEnabled(self):
        """If xmpp generally enabled
        :return: True if <xmpp><enabled>True</enabled>... in server config
        :rtype: bool
        """
        xmppName = PROTO_TYPE_NAMES[PROTO_TYPE.XMPP]
        if xmppName in self.__readonly__:
            result = self.__readonly__[xmppName].isEnabled()
        else:
            result = False
        return result

    def _isXmppMucChannelEnabled(self, channelType):
        """Is MUC channel enabled
        :param channelType: muc channel type
        :type channelType: XMPP_MUC_CHANNEL_TYPE
        :return: True if channel enabled
        :rtype: bool
        """
        xmppName = PROTO_TYPE_NAMES[PROTO_TYPE.XMPP]
        if xmppName in self.__readonly__:
            result = self.__readonly__[xmppName].isMucServiceAllowed(channelType)
        else:
            result = False
        return result

    def _isXmppUserRoomsEnabled(self):
        """Are users rooms enabled
        :return: True if users channels're enabled
        :rtype: bool
        """
        return self._isXmppMucChannelEnabled(XMPP_MUC_CHANNEL_TYPE.USERS)

    def _getSystemChannels(self):
        xmppName = PROTO_TYPE_NAMES[PROTO_TYPE.XMPP]
        if xmppName in self.__readonly__:
            result = self.__readonly__[xmppName].getSystemChannels()
        else:
            result = None
        return result


class _proto_type_getter(object):

    def __init__(self, protoType):
        super(_proto_type_getter, self).__init__()
        self._type = protoType

    def get(self):
        raise NotImplementedError

    def __call__(self, _):
        return self.get()


class proto_getter(_proto_type_getter):

    def get(self):
        return _SUPPORTED_PROTO_PLUGINS[self._type]


class settings_getter(_proto_type_getter):

    def get(self):
        return _SUPPORTED_PROTO_SETTINGS[self._type]
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:11 St�edn� Evropa (letn� �as)
