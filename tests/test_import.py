#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx


def test():
    import mongomock_mate

    mongomock_mate.patch_write_concern
    mongomock_mate.patch_collection
    mongomock_mate.patch_database


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
