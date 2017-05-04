# 2017.05.04 15:27:21 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/proto/xmpp/jid.py
import random
import types
import time
from string import Template
from ConnectionManager import connectionManager
from ids_generators import SequenceIDGenerator
from messenger import g_settings
from messenger.proto.xmpp.xmpp_constants import XMPP_MUC_CHANNEL_TYPE

class BareJID(object):
    __slots__ = ('_node', '_domain')

    def __init__(self, jid = None):
        super(BareJID, self).__init__()
        self.setJID(jid)

    def setJID(self, jid):
        tail = ''
        if not jid:
            self._node, self._domain = ('', '')
        elif type(jid) in types.StringTypes:
            if jid.find('@') + 1:
                self._node, jid = jid.split('@', 1)
                self._node = self._node.lower()
            else:
                self._node = ''
            if jid.find('/') + 1:
                self._domain, tail = jid.split('/', 1)
            else:
                self._domain = jid
            self._domain = self._domain.lower()
        elif isinstance(jid, BareJID):
            self._node, self._domain, tail = jid.getNode(), jid.getDomain(), jid.getResource()
        else:
            raise ValueError('JID can be specified as string or as instance of JID class.')
        return tail

    def getBareJID(self):
        return self

    def getNode(self):
        return self._node

    def setNode(self, node):
        if node is None:
            self._node = ''
        if type(node) in types.StringTypes:
            self._node = node.lower()
        else:
            self._node = node
        return

    def getDomain(self):
        return self._domain

    def setDomain(self, domain):
        raise domain or AssertionError('Domain no empty')
        self._domain = domain.lower()

    def getResource(self):
        return ''

    def setResource(self, resource):
        pass

    def __str__(self):
        if self._node:
            jid = '{0}@{1}'.format(self._node, self._domain)
        else:
            jid = self._domain
        return jid

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__() == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __nonzero__(self):
        return self.__str__() != ''

    def __hash__(self):
        return hash(self.__str__())

    def __getstate__(self):
        return str(self)

    def __setstate__(self, state):
        self.setJID(state)


class JID(BareJID):
    __slots__ = ('_resource',)

    def __init__(self, jid = None):
        super(JID, self).__init__(jid)

    def setJID(self, jid):
        self._resource = super(JID, self).setJID(jid)

    def getBareJID(self):
        return BareJID(self)

    def getResource(self):
        return self._resource

    def setResource(self, resource):
        self._resource = resource or ''

    def __str__(self):
        jid = super(JID, self).__str__()
        if self._resource:
            jid = '{0}/{1}'.format(jid, self._resource)
        return jid


class _DatabaseIDGetter(object):

    def getDatabaseID(self):
        value = getattr(self, '_node')
        if value:
            try:
                result = long(value)
            except ValueError:
                result = 0

        else:
            result = 0
        return result


class ContactBareJID(BareJID, _DatabaseIDGetter):

    def __hash__(self):
        return self.getDatabaseID()


class ContactJID(JID, _DatabaseIDGetter):

    def getBareJID(self):
        return ContactBareJID(self)

    def __hash__(self):
        return self.getDatabaseID()


def makeContactJID(dbID):
    jid = ContactBareJID()
    jid.setNode(long(dbID))
    jid.setDomain(g_settings.server.XMPP.domain)
    return jid


_counter = SequenceIDGenerator()

def makeUserRoomJID(room = ''):
    jid = JID()
    service = g_settings.server.XMPP.getChannelByType(XMPP_MUC_CHANNEL_TYPE.USERS)
    if not service or not service['hostname']:
        return jid
    if not room:
        room = 'user_room_{:08X}_{:08X}_{:04X}'.format(long(time.time()) & 4294967295L, random.randrange(1, 4294967295L), _counter.next())
    jid.setNode(room)
    jid.setDomain(service['hostname'])
    return jid


def makeSystemRoomJID(room = '', channelType = XMPP_MUC_CHANNEL_TYPE.STANDARD):
    """
    create jid for system room
    :param room: room name if exist
    :param channelType: channel type (XMPP_MUC_CHANNEL_TYPE)
    :return: system room jid
    """
    jid = JID()
    service = g_settings.server.XMPP.getChannelByType(channelType)
    if not service or not service['hostname']:
        return jid
    room = room or _getSystemChannelNameFormatter(service)
    if not room:
        return jid
    jid.setNode(room)
    jid.setDomain(service['hostname'])
    return jid


def _getSystemChannelNameFormatter(service):
    peripheryID = connectionManager.peripheryID
    chanTemplate = Template(service['format'])
    if chanTemplate:
        return chanTemplate.safe_substitute(peripheryID=peripheryID, userString=service['userString'], hostname=service['hostname'], type=service['type'])
    else:
        return None


def makeClanRoomJID(clandDbId, channelType = XMPP_MUC_CHANNEL_TYPE.CLANS):
    """
    create jid for clan room
    :param room: room name if exist
    :return: clan room jid
    """
    jid = JID()
    service = g_settings.server.XMPP.getChannelByType(channelType)
    if not service or not service['hostname']:
        return jid
    clanTemplate = Template(service['format'])
    room = clanTemplate.safe_substitute(clanDBID=clandDbId)
    if not room:
        return jid
    jid.setNode(room)
    jid.setDomain(service['hostname'])
    return jid
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\xmpp\jid.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:21 St�edn� Evropa (letn� �as)
