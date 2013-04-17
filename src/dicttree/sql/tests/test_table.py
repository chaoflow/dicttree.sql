import unittest

from sqlalchemy.exc import OperationalError

from dicttree.sql.tests import mixins

class TestTable(mixins.Sqlite, unittest.TestCase):
    # TODO: define format for entries suitable for easily adding them
    # to sql and usage in tests
    ENTRIES = ['a', 'b']

    def test_contains(self):
        table = self.db['testtable']
        self.assertTrue('1' in table)
        self.assertTrue('2' in table)
        self.assertFalse('3' in table)

    def test_getitem(self):
        table = self.db['testtable']
        self.assertEqual('a', table['1'].name)
        self.assertEqual('b', table['2'].name)
        self.assertRaises(OperationalError, lambda: table['fail'].name)

    def test_len(self):
        self.assertEqual(2, len(self.db['testtable']))

    def test_additem(self):
        pass
        #table = self.db['testtable']
        #table.additem('c')
        #self.assertEqual(3, len(table))

    def test_iterkeys(self):
        keys =  self.db['testtable'].iterkeys()
        self.assertEqual(keys.next(), 1)

    def test_itervalues(self):
        values = self.db['testtable'].itervalues()
        self.assertEqual(values.next(), (1, 'a'))

    def test_iteritems(self):
        items = self.db['testtable'].iteritems()
        item = items.next()
        self.assertEqual(1, item[0])
        self.assertEqual(1, item[1].id)
        self.assertEqual('a', item[1].name)
