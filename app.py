import dash
import flask
from flask import Flask

import dash_bootstrap_components as dbc 

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server, 
                routes_pathname_prefix='/dash/', 
                external_stylesheets=[dbc.themes.BOOTSTRAP,'../static/css/styles-login.css'])

app.config.suppress_callback_exceptions = True