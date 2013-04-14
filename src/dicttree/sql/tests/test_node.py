import unittest

from dicttree.sql.tests import mixins

class TestNode(mixins.Sqlite, unittest.TestCase):
    pass
