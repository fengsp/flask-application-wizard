# -*- coding: utf-8 -*-
"""
    myapp.blue
    ~~~~~~~~~~

    Description of the blueprint goes here...

    :copyright: (c) 2014 by fsp.
    :license: BSD, see LICENSE for more details.
"""
from flask import Blueprint
blue = Blueprint('blue', __name__)


@blue.route('/')
def index():
    return 'Hello, blue!'
