#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
from flask import Flask, render_template, request
from flask import render_template
from flask import Flask
from flask import Response
app = Flask(__name__)
form = cgi.FieldStorage()
from DDLj import genddl
@app.route('/')
def nthome():
    return render_template('index.html')
@app.route('/getfile', methods=['POST', 'GET'])
def getfile():
    if request.method == 'POST':
        jsonschema=request.form['Schempath']
        gloss=request.form['Gloss']
        domain=request.form['domain']
        sqlpath='C:/'
        try:
            f=genddl(jsonschema,domain,gloss,sqlpath)
        except Exception as e:
            print(e)
    return Response(f,mimetype='application/json',headers={'Content-Disposition':'attachment;filename='+domain+'.sql'})
if __name__ == '__main__':
    app.run(debug=True)