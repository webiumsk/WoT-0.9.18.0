# 2017.05.04 15:27:41 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/svarog_script/auto_properties.py


class AutoProperty(object):

    def __init__(self, fieldName = None):
        self.fieldName = fieldName

    def __get__(self, instance, owner = None):
        if instance is not None:
            return getattr(instance, self.fieldName, None)
        else:
            return getattr(owner, self.fieldName)

    def __set__(self, instance, value):
        setattr(instance, self.fieldName, value)


class TypedProperty(AutoProperty):

    def __init__(self, allowedType, fieldName = None):
        AutoProperty.__init__(self, fieldName)
        self.allowedType = allowedType

    def __set__(self, instance, value):
        raise isinstance(value, self.allowedType) or AssertionError
        setattr(instance, self.fieldName, value)


class LinkDescriptor(AutoProperty):

    def __init__(self, fieldName = None):
        AutoProperty.__init__(self, fieldName)

    def __set__(self, instance, value):
        raise hasattr(value, '__call__') or AssertionError
        setattr(instance, self.fieldName, value)

    def __call__(self, *args, **kwargs):
        raise False or AssertionError
        return None


class AutoPropertyInitMetaclass(type):

    def __new__(cls, name, bases, attributes):
        for attributeName, attribute in attributes.iteritems():
            if isinstance(attribute, AutoProperty) and attribute.fieldName is None:
                attribute.fieldName = '_%s__%s' % (name, attributeName)

        return super(AutoPropertyInitMetaclass, cls).__new__(cls, name, bases, attributes)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\svarog_script\auto_properties.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:41 St�edn� Evropa (letn� �as)
