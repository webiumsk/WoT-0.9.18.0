# 2017.05.04 15:21:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/doc_loaders/messages_panel_reader.py
from helpers import html
import resource_helper
_EXPECTED_STYLES = {'entityStyle': ('fontSize', 'fontFace', 'fontColor')}

def _getDefaultSettings():
    return {'direction': 'up',
     'lifeTime': 1000,
     'alphaSpeed': 1000,
     'maxLinesCount': 5,
     'poolSettings': (),
     'textBottomPadding': 0.0,
     'textRightPadding': 0.0,
     'useHtml': False,
     'showUniqueOnly': False,
     'messageGap': 0}


def _readSettings(ctx, root):
    ctx, section = resource_helper.getSubSection(ctx, root, 'settings')
    settings = _getDefaultSettings()
    for ctx, subSection in resource_helper.getIterator(ctx, section):
        item = resource_helper.readItem(ctx, subSection, 'setting')
        settings[item.name] = item.value

    return settings


def _readStyles(ctx, root):
    ctx, section = resource_helper.getSubSection(ctx, root, 'styles', safe=True)
    styles = {}
    if section is not None:
        for ctx, subSection in resource_helper.getIterator(ctx, section):
            item = resource_helper.readItem(ctx, subSection, 'style')
            raise item.name in _EXPECTED_STYLES or AssertionError('Style section %s is not expected!' % item.name)
            expectedKeys = _EXPECTED_STYLES[item.name]
            for key in expectedKeys:
                raise key in item.value or AssertionError('Style option %s is expected in section %s!' % (key, item.name))

            styles[item.name] = item.value

    return styles


def _readMessages(ctx, root):
    ctx, section = resource_helper.getSubSection(ctx, root, 'messages')
    messages = {}
    for ctx, subSection in resource_helper.getIterator(ctx, section):
        item = resource_helper.readItem(ctx, subSection, 'message')
        text, aliases = item.value
        aliases = aliases.split(',', 1)
        if len(aliases) == 1:
            aliases *= 2
        messages[item.name] = (html.translation(text), tuple(aliases))

    return messages


_cache = {}

def readXML(path):
    global _cache
    if path in _cache:
        return _cache[path]
    ctx, root = resource_helper.getRoot(path)
    settings = _readSettings(ctx, root)
    styles = _readStyles(ctx, root)
    messages = _readMessages(ctx, root)
    _cache[path] = (settings, styles, messages)
    return (settings, styles, messages)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\doc_loaders\messages_panel_reader.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:37 St�edn� Evropa (letn� �as)
