from server import app
from flask import render_template, request

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/consumerApiCiaShop')
def printer():
    return render_template('index.html')