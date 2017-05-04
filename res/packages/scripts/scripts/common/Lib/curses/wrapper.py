# 2017.05.04 15:31:32 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/curses/wrapper.py
"""curses.wrapper

Contains one function, wrapper(), which runs another function which
should be the rest of your curses-based application.  If the
application raises an exception, wrapper() will restore the terminal
to a sane state so you can read the resulting traceback.

"""
import curses

def wrapper(func, *args, **kwds):
    """Wrapper function that initializes curses and calls another function,
    restoring normal keyboard/screen behavior on error.
    The callable object 'func' is then passed the main window 'stdscr'
    as its first argument, followed by any other arguments passed to
    wrapper().
    """
    try:
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(1)
        try:
            curses.start_color()
        except:
            pass

        return func(stdscr, *args, **kwds)
    finally:
        if 'stdscr' in locals():
            stdscr.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\curses\wrapper.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:31:32 St�edn� Evropa (letn� �as)
