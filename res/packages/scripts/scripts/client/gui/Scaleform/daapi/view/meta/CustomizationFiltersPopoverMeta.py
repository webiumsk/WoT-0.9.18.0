# 2017.05.04 15:24:22 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationFiltersPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CustomizationFiltersPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def changeFilter(self, groupId, itemId):
        self._printOverrideError('changeFilter')

    def setDefaultFilter(self):
        self._printOverrideError('setDefaultFilter')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by FiltersPopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setStateS(self, data):
        """
        :param data: Represented by FiltersStateVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setState(data)

    def as_enableDefBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableDefBtn(value)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\CustomizationFiltersPopoverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:22 St�edn� Evropa (letn� �as)
