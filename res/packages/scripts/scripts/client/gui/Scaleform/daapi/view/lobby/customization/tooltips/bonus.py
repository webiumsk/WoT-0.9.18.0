# 2017.05.04 15:23:10 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/customization/tooltips/bonus.py
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.locale.VEHICLE_CUSTOMIZATION import VEHICLE_CUSTOMIZATION
from gui.shared.formatters import text_styles
from gui.shared.tooltips.common import BlocksTooltipData
from gui.shared.tooltips import formatters, TOOLTIP_TYPE
from helpers.i18n import makeString as _ms
from gui import makeHtmlString
from gui.customization.controller import g_customizationController as controller
from gui.customization.shared import CUSTOMIZATION_TYPE, QUALIFIER_TYPE
_BONUS_TOOLTIP_NAME = {QUALIFIER_TYPE.ALL: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_TOOLTIP_BONUS_ENTIRECREW,
 QUALIFIER_TYPE.RADIOMAN: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_TOOLTIP_BONUS_RADIOMAN,
 QUALIFIER_TYPE.COMMANDER: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_TOOLTIP_BONUS_COMMANDER,
 QUALIFIER_TYPE.DRIVER: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_TOOLTIP_BONUS_DRIVER,
 QUALIFIER_TYPE.GUNNER: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_TOOLTIP_BONUS_AIMER,
 QUALIFIER_TYPE.LOADER: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_TOOLTIP_BONUS_LOADER,
 QUALIFIER_TYPE.CAMOUFLAGE: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_TOOLTIP_BONUS_MASKING}
_BONUS_TOOLTIP_BODY = {QUALIFIER_TYPE.ALL: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_BONUSPANEL_BONUS_ENTIRECREW_BODY,
 QUALIFIER_TYPE.RADIOMAN: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_BONUSPANEL_BONUS_RADIOMAN_BODY,
 QUALIFIER_TYPE.COMMANDER: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_BONUSPANEL_BONUS_COMMANDER_BODY,
 QUALIFIER_TYPE.DRIVER: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_BONUSPANEL_BONUS_DRIVER_BODY,
 QUALIFIER_TYPE.GUNNER: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_BONUSPANEL_BONUS_AIMER_BODY,
 QUALIFIER_TYPE.LOADER: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_BONUSPANEL_BONUS_LOADER_BODY,
 QUALIFIER_TYPE.CAMOUFLAGE: VEHICLE_CUSTOMIZATION.CUSTOMIZATION_BONUSPANEL_BONUS_MASKING_BODY}

class BonusTooltip(BlocksTooltipData):

    def __init__(self, context):
        super(BonusTooltip, self).__init__(context, TOOLTIP_TYPE.TECH_CUSTOMIZATION_BONUS)
        self._setContentMargin(top=20, left=20, bottom=20, right=20)
        self._setMargins(afterBlock=14)
        self._setWidth(330)

    def _packBlocks(self, *args):
        self.__hasAppliedElements = False
        data = controller.bonusPanel.bonusData[args[0]]
        bonuses = super(BonusTooltip, self)._packBlocks()
        bonus = self.__getData(data, args[0])
        bonuses.append(self._packTitleBlock(bonus['title']))
        bonuses.append(self._packDescriptionBlock(bonus['description']))
        if CUSTOMIZATION_TYPE.CAMOUFLAGE in bonus['customizationTypes']:
            bonuses.append(self._packBonusBlock(bonus['customizationTypes'][CUSTOMIZATION_TYPE.CAMOUFLAGE], VEHICLE_CUSTOMIZATION.TYPESWITCHSCREEN_TYPENAME_PLURAL_0))
        if CUSTOMIZATION_TYPE.EMBLEM in bonus['customizationTypes']:
            bonuses.append(self._packBonusBlock(bonus['customizationTypes'][CUSTOMIZATION_TYPE.EMBLEM], VEHICLE_CUSTOMIZATION.TYPESWITCHSCREEN_TYPENAME_PLURAL_1))
        if CUSTOMIZATION_TYPE.INSCRIPTION in bonus['customizationTypes']:
            bonuses.append(self._packBonusBlock(bonus['customizationTypes'][CUSTOMIZATION_TYPE.INSCRIPTION], VEHICLE_CUSTOMIZATION.TYPESWITCHSCREEN_TYPENAME_PLURAL_2))
        if self.__hasAppliedElements:
            bonuses.append(self._packFooterBlock(bonus))
        return bonuses

    def _packTitleBlock(self, title):
        return formatters.packTitleDescBlock(title=text_styles.highTitle(title), padding={'top': -5})

    def _packDescriptionBlock(self, customizationType):
        return formatters.packBuildUpBlockData([formatters.packImageTextBlockData(img=customizationType['img'], desc=customizationType['description'], imgPadding={'right': 10})], 0, BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_WHITE_BG_LINKAGE)

    def _packBonusBlock(self, customizationTypeData, title):
        subBlocks = [formatters.packTextBlockData(text=text_styles.middleTitle(_ms(title)), padding={'bottom': 2})]
        for bonus in customizationTypeData:
            bonusPartDescription = text_styles.main(bonus['title'])
            if bonus['isTemporarily']:
                bonusPartDescription += '\n' + text_styles.standard('*' + bonus['description'])
            subBlocks.append(formatters.packTextParameterBlockData(name=bonusPartDescription, value=bonus['power'], padding={'bottom': 8}, valueWidth=45))

        return formatters.packBuildUpBlockData(subBlocks, 0, BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_LINKAGE, {'left': 3})

    @staticmethod
    def _packFooterBlock(item):
        status = text_styles.standard(_ms(VEHICLE_CUSTOMIZATION.CUSTOMIZATION_BONUSPANEL_BONUS_FOOTER))
        return formatters.packTextBlockData(text=makeHtmlString('html_templates:lobby/textStyle', 'alignText', {'align': 'center',
         'message': status}), padding={'bottom': -4,
         'top': -4})

    def __getData(self, singleBonusData, qTypeName):
        item = {'title': _ms(VEHICLE_CUSTOMIZATION.CUSTOMIZATION_BONUSPANEL_BONUS_HEADER, bonus=_ms(_BONUS_TOOLTIP_NAME[qTypeName])),
         'description': {'img': singleBonusData['bonusIcon'],
                         'description': text_styles.main(_BONUS_TOOLTIP_BODY[qTypeName])},
         'customizationTypes': self.__aggregateBonusesInfo(singleBonusData)}
        return item

    def __aggregateBonusesInfo(self, singleBonusData):
        bonusVOs = {}
        for cType in CUSTOMIZATION_TYPE.ALL:
            if not singleBonusData[cType]:
                continue
            bonusVOs[cType] = []
            for cItemData in singleBonusData[cType]:
                if cItemData['isApplied'] and not self.__hasAppliedElements:
                    self.__hasAppliedElements = True
                cItem = cItemData['available']
                cInstalledItem = cItemData['installed']
                bonusDescription = cItem.qualifier.getDescription()
                if cItemData['isApplied']:
                    durationInfo = ''
                    powerFormatter = text_styles.bonusAppliedText
                    titleFormatter = text_styles.bonusAppliedText
                else:
                    powerFormatter = text_styles.stats
                    titleFormatter = text_styles.main
                    if cItem.isInDossier:
                        durationInfo = ' ({0})'.format(_ms('#vehicle_customization:bonusPanel/tooltip/duration/0'))
                    else:
                        durationInfo = ' ({0})'.format(_ms('#vehicle_customization:bonusPanel/tooltip/duration/1', numberOfDaysLeft=cInstalledItem.numberOfDaysLeft))
                power = '+{0}%{1}'.format(cItem.qualifier.getValue(), '*' if bonusDescription is not None else '')
                singleBonus = {'power': powerFormatter(power),
                 'title': '{0}{1}'.format(titleFormatter(cItem.getName()), durationInfo),
                 'isTemporarily': bonusDescription is not None}
                if bonusDescription is not None:
                    singleBonus['description'] = text_styles.standard(bonusDescription)
                bonusVOs[cType].append(singleBonus)

        return bonusVOs
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\customization\tooltips\bonus.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:23:10 St�edn� Evropa (letn� �as)
