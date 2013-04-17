import unittest

from sqlalchemy import schema
from sqlalchemy import  Column, Integer, String

from dicttree.sql.tests import mixins
from dicttree.sql._table import Table

class TestDatabase(mixins.Sqlite, unittest.TestCase):
    # TODO: define format for entries suitable for easily adding them
    # to sql and usage in tests
    ENTRIES = ['a', 'b']

    def test_contains(self):
        self.assertTrue('testtable' in self.db)

    def test_getitem(self):
        table = self.db['testtable']
        self.assertEqual('testtable', table.name)

    def test_len(self):
        self.assertEqual(1, len(self.db))

    def test_delitem(self):
        del self.db['testtable']
        self.assertEqual(0, len(self.db))

    def test_iterkeys(self):
        tablename = iter(self.db).next()
        self.assertEqual('testtable', tablename)

    def test_itervalues(self):
        values = self.db.itervalues()
        self.assertEqual(values.next().name, 'testtable')

    def test_iteritems(self):
        items = self.db.iteritems()
        item = items.next()
        self.assertEqual('testtable', item[0])
        self.assertEqual('testtable', item[1].name)
