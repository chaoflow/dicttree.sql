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
        #filterrule = ''
        #for columnname in self.prim_keys:
        #    filter_rule = self.prim_keys[0] +'='+ id +','
        #filter_rule = filter_rule[:-1]

        filter_rule = self.prim_keys[0] +'='+ id
        result = self._query.filter(filter_rule).first()
        if result is None:
            return False
        return True

    def __getitem__(self, id):
        #XXX define rule by looping over prim_keys and id as list
        filter_rule = self.prim_keys[0] +'='+ id
        return self._query.filter(filter_rule).one()

    def __setitem__(self, id, values):
        pass

    def __delitem__(self, id):
        #XXX self.session.delete(obj1) requires whole object,
        # i.e. Testtable(id=3, name='c')
        #XXX delete over query does not delete cascade and orphans!!!
        #it also does not allow text filter
        #as it removes the entries from session

    def __iter__(self):
        pass

    def __len__(self):
        return sum(1 for row in iter(self))

    iterkeys = __iter__

    def itervalues(self):
        pass

    def iteritems(self):
        pass

    def items(self):
        return ItemsView(dictionary=self)

    def keys(self):
        return KeysView(dictionary=self)

    def values(self):
        return ValuesView(dictionary=self)
