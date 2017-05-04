# 2017.05.04 15:20:16 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/account_helpers/diff_utils.py
_KEY_DELIMITER = '.'

def synchronizeDicts(diff, cache, parentKey = '', changeList = None, defaultCacheType = dict):
    updates, replaces, deletes = (0, 0, 0)
    if parentKey is not '':
        parentKey = parentKey + _KEY_DELIMITER
    keys_r, keys_d, keys_u = [], [], []
    for k in diff.iterkeys():
        if changeList is not None and isinstance(k, basestring):
            changeList[parentKey + k] = diff[k]
        if isinstance(k, tuple):
            if k[1] == '_r':
                keys_r.append(k)
                replaces += 1
                continue
            elif k[1] == '_d':
                keys_d.append(k)
                deletes += 1
                continue
        keys_u.append(k)
        updates += 1

    for key_r in keys_r:
        cache[key_r[0]] = diff[key_r]

    for key_d in keys_d:
        value = cache.get(key_d[0], None)
        if value:
            value.difference_update(diff[key_d])

    for key_u in keys_u:
        value = diff[key_u]
        if value is None:
            cache.pop(key_u, None)
        elif isinstance(value, dict):
            newParentKey = parentKey + str(key_u) if changeList is not None else ''
            result = synchronizeDicts(value, cache.setdefault(key_u, defaultCacheType()), newParentKey, changeList, defaultCacheType)
            updates, replaces, deletes = [ i + j for i, j in zip((updates, replaces, deletes), result) ]
        elif isinstance(value, set):
            cache.setdefault(key_u, set()).update(value)
        else:
            cache[key_u] = value

    return (updates, replaces, deletes)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\account_helpers\diff_utils.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:16 St�edn� Evropa (letn� �as)
