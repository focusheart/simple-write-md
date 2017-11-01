# -*- coding: utf8 -*-

from flask import Flask
from flask import render_template
import os
from ConfigParser import ConfigParser

config = ConfigParser()
config.read('config.ini')

DOC_ROOT = config.get('doc', 'root')

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/edit')
def edit():
    return 'edit'

@app.route('/save', methods=['GET', 'POST'])
def save():
    return 'save'

if __name__ == '__main__':
    app.run()
