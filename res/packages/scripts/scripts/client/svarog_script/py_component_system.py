# 2017.05.04 15:27:41 Støední Evropa (letní èas)
# Embedded file name: scripts/client/svarog_script/py_component_system.py
import Svarog
from svarog_script.auto_properties import AutoProperty, AutoPropertyInitMetaclass

class ComponentDescriptor(AutoProperty):

    def __init__(self, fieldName = None):
        AutoProperty.__init__(self, fieldName)

    def __set__(self, instance, value):
        if not isinstance(instance, ComponentSystem):
            raise AssertionError
            prevValue = getattr(instance, self.fieldName, None)
            if prevValue is not None:
                instance.removeComponent(prevValue)
            value is not None and instance.addComponent(value, self.fieldName)
        setattr(instance, self.fieldName, value)
        return


class ComponentSystem(object):
    __metaclass__ = AutoPropertyInitMetaclass

    @staticmethod
    def groupCall(func):

        def wrapped(*args, **kwargs):
            self = args[0]
            processedArgs = args[1:]
            for component in self._components:
                attr = getattr(component, func.__name__, None)
                if attr is not None:
                    attr(*processedArgs, **kwargs)

            func(*args, **kwargs)
            return

        return wrapped

    def __init__(self):
        self._components = []
        self._nativeSystem = Svarog.ComponentSystem()

    def activate(self):
        self._nativeSystem.activate()

    def deactivate(self):
        self._nativeSystem.deactivate()

    def addComponent(self, component, name = ''):
        self._nativeSystem.addComponent(component, name)
        self._components.append(component)

    def removeComponent(self, component):
        self._nativeSystem.removeComponent(component)
        self._components.remove(component)

    def destroy(self):
        self._components = []
        self._nativeSystem.destroy()

    def __getattr__(self, item):
        return getattr(self._nativeSystem, item)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\svarog_script\py_component_system.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:42 Støední Evropa (letní èas)
