import unittest

from sqlalchemy.exc import OperationalError

from dicttree.sql.tests import mixins

import ipdb

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

    def test_setitem(self):
        pass
        #table = self.db['testtable']
        #table['3'] = 'c'
        #self.assertEqual('c', table['3'].name)

    def test_delitem(self):
        table = self.db['testtable']
        self.assertEqual('b', table['2'].name)
        del table['2']
        self.assertRaises(OpertationalError, lambda: table['b'].name)
