# 2017.05.04 15:32:19 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/encodings/raw_unicode_escape.py
""" Python 'raw-unicode-escape' Codec


Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""
import codecs

class Codec(codecs.Codec):
    encode = codecs.raw_unicode_escape_encode
    decode = codecs.raw_unicode_escape_decode


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final = False):
        return codecs.raw_unicode_escape_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final = False):
        return codecs.raw_unicode_escape_decode(input, self.errors)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='raw-unicode-escape', encode=Codec.encode, decode=Codec.decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\encodings\raw_unicode_escape.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:19 Støední Evropa (letní èas)
