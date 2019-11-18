import dash
import flask
from flask import Flask, render_template, request,redirect, url_for
import dash_core_components as dcc
import dash_html_components as html

server = flask.Flask(__name__)

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
    
    

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/'
)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    
    
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)  