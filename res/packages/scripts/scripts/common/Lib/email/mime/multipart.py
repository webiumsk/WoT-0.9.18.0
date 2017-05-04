# 2017.05.04 15:32:01 Støední Evropa (letní èas)
# Embedded file name: scripts/common/Lib/email/mime/multipart.py
"""Base class for MIME multipart/* type messages."""
__all__ = ['MIMEMultipart']
from email.mime.base import MIMEBase

class MIMEMultipart(MIMEBase):
    """Base class for MIME multipart/* type messages."""

    def __init__(self, _subtype = 'mixed', boundary = None, _subparts = None, **_params):
        """Creates a multipart/* type message.
        
        By default, creates a multipart/mixed message, with proper
        Content-Type and MIME-Version headers.
        
        _subtype is the subtype of the multipart content type, defaulting to
        `mixed'.
        
        boundary is the multipart boundary string.  By default it is
        calculated as needed.
        
        _subparts is a sequence of initial subparts for the payload.  It
        must be an iterable object, such as a list.  You can always
        attach new subparts to the message by using the attach() method.
        
        Additional parameters for the Content-Type header are taken from the
        keyword arguments (or passed into the _params argument).
        """
        MIMEBase.__init__(self, 'multipart', _subtype, **_params)
        self._payload = []
        if _subparts:
            for p in _subparts:
                self.attach(p)

        if boundary:
            self.set_boundary(boundary)
# okay decompyling C:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\email\mime\multipart.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.05.04 15:32:01 Støední Evropa (letní èas)
