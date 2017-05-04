# 2017.05.04 15:32:18 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/encodings/mbcs.py
""" Python 'mbcs' Codec for Windows


Cloned by Mark Hammond (mhammond@skippinet.com.au) from ascii.py,
which was written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""
from codecs import mbcs_encode, mbcs_decode
import codecs
encode = mbcs_encode

def decode(input, errors = 'strict'):
    return mbcs_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final = False):
        return mbcs_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = mbcs_decode


class StreamWriter(codecs.StreamWriter):
    encode = mbcs_encode


class StreamReader(codecs.StreamReader):
    decode = mbcs_decode


def getregentry():
    return codecs.CodecInfo(name='mbcs', encode=encode, decode=decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\encodings\mbcs.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:18 Støední Evropa (letní èas)
