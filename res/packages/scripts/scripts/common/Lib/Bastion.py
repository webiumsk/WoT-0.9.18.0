# 2017.05.04 15:29:23 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/Bastion.py
"""Bastionification utility.

A bastion (for another object -- the 'original') is an object that has
the same methods as the original but does not give access to its
instance variables.  Bastions have a number of uses, but the most
obvious one is to provide code executing in restricted mode with a
safe interface to an object implemented in unrestricted mode.

The bastionification routine has an optional second argument which is
a filter function.  Only those methods for which the filter method
(called with the method name as argument) returns true are accessible.
The default filter method returns true unless the method name begins
with an underscore.

There are a number of possible implementations of bastions.  We use a
'lazy' approach where the bastion's __getattr__() discipline does all
the work for a particular method the first time it is used.  This is
usually fastest, especially if the user doesn't call all available
methods.  The retrieved methods are stored as instance variables of
the bastion, so the overhead is only occurred on the first use of each
method.

Detail: the bastion class has a __repr__() discipline which includes
the repr() of the original object.  This is precomputed when the
bastion is created.

"""
from warnings import warnpy3k
warnpy3k('the Bastion module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
__all__ = ['BastionClass', 'Bastion']
from types import MethodType

class BastionClass:
    """Helper class used by the Bastion() function.
    
    You could subclass this and pass the subclass as the bastionclass
    argument to the Bastion() function, as long as the constructor has
    the same signature (a get() function and a name for the object).
    
    """

    def __init__(self, get, name):
        """Constructor.
        
        Arguments:
        
        get - a function that gets the attribute value (by name)
        name - a human-readable name for the original object
               (suggestion: use repr(object))
        
        """
        self._get_ = get
        self._name_ = name

    def __repr__(self):
        """Return a representation string.
        
        This includes the name passed in to the constructor, so that
        if you print the bastion during debugging, at least you have
        some idea of what it is.
        
        """
        return '<Bastion for %s>' % self._name_

    def __getattr__(self, name):
        """Get an as-yet undefined attribute value.
        
        This calls the get() function that was passed to the
        constructor.  The result is stored as an instance variable so
        that the next time the same attribute is requested,
        __getattr__() won't be invoked.
        
        If the get() function raises an exception, this is simply
        passed on -- exceptions are not cached.
        
        """
        attribute = self._get_(name)
        self.__dict__[name] = attribute
        return attribute


def Bastion(object, filter = lambda name: name[:1] != '_', name = None, bastionclass = BastionClass):
    """Create a bastion for an object, using an optional filter.
    
    See the Bastion module's documentation for background.
    
    Arguments:
    
    object - the original object
    filter - a predicate that decides whether a function name is OK;
             by default all names are OK that don't start with '_'
    name - the name of the object; default repr(object)
    bastionclass - class used to create the bastion; default BastionClass
    
    """
    raise RuntimeError, 'This code is not secure in Python 2.2 and later'

    def get1(name, object = object, filter = filter):
        """Internal function for Bastion().  See source comments."""
        if filter(name):
            attribute = getattr(object, name)
            if type(attribute) == MethodType:
                return attribute
        raise AttributeError, name

    def get2(name, get1 = get1):
        """Internal function for Bastion().  See source comments."""
        return get1(name)

    if name is None:
        name = repr(object)
    return bastionclass(get2, name)


def _test():
    """Test the Bastion() function."""

    class Original:

        def __init__(self):
            self.sum = 0

        def add(self, n):
            self._add(n)

        def _add(self, n):
            self.sum = self.sum + n

        def total(self):
            return self.sum

    o = Original()
    b = Bastion(o)
    testcode = 'if 1:\n    b.add(81)\n    b.add(18)\n    print "b.total() =", b.total()\n    try:\n        print "b.sum =", b.sum,\n    except:\n        print "inaccessible"\n    else:\n        print "accessible"\n    try:\n        print "b._add =", b._add,\n    except:\n        print "inaccessible"\n    else:\n        print "accessible"\n    try:\n        print "b._get_.func_defaults =", map(type, b._get_.func_defaults),\n    except:\n        print "inaccessible"\n    else:\n        print "accessible"\n    \n'
    exec testcode
    print '====================', 'Using rexec:', '===================='
    import rexec
    r = rexec.RExec()
    m = r.add_module('__main__')
    m.b = b
    r.r_exec(testcode)


if __name__ == '__main__':
    _test()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\Bastion.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:29:23 St�edn� Evropa (letn� �as)