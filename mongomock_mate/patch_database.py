#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
monkey patch ``mongomock.database``
"""

from superjson import json
from mongomock.database import Database

from .sixmini import iteritems


def _dump(db):
    """
    Dump :class:`mongomock.database.Database` to dict data.
    """
    db_data = {"name": db.name, "_collections": dict()}
    for col_name, collection in iteritems(db._collections):
        if col_name != "system.indexes":
            col_data = {
                "_documents": collection._documents,
                "_uniques": collection._uniques,
            }
            db_data["_collections"][col_name] = col_data

    return db_data


def _load(db_data, db, check_dbname=True):
    """
    Load dict data and fill into class:`mongomock.database.Database`.
    Old data will be replaced.

    :param db_data: dict.
    :param db: :class:`mongomock.database.Database` instance.
    :param check_dbname: bool, if True, the dbname has to be matched.
    """
    if check_dbname:  # pragma: no cover
        if db.name != db_data["name"]:
            raise ValueError(
                "dbname doesn't matches! Maybe wrong database data.")

    db.__init__(client=db._client, name=db.name)
    for col_name, col_data in iteritems(db_data["_collections"]):
        collection = db.get_collection(col_name)
        collection._documents = col_data["_documents"]
        collection._uniques = col_data["_uniques"]
        db._collections[col_name] = collection

    return db


def dump_db(self, file,
            pretty=False,
            overwrite=False,
            verbose=True):
    """
    Dump :class:`mongomock.database.Database` to a local file. Only support
    ``*.json`` or ``*.gz`` (compressed json file)

    :param file: file path.
    :param pretty: bool, toggle on jsonize into pretty format.
    :param overwrite: bool, allow overwrite to existing file.
    :param verbose: bool, toggle on log.
    """
    db_data = _dump(self)
    json.dump(
        db_data, file,
        pretty=pretty, overwrite=overwrite, verbose=verbose,
    )


def load_db(self, file, check_dbname=True, verbose=True):
    """
    Load :class:`mongomock.database.Database` from a local file.

    :param file: file path.
    :param check_dbname: bool, if True, the dbname has to be matched.
    :param verbose: bool, toggle on log.
    """
    db_data = json.load(file, verbose=verbose)
    return _load(db_data, self, check_dbname=check_dbname)


Database.dump_db = dump_db
Database.load_db = load_db
