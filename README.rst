.. image:: https://travis-ci.org/MacHu-GWU/mongomock_mate-project.svg?branch=master
    :target: https://travis-ci.org/MacHu-GWU/mongomock_mate-project?branch=master

.. image:: https://codecov.io/gh/MacHu-GWU/mongomock_mate-project/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/MacHu-GWU/mongomock_mate-project

.. image:: https://img.shields.io/pypi/v/mongomock_mate.svg
    :target: https://pypi.python.org/pypi/mongomock_mate

.. image:: https://img.shields.io/pypi/l/mongomock_mate.svg
    :target: https://pypi.python.org/pypi/mongomock_mate

.. image:: https://img.shields.io/pypi/pyversions/mongomock_mate.svg
    :target: https://pypi.python.org/pypi/mongomock_mate

.. image:: https://img.shields.io/badge/Star_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/mongomock_mate-project


Welcome to ``mongomock_mate`` Documentation
==============================================================================

**Use** ``mongomock_mate``:

Just import ``mongomock_mate`` at begin of your script. It use monkey patch:

.. code-block:: python

    import mongomock_mate


**Features**:

**Data Persistence: dump and load data**

.. code-block:: python

    import mongomock_mate

    # dump
    db = client["test"]
    c_user = db["user"]

    c_user.insert([{"_id": 1, "name": "Alice"}, {"_id": 2, "name": "Bob"}])

    db.dump_db("test.json")

    # load
    db = client["test"]
    db.load_db("test.json")

    # other params
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

    def load_db(self, file, check_dbname=True, verbose=True):
        """
        Load :class:`mongomock.database.Database` from a local file.

        :param file: file path.
        :param check_dbname: bool, if True, the dbname has to be matched.
        :param verbose: bool, toggle on log.
        """
    
    
**Working with mongoengine ORM:**

2018-07-30:

At mongomock==3.10.0, insert operation doesn't work with latest mongoengine==0.15.3, because the implementation of ``WriteConcern`` is not correct in mongomock.

`Github Issue <https://github.com/mongomock/mongomock/issues/406>`_.

.. code-block:: python

    import mongomock_mate
    from mongoengine import connect, Document, fields

    connect('mongoenginetest', host='mongomock://localhost')

    class User(Document):
        _id = fields.IntField(primary_key=True)
        name = fields.StringField()

    User.objects.insert(User(_id=1, name="Alice"))


Quick Links
------------------------------------------------------------------------------
- .. image:: https://img.shields.io/badge/Link-Document-red.svg
      :target: https://mongomock_mate.readthedocs.io/index.html

- .. image:: https://img.shields.io/badge/Link-API_Reference_and_Source_Code-red.svg
      :target: https://mongomock_mate.readthedocs.io/py-modindex.html

- .. image:: https://img.shields.io/badge/Link-Install-red.svg
      :target: `install`_

- .. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
      :target: https://github.com/MacHu-GWU/mongomock_mate-project

- .. image:: https://img.shields.io/badge/Link-Submit_Issue_and_Feature_Request-blue.svg
      :target: https://github.com/MacHu-GWU/mongomock_mate-project/issues

- .. image:: https://img.shields.io/badge/Link-Download-blue.svg
      :target: https://pypi.python.org/pypi/mongomock_mate#downloads


.. _install:

Install
------------------------------------------------------------------------------

``mongomock_mate`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install mongomock_mate

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade mongomock_mate