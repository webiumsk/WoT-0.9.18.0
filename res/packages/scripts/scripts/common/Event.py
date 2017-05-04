# 2017.05.04 15:28:30 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Event.py
from debug_utils import LOG_CURRENT_EXCEPTION

class Event(object):
    """
    Allows delegates to subscribe for the event and to be called when event
    is triggered.
    
    Clearing events without event manager:
        onEvent1 = Event()
        onEvent2 = Event()
        ...
        onEvent1.clear()
        onEvent2.clear()
    
    Clearing events with event manager:
        em = EventManager()
        onEvent1 = Event(em)
        onEvent2 = Event(em)
        ...
        em.clear()
    """

    def __init__(self, manager = None):
        """
        :param manager - event manager that is used to clear all events thereby
        break all references.
        """
        self.__delegates = []
        if manager is not None:
            manager.register(self)
        return

    def __call__(self, *args, **kwargs):
        for delegate in self.__delegates[:]:
            try:
                delegate(*args, **kwargs)
            except:
                LOG_CURRENT_EXCEPTION()

    def __iadd__(self, delegate):
        if delegate not in self.__delegates:
            self.__delegates.append(delegate)
        return self

    def __isub__(self, delegate):
        if delegate in self.__delegates:
            self.__delegates.remove(delegate)
        return self

    def clear(self):
        del self.__delegates[:]

    def __repr__(self):
        return 'Event(%s):%s' % (len(self.__delegates), repr(self.__delegates))


class Handler(object):
    """
    Similar to Event. Difference is Handler allows only one delegate to be
    subscribed. One event manager could be used both for handlers and events.
    """

    def __init__(self, manager = None):
        """
        :param manager - event manager that is used to clear all handlers
        thereby break all references.
        """
        self.__delegate = None
        if manager is not None:
            manager.register(self)
        return

    def __call__(self, *args, **kwargs):
        if self.__delegate is not None:
            return self.__delegate(*args, **kwargs)
        else:
            return

    def set(self, delegate):
        self.__delegate = delegate

    def clear(self):
        self.__delegate = None
        return


class EventManager(object):
    """
    Event manager that is used to clear all events thereby break all references.
    """

    def __init__(self):
        self.__events = []

    def register(self, event):
        self.__events.append(event)

    def clear(self):
        for event in self.__events:
            event.clear()


class SuspendedEvent(Event):

    def __init__(self, manager):
        """
        Constructor.
        
        :param manager: EventManager derived event manager
        """
        raise isinstance(manager, SuspendedEventManager) or AssertionError
        super(SuspendedEvent, self).__init__(manager)
        self.__manager = manager

    def clear(self):
        self.__manager = None
        super(SuspendedEvent, self).clear()
        return

    def __call__(self, *args, **kwargs):
        if self.__manager.isSuspended():
            self.__manager.suspendEvent(self, *args, **kwargs)
        else:
            super(SuspendedEvent, self).__call__(*args, **kwargs)


class SuspendedEventManager(EventManager):

    def __init__(self):
        super(SuspendedEventManager, self).__init__()
        self.__isSuspended = False
        self.__suspendedEvents = []

    def suspendEvent(self, e, *args, **kwargs):
        self.__suspendedEvents.append((e, args, kwargs))

    def isSuspended(self):
        return self.__isSuspended

    def suspend(self):
        self.__isSuspended = True

    def resume(self):
        if self.__isSuspended:
            self.__isSuspended = False
            while self.__suspendedEvents:
                e, args, kwargs = self.__suspendedEvents.pop(0)
                e(*args, **kwargs)

    def clear(self):
        self.__isSuspended = False
        self.__suspendedEvents = []
        super(SuspendedEventManager, self).clear()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Event.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:30 St�edn� Evropa (letn� �as)
