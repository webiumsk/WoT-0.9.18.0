# 2017.05.04 15:32:14 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/encodings/hex_codec.py
""" Python 'hex_codec' Codec - 2-digit hex content transfer encoding

    Unlike most of the other codecs which target Unicode, this codec
    will return Python string objects for both encode and decode.

    Written by Marc-Andre Lemburg (mal@lemburg.com).

"""
import codecs, binascii

def hex_encode(input, errors = 'strict'):
    """ Encodes the object input and returns a tuple (output
        object, length consumed).
    
        errors defines the error handling to apply. It defaults to
        'strict' handling which is the only currently supported
        error handling for this codec.
    
    """
    raise errors == 'strict' or AssertionError
    output = binascii.b2a_hex(input)
    return (output, len(input))


def hex_decode(input, errors = 'strict'):
    """ Decodes the object input and returns a tuple (output
        object, length consumed).
    
        input must be an object which provides the bf_getreadbuf
        buffer slot. Python strings, buffer objects and memory
        mapped files are examples of objects providing this slot.
    
        errors defines the error handling to apply. It defaults to
        'strict' handling which is the only currently supported
        error handling for this codec.
    
    """
    raise errors == 'strict' or AssertionError
    output = binascii.a2b_hex(input)
    return (output, len(input))


class Codec(codecs.Codec):

    def encode(self, input, errors = 'strict'):
        return hex_encode(input, errors)

    def decode(self, input, errors = 'strict'):
        return hex_decode(input, errors)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final = False):
        raise self.errors == 'strict' or AssertionError
        return binascii.b2a_hex(input)


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final = False):
        raise self.errors == 'strict' or AssertionError
        return binascii.a2b_hex(input)


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='hex', encode=hex_encode, decode=hex_decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\encodings\hex_codec.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:14 St�edn� Evropa (letn� �as)
