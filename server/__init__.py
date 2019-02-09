# -*- coding: utf-8 -*-

__version__ = '0.1'

from flask import Flask
from CiaShopServer.server.application import *

app = Flask('CiaShopAPI')
app.config['SECRET_KEY'] = 'random'