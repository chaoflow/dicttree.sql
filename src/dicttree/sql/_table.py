from dicttree.sql._views import KeysView
from dicttree.sql._views import ItemsView
from dicttree.sql._views import ValuesView

#XXX move views from dicttree.sql
import ipdb

class Table(object):
    def __init__(self, table, session):
        self._table = table
        self.name = table.name
        self.session = session
        self._query = self.session.query(self._table)
        self.prim_keys = self._table.primary_key.columns.keys()

    def __contains__(self, id):
        #XXX define rule by looping over prim_keys and id as list
        # for one prim key we can use get(id)
        filter_rule = self.prim_keys[0] +'='+ id
        result = self._query.filter(filter_rule).first()
        if result is None:
            return False
        return True

    def __getitem__(self, id):
        #XXX define rule by looping over prim_keys and id as list
        # for one prim key we can use get(id)
        filter_rule = self.prim_keys[0] +'='+ id
        return self._query.filter(filter_rule).one()

    def additem(self, columnvalueslist):
        #XXX needs new table object!
        #values = ','.join(map(str, columnvalueslist))
        #Tableobject = self._table.__class__
        #record = Tableobject(values)
        #self.session.add(record)
        #self.session.commit()
        raise NotImplementedError('Not yet')

    def __setitem__(self, id, values):
        raise NotImplementedError('Use additem')

    def __delitem__(self, id):
       raise NotImplementedError()

    def __iter__(self):
        col = self._table.primary_key.columns[self.prim_keys[0]]
        for key in self.session.query(col).all():
            yield key[0]

    def __len__(self):
        return sum(1 for row in iter(self))

    iterkeys = __iter__

    def itervalues(self):
        for row in self._query:
            yield row

    def iteritems(self):
        return ((row.__dict__[self.prim_keys[0]], row)
                for row in ValuesView(self))

    def items(self):
        return ItemsView(dictionary=self)

    def keys(self):
        return KeysView(dictionary=self)

    def values(self):
        return ValuesView(dictionary=self)
