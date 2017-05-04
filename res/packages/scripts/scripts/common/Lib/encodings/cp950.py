# 2017.05.04 15:32:13 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/encodings/cp950.py
import _codecs_tw, codecs
import _multibytecodec as mbc
codec = _codecs_tw.getcodec('cp950')

class Codec(codecs.Codec):
    encode = codec.encode
    decode = codec.decode


class IncrementalEncoder(mbc.MultibyteIncrementalEncoder, codecs.IncrementalEncoder):
    codec = codec


class IncrementalDecoder(mbc.MultibyteIncrementalDecoder, codecs.IncrementalDecoder):
    codec = codec


class StreamReader(Codec, mbc.MultibyteStreamReader, codecs.StreamReader):
    codec = codec


class StreamWriter(Codec, mbc.MultibyteStreamWriter, codecs.StreamWriter):
    codec = codec


def getregentry():
    return codecs.CodecInfo(name='cp950', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\encodings\cp950.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:13 Støední Evropa (letní èas)
