import unittest

from dicttree.sql.tests import mixins
from dicttree.sql.tests.mixins import Testtable

import ipdb

class TestSqlite(mixins.Sqlite, unittest.TestCase):
    # TODO: define format for entries suitable for easily adding them
    # to sql and usage in tests
    ENTRIES = ['a', 'b']

    def test_contains(self):
        query = self.session.query(Testtable)
        result =  query.filter(Testtable.name=='a').first()
        self.assertEqual('a', result.name)
        result =  query.filter(Testtable.name=='b').first()
        self.assertEqual('b', result.name)
        result = query.filter(Testtable.name=='fail').first()
        self.assertEqual(None, result)
