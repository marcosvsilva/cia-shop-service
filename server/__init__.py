# -*- coding: utf-8 -*-

__version__ = '0.1'

from flask import Flask

app = Flask('CiaShopAPI')
app.config['SECRET_KEY'] = 'random'

import CiaShopServer.server.controller
import CiaShopServer.server.model
import CiaShopServer.server.service
import CiaShopServer.server.application
