#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytest
from pytest import raises, approx
import mongomock_mate
from mongoengine import Document, fields, connect
from pathlib_mate import Path


def test_crud():
    dbname = "test_crud"
    client = connect(db=dbname, host="mongomock://localhost", alias=dbname)

    class User(Document):
        _id = fields.IntField(primary_key=True)
        name = fields.StringField()

        meta = {"db_alias": dbname, "collection": "user"}

    User.objects.insert(User(id=1, name="Alice"))
    User.objects.insert([User(id=2, name="Bob"), User(id=3, name="Cathy")])

    user = User.objects(_id=1).get()
    user.name = "Adam"
    user.save()

    assert User.objects(_id=1).get().name == "Adam"


def test_io():
    # dump
    dbname = "test_dump"
    client = connect(db=dbname, host="mongomock://localhost", alias=dbname)
    db = client[dbname]

    class User(Document):
        _id = fields.IntField(primary_key=True)
        name = fields.StringField()

        meta = {"db_alias": dbname, "collection": "user"}

    User.objects.insert([
        User(id=1, name="Alice"),
        User(id=2, name="Bob"),
        User(id=3, name="Cathy"),
    ])

    db_file = Path(__file__).change(new_basename="%s.json" % dbname).abspath

    db.dump_db(db_file, pretty=True, overwrite=True, verbose=False)

    # load
    dbname = "test_load"
    client = connect(db=dbname, host="mongomock://localhost", alias=dbname)
    db = client[dbname]

    class User(Document):
        _id = fields.IntField(primary_key=True)
        name = fields.StringField()

        meta = {"db_alias": dbname, "collection": "user"}

    db.load_db(db_file, check_dbname=False, verbose=False)
    assert len(list(db.user.find())) == 3

    try:
        os.remove(db_file)
    except:
        pass


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
