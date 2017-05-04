# 2017.05.04 15:24:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ContainerManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ContainerManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def isModalViewsIsExists(self):
        self._printOverrideError('isModalViewsIsExists')

    def canCancelPreviousLoading(self, containerType):
        self._printOverrideError('canCancelPreviousLoading')

    def as_getViewS(self, name):
        if self._isDAAPIInited():
            return self.flashObject.as_getView(name)

    def as_showS(self, name, x, y):
        if self._isDAAPIInited():
            return self.flashObject.as_show(name, x, y)

    def as_hideS(self, name):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(name)

    def as_registerContainerS(self, type, name):
        if self._isDAAPIInited():
            return self.flashObject.as_registerContainer(type, name)

    def as_unregisterContainerS(self, type):
        if self._isDAAPIInited():
            return self.flashObject.as_unregisterContainer(type)

    def as_closePopUpsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closePopUps()

    def as_isOnTopS(self, cType, vName):
        if self._isDAAPIInited():
            return self.flashObject.as_isOnTop(cType, vName)

    def as_bringToFrontS(self, cType, vName):
        if self._isDAAPIInited():
            return self.flashObject.as_bringToFront(cType, vName)

    def as_showContainersS(self, viewTypes):
        """
        :param viewTypes: Represented by Vector.<String> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showContainers(viewTypes)

    def as_hideContainersS(self, viewTypes):
        """
        :param viewTypes: Represented by Vector.<String> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideContainers(viewTypes)

    def as_isContainerShownS(self, viewType):
        if self._isDAAPIInited():
            return self.flashObject.as_isContainerShown(viewType)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\ContainerManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:46 Støední Evropa (letní èas)
