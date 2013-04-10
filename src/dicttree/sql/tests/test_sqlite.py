import unittest

from dicttree.sql.tests import mixins


# probably better split up into different files.

class TestSqlite(mixins.Sqlite, unittest.TestCase):
    # TODO: define format for entries suitable for easily adding them
    # to sql and usage in tests
    ENTRIES = []

    def test_contains(self):
        pass

class TestDatabase(mixins.Sqlite, unittest.TestCase):
    # TODO: define format for entries suitable for easily adding them
    # to sql and usage in tests
    ENTRIES = []

    def test_contains(self):
        pass

class TestTable(mixins.Sqlite, unittest.TestCase):
    pass


class TestNode():
    pass
