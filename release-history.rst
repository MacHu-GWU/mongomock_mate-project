Release and Version History
==============================================================================


0.0.2 (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.0.1 (2018-07-30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First release

**Features and Improvements**

- Fixed issue that mongomock not working with mongoengine in insert. Implement the dummy ``WriteConcern`` class, and fix the ``collection.Collection.write_concern`` method.
- Add data persistence function, so you can use mongomock as a fake in-memory mongodb.

**Miscellaneous**

Compatible with:

- pymongo==3.7.1
- mongoengine==0.15.3
- mongomock==3.10.0