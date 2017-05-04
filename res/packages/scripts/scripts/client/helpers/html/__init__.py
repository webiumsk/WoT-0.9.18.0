# 2017.05.04 15:26:50 Støední Evropa (letní èas)
# Embedded file name: scripts/client/helpers/html/__init__.py
from debug_utils import LOG_CURRENT_EXCEPTION
from helpers import i18n
import re
_getText_re = re.compile('\\_\\(([^)]+)\\)', re.U | re.M)

def _search(match):
    if match.group(1):
        return i18n.makeString(match.group(1))
    return ''


def escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')


def translation(text):
    result = text
    try:
        result = _getText_re.sub(_search, text)
    except re.error:
        LOG_CURRENT_EXCEPTION()
    finally:
        return result
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\helpers\html\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:50 Støední Evropa (letní èas)
