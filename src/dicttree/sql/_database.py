from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData

from dicttree.sql._views import KeysView
from dicttree.sql._views import ItemsView
from dicttree.sql._views import ValuesView
#XXX move views from dicttree.sql

from dicttree.sql._table import Table

class Database(object):
    def __init__(self, *args, **kw):
        self.engine = create_engine(*args, **kw)
        self.metadata = MetaData(bind=self.engine)
        self.metadata.reflect(bind=self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def __contains__(self, tablename):
        return tablename in self.metadata.tables.keys()

    def __getitem__(self, tablename):
        return Table(self.metadata.tables[tablename], self.session)

    def __setitem__(self, dn, node):
        raise NotImplementedError()

    def __delitem__(self, tablename):
        table = self[tablename]
        table._table.drop(self.engine)
        self.metadata.remove(table._table)

    def __iter__(self):
        for tablename in self.metadata.tables:
            yield tablename

    def __len__(self):
        return sum(1 for table in iter(self))

    iterkeys = __iter__

    def itervalues(self):
        for table in self.metadata.tables.values():
            yield Table(table, self.session)

    def iteritems(self):
        return ((table.name, table) for table in ValuesView(self))

    def items(self):
        return ItemsView(dictionary=self)

    def keys(self):
        return KeysView(dictionary=self)

    def values(self):
        return ValuesView(dictionary=self)
