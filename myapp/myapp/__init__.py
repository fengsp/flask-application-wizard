# -*- coding: utf-8 -*-
"""
    myapp
    ~~~~~

    Description of the module goes here...

    :copyright: (c) 2014 by fsp.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask
app = Flask(__name__)
app.config.from_object('myapp.settings')

import myapp.views
from myapp.blue import blue


app.register_blueprint(blue, url_prefix='/blue')
