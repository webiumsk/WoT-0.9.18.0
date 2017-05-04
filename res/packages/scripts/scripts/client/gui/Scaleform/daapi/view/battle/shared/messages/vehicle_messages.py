# 2017.05.04 15:22:41 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/messages/vehicle_messages.py
from MemoryCriticalController import g_critMemHandler
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.battle.shared.messages import fading_messages
from gui.shared.events import GameEvent
from helpers import i18n
from items import vehicles
_VEHICLE_TYPE_FORMATTER = ' <img src="img://gui/maps/icons/vehicleTypes/{0}.png" vspace="-4"/>'
_VEHICLE_STYLE_FORMATTER = '<font size="%(fontSize)s" face="%(fontFace)s" color="%(fontColor)s">{0}</font>'

class VehicleMessages(fading_messages.FadingMessages):

    def __init__(self):
        super(VehicleMessages, self).__init__('VehicleMessagesPanel', 'vehicle_messages_panel.xml')
        self.__styleFormatter = None
        return

    def __del__(self):
        LOG_DEBUG('VehicleMessages panel is deleted')

    def _populate(self):
        super(VehicleMessages, self)._populate()
        styles = self.getStyles()
        raise 'entityStyle' in styles or AssertionError('Entity styles for messages under Ammo panel are not defined!')
        self.__styleFormatter = _VEHICLE_STYLE_FORMATTER % styles['entityStyle']

    def _dispose(self):
        self.__styleFormatter = None
        super(VehicleMessages, self)._dispose()
        return

    def _addGameListeners(self):
        super(VehicleMessages, self)._addGameListeners()
        self.addListener(GameEvent.SCREEN_SHOT_MADE, self.__handleScreenShotMade)
        for message in g_critMemHandler.messages:
            self.__handleMemoryCriticalMessage(message)

        g_critMemHandler.onMemCrit += self.__handleMemoryCriticalMessage
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleMessageByCode += self.__onShowVehicleMessageByCode
            ctrl.onShowVehicleMessageByKey += self.__onShowVehicleMessageByKey
            ctrl.onUIPopulated()
        return

    def _removeGameListeners(self):
        self.removeListener(GameEvent.SCREEN_SHOT_MADE, self.__handleScreenShotMade)
        g_critMemHandler.onMemCrit -= self.__handleMemoryCriticalMessage
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleMessageByCode -= self.__onShowVehicleMessageByCode
            ctrl.onShowVehicleMessageByKey -= self.__onShowVehicleMessageByKey
        super(VehicleMessages, self)._removeGameListeners()
        return

    def __handleMemoryCriticalMessage(self, message):
        self.showMessage(message[1])

    def __handleScreenShotMade(self, event):
        if 'path' not in event.ctx:
            return
        self.showMessage('SCREENSHOT_CREATED', {'path': i18n.encodeUtf8(event.ctx['path'])})

    def __onShowVehicleMessageByCode(self, code, postfix, entityID, extra, equipmentID):
        LOG_DEBUG('onShowVehicleMessage', code, postfix, entityID, extra, equipmentID)
        names = {'device': '',
         'entity': '',
         'target': ''}
        if extra is not None:
            names['device'] = extra.deviceUserString
        if entityID:
            names['entity'] = self.__formatEntity(entityID)
        if equipmentID:
            equipment = vehicles.g_cache.equipments().get(equipmentID)
            if equipment is not None:
                postfix = '_'.join((postfix, equipment.name.split('_')[0].upper()))
        self.showMessage(code, names, postfix=postfix)
        return

    def __onShowVehicleMessageByKey(self, key, args = None, extra = None):
        self.showMessage(key, args, extra)

    def __formatEntity(self, entityID):
        ctx = self.sessionProvider.getCtx()
        vTypeInfoVO = ctx.getArenaDP().getVehicleInfo(entityID).vehicleType
        playerName = ctx.getPlayerFullName(entityID, showVehShortName=False)
        iconTag = _VEHICLE_TYPE_FORMATTER.format(vTypeInfoVO.classTag)
        playerInfo = '%s%s%s' % (playerName, iconTag, vTypeInfoVO.shortNameWithPrefix)
        entityInfo = self.__styleFormatter.format(playerInfo)
        return entityInfo
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\shared\messages\vehicle_messages.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:42 St�edn� Evropa (letn� �as)
