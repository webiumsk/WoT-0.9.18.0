# 2017.05.04 15:21:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/doc_loaders/GuiDirReader.py
import ResMgr

class GuiDirReader(object):
    SCALEFORM_STARTUP_VIDEO_PATH = 'gui/flash/video'
    SCALEFORM_STARTUP_VIDEO_MASK = 'video/%s'
    VIDEO_EXTENSION = 'usm'

    def __init__(self):
        super(GuiDirReader, self).__init__()

    @staticmethod
    def getAvailableIntroVideoFiles():
        ds = ResMgr.openSection(GuiDirReader.SCALEFORM_STARTUP_VIDEO_PATH)
        movieFiles = []
        for filename in ds.keys():
            basename, extension = filename.split('.')
            if extension == GuiDirReader.VIDEO_EXTENSION and basename[0:1] != '_':
                movieFiles.append(GuiDirReader.SCALEFORM_STARTUP_VIDEO_MASK % filename)

        ResMgr.purge(GuiDirReader.SCALEFORM_STARTUP_VIDEO_PATH, True)
        return movieFiles
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\doc_loaders\GuiDirReader.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:21:37 Støední Evropa (letní èas)
