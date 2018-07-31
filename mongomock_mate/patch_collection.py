#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
monkey patch ``mongomock.collection``
"""

from mongomock.collection import Collection
from mongomock.write_concern import WriteConcern

Collection._write_concern_attr = None


@property
def _collection_write_concern(self):
    if self._write_concern_attr is None:
        self._write_concern_attr = WriteConcern()
    return self._write_concern_attr


Collection.write_concern = _collection_write_concern
