# 2017.05.04 15:24:30 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/HangarMeta.py
from gui.Scaleform.framework.entities.View import View

class HangarMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def onEscape(self):
        self._printOverrideError('onEscape')

    def showHelpLayout(self):
        self._printOverrideError('showHelpLayout')

    def closeHelpLayout(self):
        self._printOverrideError('closeHelpLayout')

    def as_setCrewEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewEnabled(value)

    def as_setCarouselEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselEnabled(value)

    def as_setupAmmunitionPanelS(self, maintenanceEnabled, maintenanceTooltip, customizationEnabled, customizationTooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setupAmmunitionPanel(maintenanceEnabled, maintenanceTooltip, customizationEnabled, customizationTooltip)

    def as_setControlsVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setControlsVisible(value)

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)

    def as_showHelpLayoutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showHelpLayout()

    def as_closeHelpLayoutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closeHelpLayout()

    def as_showMiniClientInfoS(self, description, hyperlink):
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)

    def as_show3DSceneTooltipS(self, id, args):
        if self._isDAAPIInited():
            return self.flashObject.as_show3DSceneTooltip(id, args)

    def as_hide3DSceneTooltipS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide3DSceneTooltip()

    def as_setCarouselS(self, linkage, alias):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarousel(linkage, alias)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\HangarMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:30 St�edn� Evropa (letn� �as)
