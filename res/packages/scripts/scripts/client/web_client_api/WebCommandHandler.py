# 2017.05.04 15:28:09 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/web_client_api/WebCommandHandler.py
import json
from . import WebCommandException
from commands import WebCommand, instantiateObject, CommandHandler
from debug_utils import LOG_WARNING, LOG_DEBUG
from Event import Event

class WebCommandHandler(object):
    """
    Purpose of this class is to receive json messages from Browser parse them,
    create appropriate commands and handle created commands.
    """

    def __init__(self, browserID, alias):
        self.__handlers = []
        self.__browserID = browserID
        self.__alias = alias
        self.onCallback = Event()

    def handleCommand(self, data):
        LOG_DEBUG('Web2Client handle: %s' % data)
        try:
            parsed = json.loads(data, encoding='utf-8')
        except (TypeError, ValueError) as exception:
            raise WebCommandException('Command parse failed! Description: %s' % exception)

        command = instantiateObject(WebCommand, parsed)
        self.handleWebCommand(command)

    def addHandlers(self, handlers):
        for handler in handlers:
            self.addHandler(handler)

    def addHandler(self, handler):
        if not isinstance(handler, CommandHandler):
            raise AssertionError
            handler not in self.__handlers and self.__handlers.append(handler)
        else:
            LOG_WARNING('Handler %s already added to WebCommandHandler!' % str(handler))

    def removeHandler(self, handler):
        if handler in self.__handlers:
            self.__handlers.remove(handler)

    def handleWebCommand(self, webCommand):
        commandName = webCommand.command
        for handler in self.__handlers:
            if commandName == handler.name:
                command = instantiateObject(handler.cls, webCommand.params)
                handler.handler(command, self.__createCtx(commandName))
                return

        raise WebCommandException("Command '%s' is unsupported!" % commandName)

    def __createCtx(self, commandName):

        def callback(data):
            callbackData = {'command': commandName,
             'data': data}
            LOG_DEBUG('Web2Client callback: %s' % callbackData)
            jsonMessage = json.dumps(callbackData).replace('"', '\\"')
            self.onCallback(jsonMessage)

        return {'browser_id': self.__browserID,
         'browser_alias': self.__alias,
         'callback': callback}
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\web_client_api\WebCommandHandler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:28:09 St�edn� Evropa (letn� �as)
