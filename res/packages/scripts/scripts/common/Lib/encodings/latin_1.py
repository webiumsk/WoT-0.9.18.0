# 2017.05.04 15:32:17 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/encodings/latin_1.py
""" Python 'latin-1' Codec


Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""
import codecs

class Codec(codecs.Codec):
    encode = codecs.latin_1_encode
    decode = codecs.latin_1_decode


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final = False):
        return codecs.latin_1_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final = False):
        return codecs.latin_1_decode(input, self.errors)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


class StreamConverter(StreamWriter, StreamReader):
    encode = codecs.latin_1_decode
    decode = codecs.latin_1_encode


def getregentry():
    return codecs.CodecInfo(name='iso8859-1', encode=Codec.encode, decode=Codec.decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\encodings\latin_1.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:17 Støední Evropa (letní èas)
