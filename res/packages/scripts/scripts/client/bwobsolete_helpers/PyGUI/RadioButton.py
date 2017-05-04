# 2017.05.04 15:20:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/RadioButton.py
import BigWorld, GUI
from Button import Button
from CheckBox import CheckBox

class RadioButton(CheckBox):
    factoryString = 'PyGUI.RadioButton'

    def __init__(self, component):
        CheckBox.__init__(self, component)
        self.buttonStyle = Button.RADIOBUTTON_STYLE

    @staticmethod
    def create(texture, text = '', groupName = '', **kwargs):
        b = RadioButton(CheckBox.createInternal(texture, text, **kwargs), **kwargs)
        b.groupName = groupName
        return b.component
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bwobsolete_helpers\PyGUI\RadioButton.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:47 Støední Evropa (letní èas)
