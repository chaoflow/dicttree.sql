import os
import shutil
import sys
import traceback

import ipdb

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dicttree.sql._database import Database


Base = declarative_base()

class Sqlite(object):
    def setUp(self):
        try:
            self._setUp()
        except Exception, e:
            # XXX: working around nose to get immediate exception
            # output, not collected after all tests are run
            sys.stderr.write("""
======================================================================
Error setting up testcase: %s
----------------------------------------------------------------------
%s
""" % (str(e), traceback.format_exc()))
            self.tearDown()
            raise e

    def _setUp(self):
        self.basedir = '/'.join(['var', self.id()])
        os.mkdir(self.basedir)
        dbpath = self.basedir + '/test.db'

        # create sqlite database in basedir
        # and connection using sqlalchemy
        engine = create_engine('sqlite:///' + dbpath)
                               #, echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

        #add entries defined by test class
        for x in self.ENTRIES:
            self.session.add(Testtable(x))
        self.session.commit()

        self.db = Database(dbpath = dbpath)

    def tearDown(self):
        successful = sys.exc_info() == (None, None, None)
        if successful or not os.environ['KEEP_FAILED']:
            shutil.rmtree(self.basedir)

class Testtable(Base):

    __tablename__ = "testtable"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
