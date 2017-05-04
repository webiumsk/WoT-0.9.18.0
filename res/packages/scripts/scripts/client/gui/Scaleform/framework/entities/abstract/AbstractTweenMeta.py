# 2017.05.04 15:24:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/AbstractTweenMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class AbstractTweenMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def initialiaze(self, props):
        """
        :param props: Represented by ITweenPropertiesVO (AS)
        """
        self._printOverrideError('initialiaze')

    def creatTweenPY(self, tween):
        """
        :param tween: Represented by DisplayObject (AS)
        """
        self._printOverrideError('creatTweenPY')

    def getPaused(self):
        self._printOverrideError('getPaused')

    def setPaused(self, paused):
        self._printOverrideError('setPaused')

    def getLoop(self):
        self._printOverrideError('getLoop')

    def setLoop(self, loop):
        self._printOverrideError('setLoop')

    def getDuration(self):
        self._printOverrideError('getDuration')

    def setDuration(self, duration):
        self._printOverrideError('setDuration')

    def getPosition(self):
        self._printOverrideError('getPosition')

    def setPosition(self, position):
        self._printOverrideError('setPosition')

    def getDelay(self):
        self._printOverrideError('getDelay')

    def setDelay(self, delay):
        self._printOverrideError('setDelay')

    def resetAnim(self):
        self._printOverrideError('resetAnim')

    def getTweenIdx(self):
        self._printOverrideError('getTweenIdx')

    def getIsComplete(self):
        self._printOverrideError('getIsComplete')

    def postponedCheckState(self):
        self._printOverrideError('postponedCheckState')

    def getTargetDisplayObjectS(self):
        if self._isDAAPIInited():
            return self.flashObject.getTargetDisplayObject()

    def onAnimCompleteS(self):
        if self._isDAAPIInited():
            return self.flashObject.onAnimComplete()

    def onAnimStartS(self):
        if self._isDAAPIInited():
            return self.flashObject.onAnimStart()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\AbstractTweenMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:45 St�edn� Evropa (letn� �as)
