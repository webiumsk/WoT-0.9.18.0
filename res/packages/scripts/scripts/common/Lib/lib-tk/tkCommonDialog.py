# 2017.05.04 15:32:53 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/lib-tk/tkCommonDialog.py
from Tkinter import *

class Dialog:
    command = None

    def __init__(self, master = None, **options):
        if TkVersion < 4.2:
            raise TclError, 'this module requires Tk 4.2 or newer'
        self.master = master
        self.options = options
        if not master and options.get('parent'):
            self.master = options['parent']

    def _fixoptions(self):
        pass

    def _fixresult(self, widget, result):
        return result

    def show(self, **options):
        for k, v in options.items():
            self.options[k] = v

        self._fixoptions()
        w = Frame(self.master)
        try:
            s = w.tk.call(self.command, *w._options(self.options))
            s = self._fixresult(w, s)
        finally:
            try:
                w.destroy()
            except:
                pass

        return s
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\lib-tk\tkCommonDialog.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:53 Støední Evropa (letní èas)
