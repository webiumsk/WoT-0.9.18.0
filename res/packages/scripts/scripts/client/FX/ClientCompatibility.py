# 2017.05.04 15:20:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/FX/ClientCompatibility.py
import BigWorld
if BigWorld.component == 'editor':

    def addMat(a, b):
        return 0


    def delMat(a):
        return 0


    BigWorld.addMat = addMat
    BigWorld.delMat = delMat

    def player():
        return None


    BigWorld.player = player
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\FX\ClientCompatibility.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:20:51 Støední Evropa (letní èas)
