import dash_core_components as dcc
import dash_html_components as html
import flask
import callbacks

from dash.dependencies import Input, Output
from app import app
from layouts import dashboard, login_layout, url_bar_and_content_div


def serve_layout():
    if flask.has_request_context():
        return url_bar_and_content_div   
    return html.Div([
        url_bar_and_content_div,
        login_layout,
        dashboard        
    ])

app.layout = serve_layout

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):    
    if pathname == '/dashboard':
         return dashboard         
    elif pathname == '/':
        return login_layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
