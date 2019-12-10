import flask
import pandas as pd
import numpy as np
from flask import Flask, render_template, request,redirect, url_for
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import callbacks
from app import app, server
from layouts import dashboard

@server.route('/')
def index():
    return render_template('home.html')

@server.route('/result', methods = ['POST', 'GET'])
def result():
    #Authentication Logic
    if request.method == 'POST' and request.form['username'] == 'admin' and request.form['pass'] == '123456' :
        print('llego del boton marica')
        print('POST con usuario {} con password {}'.format(request.form['username'],request.form['pass']))
        return redirect(url_for('/dash/'))
    else:
        return 'logged faild, check your credentials...'

app.layout = dashboard

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
