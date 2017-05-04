# 2017.05.04 15:22:51 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/AwardWindow.py
from collections import namedtuple
from gui.Scaleform.daapi.view.meta.MissionAwardWindowMeta import MissionAwardWindowMeta
from helpers import i18n
from gui.Scaleform.daapi.view.meta.AwardWindowMeta import AwardWindowMeta
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.genConsts.AWARDWINDOW_CONSTANTS import AWARDWINDOW_CONSTANTS
AwardsRibbonInfo = namedtuple('AwardsRibbonInfo', ['awardForCompleteText',
 'isAwardForCompleteVisible',
 'awardReceivedText',
 'isAwardsReceivedVisible',
 'awardBonusStrText',
 'isAwardBonusStrVisible',
 'ribbonSource',
 'awards'])

def packRibbonInfo(awards = None, awardForCompleteText = '', awardReceivedText = '', awardBonusStrText = ''):
    return AwardsRibbonInfo(awardForCompleteText=awardForCompleteText, isAwardForCompleteVisible=bool(len(awardForCompleteText)), awardReceivedText=awardReceivedText, isAwardsReceivedVisible=bool(len(awardReceivedText)), awardBonusStrText=awardBonusStrText, isAwardBonusStrVisible=bool(len(awardBonusStrText)), ribbonSource=RES_ICONS.MAPS_ICONS_QUESTS_AWARDRIBBON, awards=awards or [])


class AwardAbstract(object):

    def getWindowTitle(self):
        return ''

    def getBackgroundImage(self):
        return ''

    def useBackgroundAnimation(self):
        return False

    def getBackgroundAnimationData(self):
        return None

    def getAwardImage(self):
        return None

    def getHeader(self):
        return ''

    def getDescription(self):
        return ''

    def getAdditionalText(self):
        return ''

    def getTextAreaIconPath(self):
        return ''

    def getTextAreaIconIsShow(self):
        return False

    def getExtraFields(self):
        return {}

    def getHasDashedLine(self):
        return False

    def getButtonStates(self):
        return (True, False, False)

    def getOkButtonText(self):
        return i18n.makeString(MENU.AWARDWINDOW_OKBUTTON)

    def getCloseButtonText(self):
        return i18n.makeString(MENU.AWARDWINDOW_CLOSEBUTTON)

    def getBodyButtonText(self):
        return ''

    def getRibbonInfo(self):
        return None

    def handleOkButton(self):
        pass

    def handleCloseButton(self):
        pass

    def handleBodyButton(self):
        pass

    def clear(self):
        pass


class MissionAwardAbstract(AwardAbstract):

    def getRibbonImage(self):
        return ''

    def getCurrentQuestHeader(self):
        return ''

    def getCurrentQuestConditions(self):
        return None

    def getCurrentQuestConditionsText(self):
        return ''

    def getNextQuestHeader(self):
        return ''

    def getNextQuestConditions(self):
        return ''

    def getAdditionalStatusText(self):
        return ''

    def getMainStatusText(self):
        return ''

    def getMainStatusIcon(self):
        return ''

    def getAvalableText(self):
        return ''

    def getAdditionalStatusIcon(self):
        return ''

    def getNextButtonText(self):
        return ''

    def getNextButtonTooltip(self):
        return ''

    def isNextAvailable(self):
        return False

    def isLast(self):
        return False

    def isPersonal(self):
        return False

    def getAwards(self):
        return []

    def handleNextButton(self):
        pass

    def handleCurrentButton(self):
        pass


class ExplosionBackAward(AwardAbstract):

    def __init__(self, useAnimation = True):
        super(ExplosionBackAward, self).__init__()
        self.__useAnimation = useAnimation

    def getBackgroundImage(self):
        return RES_ICONS.MAPS_ICONS_REFERRAL_AWARDBACK

    def useBackgroundAnimation(self):
        return self.__useAnimation

    def getBackgroundAnimationData(self):
        if self.__useAnimation:
            return {'image': self.getAwardImage(),
             'animationPath': AWARDWINDOW_CONSTANTS.EXPLOSION_BACK_ANIMATION_PATH,
             'animationLinkage': AWARDWINDOW_CONSTANTS.EXPLOSION_BACK_ANIMATION_LINKAGE}
        else:
            return None


class AwardWindow(AwardWindowMeta):

    def __init__(self, ctx):
        super(AwardWindow, self).__init__()
        raise 'award' in ctx and isinstance(ctx['award'], AwardAbstract) or AssertionError
        self.__award = ctx['award']

    def onWindowClose(self):
        self.destroy()

    def onOKClick(self):
        self.__award.handleOkButton()
        self.onWindowClose()

    def onCloseClick(self):
        self.__award.handleCloseButton()
        self.onWindowClose()

    def onTakeNextClick(self):
        self.__award.handleBodyButton()
        self.onWindowClose()

    def _populate(self):
        super(AwardWindow, self)._populate()
        okBtn, closeBtn, bodyBtn = self.__award.getButtonStates()
        data = {'windowTitle': self.__award.getWindowTitle(),
         'backImage': self.__award.getBackgroundImage(),
         'useBackAnimation': self.__award.useBackgroundAnimation(),
         'backAnimationData': self.__award.getBackgroundAnimationData(),
         'awardImage': self.__award.getAwardImage(),
         'header': self.__award.getHeader(),
         'description': self.__award.getDescription(),
         'additionalText': self.__award.getAdditionalText(),
         'isDashLineEnabled': self.__award.getHasDashedLine(),
         'buttonText': self.__award.getOkButtonText(),
         'closeBtnLabel': self.__award.getCloseButtonText(),
         'takeNextBtnLabel': self.__award.getBodyButtonText(),
         'textAreaIconPath': self.__award.getTextAreaIconPath(),
         'textAreaIconIsShow': self.__award.getTextAreaIconIsShow(),
         'isOKBtnEnabled': okBtn,
         'isCloseBtnEnabled': closeBtn,
         'isTakeNextBtnEnabled': bodyBtn}
        data.update(self.__award.getExtraFields())
        ribbonInfo = self.__award.getRibbonInfo()
        if ribbonInfo is not None:
            data.update({'awardsBlock': ribbonInfo._asdict()})
        self.as_setDataS(data)
        return

    def _dispose(self):
        if self.__award is not None:
            self.__award.clear()
            self.__award = None
        super(AwardWindow, self)._dispose()
        return


class MissionAwardWindow(MissionAwardWindowMeta):

    def __init__(self, ctx):
        super(MissionAwardWindow, self).__init__()
        raise 'award' in ctx and isinstance(ctx['award'], AwardAbstract) or AssertionError
        self.__award = ctx['award']

    def onWindowClose(self):
        self.destroy()

    def onCurrentQuestClick(self):
        self.__award.handleNextButton()
        self.onWindowClose()

    def onNextQuestClick(self):
        self.__award.handleCurrentButton()
        self.onWindowClose()

    def _populate(self):
        super(MissionAwardWindow, self)._populate()
        data = {'windowTitle': self.__award.getWindowTitle(),
         'backImage': self.__award.getBackgroundImage(),
         'ribbonImage': self.__award.getRibbonImage(),
         'header': self.__award.getHeader(),
         'description': self.__award.getDescription(),
         'currentQuestHeader': self.__award.getCurrentQuestHeader(),
         'currentQuestConditions': self.__award.getCurrentQuestConditionsText(),
         'nextQuestHeader': self.__award.getNextQuestHeader(),
         'nextQuestConditions': self.__award.getNextQuestConditions(),
         'additionalStatusText': self.__award.getAdditionalStatusText(),
         'mainStatusText': self.__award.getMainStatusText(),
         'availableText': self.__award.getAvalableText(),
         'additionalStatusIcon': self.__award.getAdditionalStatusIcon(),
         'mainStatusIcon': self.__award.getMainStatusIcon(),
         'nextButtonText': self.__award.getNextButtonText(),
         'nextButtonTooltip': self.__award.getNextButtonTooltip(),
         'awards': self.__award.getAwards(),
         'conditions': self.__award.getCurrentQuestConditions(),
         'isPersonalQuest': self.__award.isPersonal(),
         'availableNextQuest': self.__award.isNextAvailable(),
         'isLastQuest': self.__award.isLast()}
        self.as_setDataS(data)

    def _dispose(self):
        self.__award.clear()
        self.__award = None
        super(MissionAwardWindow, self)._dispose()
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\AwardWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:22:51 St�edn� Evropa (letn� �as)
