# 2017.05.04 15:24:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/TutorialManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class TutorialManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def onComponentFound(self, componentId):
        self._printOverrideError('onComponentFound')

    def onComponentDisposed(self, componentId):
        self._printOverrideError('onComponentDisposed')

    def onTriggerActivated(self, componentId, triggerId):
        self._printOverrideError('onTriggerActivated')

    def requestCriteriaValue(self, criteriaName):
        self._printOverrideError('requestCriteriaValue')

    def as_setSystemEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSystemEnabled(value)

    def as_setDescriptionsS(self, descriptions):
        if self._isDAAPIInited():
            return self.flashObject.as_setDescriptions(descriptions)

    def as_setCriteriaS(self, criteriaName, criteriaValue, requestedCriteria):
        if self._isDAAPIInited():
            return self.flashObject.as_setCriteria(criteriaName, criteriaValue, requestedCriteria)

    def as_setTriggersS(self, componentId, triggers):
        if self._isDAAPIInited():
            return self.flashObject.as_setTriggers(componentId, triggers)

    def as_showHintS(self, viewTutorialId, componentId, data, isCustomCmp):
        if self._isDAAPIInited():
            return self.flashObject.as_showHint(viewTutorialId, componentId, data, isCustomCmp)

    def as_hideHintS(self, viewTutorialId, componentId):
        if self._isDAAPIInited():
            return self.flashObject.as_hideHint(viewTutorialId, componentId)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\TutorialManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:47 Støední Evropa (letní èas)
