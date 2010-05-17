# -*- coding: utf-8 -
#
# This file is part of gunicorn released under the MIT license. 
# See the NOTICE for more information.

import os
import sys
import traceback

from gunicorn import util
from gunicorn.app.base import Application

class WSGIApplication(Application):
    
    def init(self, parser, opts, args):
        if len(args) != 1:
            parser.error("No application module specified.")

        self.cfg.set("default_proc_name", args[0])
        self.app_uri = args[0]

        sys.path.insert(0, os.getcwd())
        try:
            self.load()
        except:
            print "Failed to import application: %s" % self.app_uri
            traceback.print_exc()
            sys.exit(1)

    def load(self):
        return util.import_app(self.app_uri)