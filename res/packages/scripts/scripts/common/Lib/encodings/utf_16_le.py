# 2017.05.04 15:32:21 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/encodings/utf_16_le.py
""" Python 'utf-16-le' Codec


Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""
import codecs
encode = codecs.utf_16_le_encode

def decode(input, errors = 'strict'):
    return codecs.utf_16_le_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final = False):
        return codecs.utf_16_le_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_16_le_decode


class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_16_le_encode


class StreamReader(codecs.StreamReader):
    decode = codecs.utf_16_le_decode


def getregentry():
    return codecs.CodecInfo(name='utf-16-le', encode=encode, decode=decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\encodings\utf_16_le.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:21 Støední Evropa (letní èas)
