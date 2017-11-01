# -*- coding: utf8 -*-
'''
Simple Write MD Server Program

Provide list, query, edit, save, etc

'''

import os
import codecs
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import abort

app = Flask(__name__)
app.config.from_object('config')

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
    if path is None:
        path = ''
    path = path.strip()

    # security check

    # get file list here
    files = os.listdir(os.path.join(app.config['DOC_ROOT'], path))
    
    return render_template('list.html', files=files)

@app.route('/edit')
def edit():
    '''
    Edit specified file
    '''
    act = request.args.get('a')
    fn = request.args.get('f')

    if act is None: abort(404)
    if fn is None: abort(404)

    fn = fn.strip()
    # security check

    # edit now
    if act == 'new':
        ctt = ''
    else:
        ctt = open(os.path.join(app.config['DOC_ROOT'], fn))

    return render_template('edit.html', fn=fn, ctt=ctt)

@app.route('/save', methods=['GET', 'POST'])
def save():
    '''
    Save submitted md content
    '''
    if request.method == 'GET':
        return 'save'

    fn = request.form.get('f')
    ctt = request.form.get('c')

    full_fn = os.path.join(app.config['DOC_ROOT'], fn)

    codecs.open(full_fn, 'w', 'utf-8').write(ctt)

    # Handle the save file operation
    ret = {'success': True}
    return jsonify(ret)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=51101)
