import os
import sqlalchemy
import shutil
import sys
import traceback


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

        # TODO: create sqlite database in basedir

        # TODO: create sql connection to sqlite database using sqlalchemy

        # TODO: add entries defined by test class

    def tearDown(self):
        successful = sys.exc_info() == (None, None, None)
        if successful or not os.environ['KEEP_FAILED']:
            shutil.rmtree(self.basedir)
