# -*- coding: utf-8 -*-

__version__ = '0.1'

from CiaShopServer import app

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)