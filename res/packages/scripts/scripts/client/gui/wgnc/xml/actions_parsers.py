# 2017.05.04 15:26:35 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/wgnc/xml/actions_parsers.py
from gui.wgnc import actions
from gui.wgnc.wgnc_helpers import parseSize
from gui.wgnc.errors import ParseError
from gui.wgnc.xml.shared_parsers import SectionParser, ParsersCollection

class _CallbackActionParser(SectionParser):

    def getTagName(self):
        return 'callback'

    def parse(self, section):
        return actions.Callback(self._readString('name', section), section.readBool('purge', True))


class _BrowseActionParser(SectionParser):

    def getTagName(self):
        return 'browse'

    def parse(self, section):
        name = self._readString('name', section)
        url = self._readString('href', section)
        target = section.readString('target', 'internal')
        if target == 'internal':
            size = parseSize(section.readString('size'))
            showRefresh = section.readBool('show_refresh')
            webClientHandler = section.readString('web_client_handler')
            action = actions.OpenInternalBrowser(name, url, size, showRefresh, webClientHandler)
        elif target == 'external':
            action = actions.OpenExternalBrowser(name, url)
        elif target == 'promo':
            action = actions.OpenPromoBrowser(name, url)
        else:
            raise ParseError('The target of action "{0}" is not valid: {1}.'.format(self.getTagName(), target))
        return action


class _OpenWindowParser(SectionParser):

    def getTagName(self):
        return 'openwindow'

    def parse(self, section):
        return actions.OpenWindow(self._readString('name', section), self._readString('target', section))


class _ReplaceButtonsAction(SectionParser):

    def getTagName(self):
        return 'replace_buttons'

    def parse(self, section):
        text = section.asString
        if not text:
            raise ParseError('The content of action "{0}" is not defined.'.format(self.getTagName()))
        return actions.ReplaceButtons(self._readString('name', section), section.asString)


class _ActionsParser(ParsersCollection):

    def getTagName(self):
        return 'actions'

    def parse(self, section):
        items = []
        for item in super(_ActionsParser, self).parse(section):
            items.append(item)

        return actions.ActionsHolder(items)


class ActionsParser_v2(_ActionsParser):

    def __init__(self):
        super(ActionsParser_v2, self).__init__((_CallbackActionParser(),
         _BrowseActionParser(),
         _OpenWindowParser(),
         _ReplaceButtonsAction()))
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\wgnc\xml\actions_parsers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:26:35 St�edn� Evropa (letn� �as)
