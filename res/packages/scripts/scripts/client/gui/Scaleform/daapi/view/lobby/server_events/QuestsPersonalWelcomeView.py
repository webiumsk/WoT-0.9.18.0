# 2017.05.04 15:23:56 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/server_events/QuestsPersonalWelcomeView.py
import weakref
from gui.LobbyContext import g_lobbyContext
from helpers import i18n
from debug_utils import LOG_WARNING, LOG_CURRENT_EXCEPTION
from gui.shared.formatters import text_styles
from gui.server_events import settings as quest_settings
from gui.Scaleform.daapi.view.meta.QuestsPersonalWelcomeViewMeta import QuestsPersonalWelcomeViewMeta
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from constants import ARENA_GUI_TYPE_LABEL, ARENA_GUI_TYPE

class QuestsPersonalWelcomeView(QuestsPersonalWelcomeViewMeta):

    def __init__(self):
        super(QuestsPersonalWelcomeView, self).__init__()
        self.__proxy = None
        return

    def success(self):
        try:
            quest_settings.markPQIntroAsShown()
            self.__proxy._showSeasonsView()
        except:
            LOG_WARNING('Error while getting event window for showing seasons view')
            LOG_CURRENT_EXCEPTION()

    def _setMainView(self, eventsWindow):
        self.__proxy = weakref.proxy(eventsWindow)

    def _populate(self):
        super(QuestsPersonalWelcomeView, self)._populate()
        falloutEnabled = g_lobbyContext.getServerSettings().isFalloutQuestEnabled()
        if falloutEnabled:
            announcementIcon = ARENA_GUI_TYPE_LABEL.LABELS[ARENA_GUI_TYPE.FALLOUT_CLASSIC]
            announcementText = text_styles.promoSubTitle(QUESTS.QUESTSPERSONALWELCOMEVIEW_ANNOUNCEMENTTEXT)
            background = RES_ICONS.MAPS_ICONS_QUESTS_PROMOSCREEN_FALLOUT
        else:
            announcementIcon = None
            announcementText = None
            background = RES_ICONS.MAPS_ICONS_QUESTS_PROMOSCREEN
        self.as_setDataS({'buttonLbl': QUESTS.QUESTSPERSONALWELCOMEVIEW_BTNLABEL,
         'titleText': text_styles.promoTitle(i18n.makeString(QUESTS.QUESTSPERSONALWELCOMEVIEW_MAINTITLE_TEXTLABEL)),
         'blockData': self.__makeBlocksData(),
         'showAnnouncement': falloutEnabled,
         'announcementIcon': announcementIcon,
         'announcementText': announcementText,
         'background': background})
        return

    def _dispose(self):
        self.__proxy = None
        super(QuestsPersonalWelcomeView, self)._dispose()
        return

    def __makeBlocksData(self):
        result = []
        for blockName in ('block1', 'block2', 'block3'):
            result.append({'blockTitle': text_styles.promoSubTitle(i18n.makeString(QUESTS.questspersonalwelcomeview_textblock_header(blockName))),
             'blockBody': text_styles.main(i18n.makeString(QUESTS.questspersonalwelcomeview_textblock_body(blockName)))})

        return result
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\server_events\QuestsPersonalWelcomeView.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:56 St�edn� Evropa (letn� �as)
