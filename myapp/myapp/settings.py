# -*- coding: utf-8 -*-
"""
    myapp.settings
    ~~~~~~~~~~~~~~

    Settings.

    :copyright: (c) 2014 by fsp.
    :license: BSD, see LICENSE for more details.
"""
import os


DEBUG = False
# Detect environment by whether debug named file exists or not
if os.path.exists(os.path.join(os.path.dirname(__file__), 'debug')):
    DEBUG = True


if DEBUG:
    pass
else:
    pass
