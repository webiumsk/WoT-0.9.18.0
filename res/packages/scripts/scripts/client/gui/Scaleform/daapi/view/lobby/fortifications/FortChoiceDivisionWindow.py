# 2017.05.04 15:23:17 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/FortChoiceDivisionWindow.py
from UnitBase import SORTIE_DIVISION
from adisp import process
from constants import PREBATTLE_TYPE
from gui.Scaleform.daapi.view.lobby.fortifications.components.sorties_dps import makeDivisionData
from gui.Scaleform.daapi.view.lobby.fortifications.fort_utils import fort_formatters
from gui.Scaleform.daapi.view.meta.FortChoiceDivisionWindowMeta import FortChoiceDivisionWindowMeta
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS as I18N_FORTIFICATIONS
from gui.prb_control.entities.base.unit.ctx import ChangeDivisionUnitCtx
from gui.prb_control.items.unit_items import SupportedRosterSettings
from gui.prb_control import prbDispatcherProperty
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.events import FortEvent
from gui.shared.formatters.text_styles import main, standard, highTitle
from helpers import i18n

def _getTextLevels(lvl):
    return main(fort_formatters.getTextLevel(lvl))


class FortChoiceDivisionWindow(FortChoiceDivisionWindowMeta):

    def __init__(self, ctx = None):
        super(FortChoiceDivisionWindow, self).__init__()
        self.__isInChangeDivisionMode = ctx.get('isInChangeDivisionMode', False)
        self.__divisionID = ctx.get('division', None)
        return

    @prbDispatcherProperty
    def prbDispatcher(self):
        return None

    def onWindowClose(self):
        self.destroy()

    @process
    def sendRequest(self, request):
        yield self.prbDispatcher.sendPrbRequest(request)

    def selectedDivision(self, divisionID):
        if self.__divisionID is None:
            self.__divisionID = divisionID
            self.fireEvent(FortEvent(FortEvent.CHOICE_DIVISION, ctx={'data': divisionID}), EVENT_BUS_SCOPE.LOBBY)
        else:
            self.changedDivision(divisionID)
        return

    def changedDivision(self, divisionID):
        if divisionID != self.__divisionID:
            self.__divisionID = divisionID
            self.sendRequest(ChangeDivisionUnitCtx(int(divisionID), 'prebattle/changeDivision'))

    def _populate(self):
        super(FortChoiceDivisionWindow, self)._populate()
        self.playersRange = []
        for roster in SupportedRosterSettings.list(PREBATTLE_TYPE.SORTIE):
            self.playersRange.append((roster.getMinSlots(), roster.getMaxSlots()))

        self.__makeData()

    def _dispose(self):
        self.playersRange = None
        super(FortChoiceDivisionWindow, self)._dispose()
        return

    def __makeData(self):
        data = {}
        if self.__isInChangeDivisionMode:
            data['windowTitle'] = I18N_FORTIFICATIONS.CHOICEDIVISION_CHANGEWINDOWTITLE
        else:
            data['windowTitle'] = I18N_FORTIFICATIONS.CHOICEDIVISION_WINDOWTITLE
        data['description'] = main(i18n.makeString(I18N_FORTIFICATIONS.CHOICEDIVISION_DESCRIPTION))
        if self.__isInChangeDivisionMode:
            data['applyBtnLbl'] = I18N_FORTIFICATIONS.CHOICEDIVISION_CHANGEBTNLBL
            data['windowTitle'] = I18N_FORTIFICATIONS.CHOICEDIVISION_CHANGEWINDOWTITLE
        else:
            data['applyBtnLbl'] = I18N_FORTIFICATIONS.CHOICEDIVISION_APPLYBTNLBL
            data['windowTitle'] = I18N_FORTIFICATIONS.CHOICEDIVISION_WINDOWTITLE
        data['cancelBtnLbl'] = I18N_FORTIFICATIONS.CHOICEDIVISION_CANCELBTNLBL
        list = makeDivisionData()
        autoSelectDivision = None
        for item in list:
            if item['level'] == SORTIE_DIVISION.MIDDLE:
                autoSelectDivision = item['level']

        divisionSelector = self.__makeDivisionsData(list)
        data['selectorsData'] = divisionSelector
        data['isInChangeDivisionMode'] = self.__isInChangeDivisionMode
        if self.__isInChangeDivisionMode:
            autoSelectDivision = data['currentDivisionID'] = self.__divisionID
        data['autoSelect'] = autoSelectDivision
        self.as_setDataS(data)
        return

    def __makeDivisionsData(self, list):
        result = []
        for item in list:
            divisionType = {}
            title = i18n.makeString(item['label'])
            profit = fort_formatters.getDefRes(item['profit'])
            divisionID = item['level']
            divisionType['divisionName'] = highTitle(i18n.makeString(I18N_FORTIFICATIONS.CHOICEDIVISION_DIVISIONFULLNAME, divisionType=title))
            divisionType['divisionProfit'] = standard(i18n.makeString(I18N_FORTIFICATIONS.CHOICEDIVISION_DIVISIONPROFIT, defResCount=profit))
            minVehLvl, maxVehLvl = item['vehLvls']
            if maxVehLvl == minVehLvl:
                vehicleLevel = i18n.makeString(I18N_FORTIFICATIONS.CHOICEDIVISION_VEHICLELEVELSINGLE, level=_getTextLevels(maxVehLvl))
            else:
                vehicleLevel = i18n.makeString(I18N_FORTIFICATIONS.CHOICEDIVISION_VEHICLELEVEL, minLevel=_getTextLevels(minVehLvl), maxLevel=_getTextLevels(maxVehLvl))
            divisionType['vehicleLevel'] = standard(vehicleLevel)
            divisionType['divisionID'] = divisionID
            if divisionID == SORTIE_DIVISION.MIDDLE:
                minCount, maxCount = self.playersRange[0]
            elif divisionID == SORTIE_DIVISION.CHAMPION:
                minCount, maxCount = self.playersRange[1]
            else:
                minCount, maxCount = self.playersRange[2]
            divisionType['playerRange'] = main('{0}-{1}'.format(str(minCount), str(maxCount)))
            result.append(divisionType)

        return result
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\fortifications\FortChoiceDivisionWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:17 St�edn� Evropa (letn� �as)
