# 2017.05.04 15:32:20 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/encodings/string_escape.py
""" Python 'escape' Codec


Written by Martin v. L\xf6wis (martin@v.loewis.de).

"""
import codecs

class Codec(codecs.Codec):
    encode = codecs.escape_encode
    decode = codecs.escape_decode


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final = False):
        return codecs.escape_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final = False):
        return codecs.escape_decode(input, self.errors)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='string-escape', encode=Codec.encode, decode=Codec.decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\encodings\string_escape.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:20 St�edn� Evropa (letn� �as)
