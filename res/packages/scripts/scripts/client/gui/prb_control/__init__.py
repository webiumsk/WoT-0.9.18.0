# 2017.05.04 15:21:55 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/__init__.py


class prbDispatcherProperty(property):
    """
    Prebattle dispatcher access property.
    """

    def __get__(self, obj, objType = None):
        """
        Getter for property.
        Args:
            obj: decorated object
            objType: decorated object's class
        
        Returns:
            prebattle dispatcher
        """
        from gui.prb_control.dispatcher import g_prbLoader
        return g_prbLoader.getDispatcher()


class prbEntityProperty(property):
    """
    Prebattle entity access property.
    """

    def __get__(self, obj, objType = None):
        """
        Getter for property.
        Args:
            obj: decorated object
            objType: decorated object's class
        
        Returns:
            prebattle entity
        """
        from gui.prb_control.dispatcher import g_prbLoader
        dispatcher = g_prbLoader.getDispatcher()
        entity = None
        if dispatcher is not None:
            entity = dispatcher.getEntity()
        return entity


class prbPeripheriesHandlerProperty(property):
    """
    Peripheries handler access property.
    """

    def __get__(self, obj, objType = None):
        """
        Getter for property.
        Args:
            obj: decorated object
            objType: decorated object's class
        
        Returns:
            peripheries handler
        """
        from gui.prb_control.dispatcher import g_prbLoader
        return g_prbLoader.getPeripheriesHandler()


class prbInvitesProperty(property):
    """
    Prebattle invites access property.
    """

    def __get__(self, obj, objType = None):
        """
        Getter for property.
        Args:
            obj: decorated object
            objType: decorated object's class
        
        Returns:
            prebattle invites
        """
        from gui.prb_control.dispatcher import g_prbLoader
        return g_prbLoader.getInvitesManager()


class prbAutoInvitesProperty(property):
    """
    Prebattle autoinvites access property.
    """

    def __get__(self, obj, objType = None):
        """
        Getter for property.
        Args:
            obj: decorated object
            objType: decorated object's class
        
        Returns:
            prebattle autoinvites
        """
        from gui.prb_control.dispatcher import g_prbLoader
        return g_prbLoader.getAutoInvitesNotifier()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:55 Støední Evropa (letní èas)
