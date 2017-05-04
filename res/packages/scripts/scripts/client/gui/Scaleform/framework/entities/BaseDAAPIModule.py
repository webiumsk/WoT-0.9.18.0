# 2017.05.04 15:24:44 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/BaseDAAPIModule.py
from debug_utils import LOG_ERROR
from gui.Scaleform.framework.entities.abstract.BaseDAAPIModuleMeta import BaseDAAPIModuleMeta

class BaseDAAPIModule(BaseDAAPIModuleMeta):

    def __init__(self):
        super(BaseDAAPIModule, self).__init__()
        self.__isScriptSet = False
        self.__isPyReloading = False
        self.__app = None
        return

    @property
    def app(self):
        return self.__app

    def setEnvironment(self, app):
        """Sets some required environment for instance of DAAPIModule.
        :param app: instance of application.
        """
        self.__app = app

    def setPyReloading(self, flag):
        self.__isPyReloading = flag

    def _printOverrideError(self, methodName):
        LOG_ERROR('Method must be override!', methodName, self.__class__)

    def setFlashObject(self, movieClip, autoPopulate = True, setScript = True):
        if movieClip is not None:
            self.__isScriptSet = setScript
            try:
                self.turnDAAPIon(setScript, movieClip)
            except:
                raise Exception('Can not initialize daapi in ' + str(self))

            if autoPopulate:
                if self.isCreated():
                    LOG_ERROR('object {0} is already created! Please, set flag autoPopulate=False'.format(str(self)))
                else:
                    self.create()
        else:
            LOG_ERROR('flashObject reference can`t be None!')
        return

    def _populate(self):
        super(BaseDAAPIModule, self)._populate()
        self.as_populateS()

    def _dispose(self):
        super(BaseDAAPIModule, self)._dispose()
        if self.flashObject is not None:
            try:
                if self.__isScriptSet and not self.__isPyReloading:
                    self.as_disposeS()
            except:
                LOG_ERROR('Error during %s flash disposing' % str(self))

            self.turnDAAPIoff(self.__isScriptSet)
        self.__app = None
        return
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\BaseDAAPIModule.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:24:44 St�edn� Evropa (letn� �as)
