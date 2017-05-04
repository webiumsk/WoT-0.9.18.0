# 2017.05.04 15:27:11 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/proto/bw/bw_chat_string_utils.py
from external_strings_utils import unicode_from_utf8
from gui.Scaleform.locale.MESSENGER import MESSENGER
from messenger.proto.bw.errors import I18nError
from messenger.proto.bw.limits import CHANNEL_LIMIT

def validateUserRoomName(name):
    name = name.strip()
    if not name or len(unicode_from_utf8(name)[0]) not in xrange(CHANNEL_LIMIT.NAME_MIN_LENGTH, CHANNEL_LIMIT.NAME_MAX_LENGTH + 1):
        error = I18nError(MESSENGER.CLIENT_ERROR_LIMIT_CHANNEL_INVALID_LENGTH, int32Arg1=CHANNEL_LIMIT.NAME_MIN_LENGTH, int32Arg2=CHANNEL_LIMIT.NAME_MAX_LENGTH)
        return (name, error)
    else:
        return (name, None)


def validateUserRoomPwd(password, isRetype = False):
    pwdRange = xrange(CHANNEL_LIMIT.PWD_MIN_LENGTH, CHANNEL_LIMIT.PWD_MAX_LENGTH + 1)
    if password is None or len(unicode_from_utf8(password)[0]) not in pwdRange:
        if isRetype:
            key = MESSENGER.CLIENT_ERROR_CHANNEL_RETYPE_INVALID
        else:
            key = MESSENGER.CLIENT_ERROR_CHANNEL_PASSWORD_INVALID
        error = I18nError(key, int32Arg1=CHANNEL_LIMIT.PWD_MIN_LENGTH, int32Arg2=CHANNEL_LIMIT.PWD_MAX_LENGTH)
        return ('', error)
    else:
        return (password, None)


def validateUserRoomPwdPair(password, retype):
    password, error = validateUserRoomPwd(password, isRetype=False)
    if error is not None:
        return ('', error)
    retype, error = validateUserRoomPwd(retype, isRetype=True)
    if error is not None:
        return ('', error)
    elif password != retype:
        error = I18nError(MESSENGER.CLIENT_ERROR_CHANNEL_PASSWORDS_NOT_EQUALS)
        return ('', error)
    else:
        return (password, None)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\bw\bw_chat_string_utils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:27:12 St�edn� Evropa (letn� �as)
