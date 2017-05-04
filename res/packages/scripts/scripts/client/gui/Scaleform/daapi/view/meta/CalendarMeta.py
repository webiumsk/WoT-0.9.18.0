# 2017.05.04 15:24:19 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CalendarMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CalendarMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onMonthChanged(self, rawDate):
        self._printOverrideError('onMonthChanged')

    def onDateSelected(self, rawDate):
        self._printOverrideError('onDateSelected')

    def formatYMHeader(self, rawDate):
        self._printOverrideError('formatYMHeader')

    def as_openMonthS(self, rawDate):
        if self._isDAAPIInited():
            return self.flashObject.as_openMonth(rawDate)

    def as_selectDateS(self, rawDate):
        if self._isDAAPIInited():
            return self.flashObject.as_selectDate(rawDate)

    def as_updateMonthEventsS(self, items):
        """
        :param items: Represented by Array (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateMonthEvents(items)

    def as_setCalendarMessageS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setCalendarMessage(message)

    def as_setMinAvailableDateS(self, rawDate):
        if self._isDAAPIInited():
            return self.flashObject.as_setMinAvailableDate(rawDate)

    def as_setMaxAvailableDateS(self, rawDate):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxAvailableDate(rawDate)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\CalendarMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:19 Støední Evropa (letní èas)
