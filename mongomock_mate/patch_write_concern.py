#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
monkey patch ``mongomock.write_concern``
"""

from mongomock.write_concern import WriteConcern


def _write_concern_init(self, w=None, wtimeout=None, j=None, fsync=None):
    self.__document = {}
    self.acknowledged = True
    self.server_default = not self.document


@property
def _write_concern_document(self):
    return self.__document.copy()


WriteConcern.__init__ = _write_concern_init
WriteConcern.document = _write_concern_document
