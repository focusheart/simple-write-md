# -*- coding: utf8 -*-
'''
Simple Write MD Server Program

Provide list, query, edit, save, etc

'''

import os
from ConfigParser import ConfigParser
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import abort

config = ConfigParser()
config.read('config.ini')

DOC_ROOT = config.get('doc', 'root')

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Index page of this tiny site
    '''
    return render_template('index.html')

@app.route('/list')
def list_files():
    '''
    List files in specified path
    '''
    path = request.args.get('p')
    if path is None or path.strip() == '':
        return abort(404)

    # get file list here

    return render_template('list.html')

@app.route('/edit')
def edit():
    '''
    Edit specified file
    '''
    return render_template('edit.html')

@app.route('/save', methods=['GET', 'POST'])
def save():
    '''
    Save submitted md content
    '''
    # Handle the save file operation
    ret = {'success': True}
    return jsonify(ret)

if __name__ == '__main__':
    app.run()
