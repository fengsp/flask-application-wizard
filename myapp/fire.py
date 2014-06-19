# -*- coding: utf-8 -*-
"""
    fire
    ~~~~

    Fire your app up.

    :copyright: (c) 2014 by fsp.
    :license: BSD, see LICENSE for more details.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
reload(sys)
sys.setdefaultencoding('utf-8')

from myapp import app


if __name__ == "__main__":
    app.run()
