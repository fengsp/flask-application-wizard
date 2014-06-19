# -*- coding: utf-8 -*-
"""
    myapp.views
    ~~~~~~~~~~~

    Register your actions.

    :copyright: (c) 2014 by fsp.
    :license: BSD, see LICENSE for more details.
"""
from myapp import app


@app.route('/')
def index():
    return 'Hello, app!'
