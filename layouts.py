import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import dash_table as dt
import pandas as pd
from app import app
from constants import air_names, vars_list, vars_list_dt
from db_connector import get_data

PAGE_SIZE = 11

df = get_data()
df['station_name'] = df['station'].map(air_names)

dashboard = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Img(src='../static/images/plain-icon.png', className='inline-header'),
                        html.H1("Horizontal & Vertical  " , className='inline-header'),
                        html.Strong("  Visibility", className='inline-header'),
                   dbc.Row([
                        ]),
                   
                    ],
                    
                 
                        style={"background-color": "#FFFFFF", "height": "70px", "position": "fixed" , "z-index": "99999" },
                ),
                dbc.Col(
                    [
                       
                            dbc.Col([

                                html.H6("Map"),
                                html.Br(),
                                html.Button('Documentation', className='button-dash'),
                                html.Br(),
                                html.Br(),
                                dcc.Dropdown(id='select-airport',
                                options=[{'label':label,'value':val} for label, val in zip(df['station_name'].unique(),df['station'].unique())],
                                value='SKBO'),
                                     html.Br(),
                                html.Div(id='map-div')                                
                            ],     
                            md=12),
                            dbc.Col([
                                html.H6("Grid"),
                                dt.DataTable(
                                    id='table',
                                    columns=vars_list_dt,
                                    data=df.to_dict('records'),
                                    style_cell={'width': '50px'},
                                    style_table={
                                            'maxHeight': '450px',
                                            'overflowY': 'scroll'
                                        }
                                )
                            ],
                            md=12)
                    ],
                    md=6,
                    style={"background-color": "#F4F4F4", "height": "100vh", "padding": "0.% 0",  "overflow": "scroll" ,  "top": "70px"},
                ),
                 dbc.Col(
                    [
                            dbc.Col([
                                html.H6("Visibility Chart"),
                                html.Br(),
                                html.Button('Proyection', className='button-dash'),
                                html.Br(),
                                     html.H6("Vertical visibility"),
                                dcc.Checklist(
                                        options=[
                                            {'label': '✈', 'value': 'v1'},
                                            {'label': '✈', 'value': 'v2'},
                                            {'label': '✈', 'value': 'v3'},
                                            {'label': '✈', 'value': 'v4'},
                                            {'label': '✈', 'value': 'v5'},
                                            {'label': '✈', 'value': 'v6'}
                                        ],
                                        value=['v1', 'v2', 'v3', 'v4', 'v5', 'v6'],
                                        labelStyle={'display': 'inline-block',}
                                ),      
                                html.Br(), 
                                html.H6("Horizontal Visibility"),
                             dcc.Checklist(
                                    options=[
                                        {'label': '✈', 'value': 'h1'},
                                        {'label': '✈', 'value': 'h2'},
                                        {'label': '✈', 'value': 'h3'},
                                        {'label': '✈', 'value': 'h4'},
                                        {'label': '✈', 'value': 'h5'},
                                        {'label': '✈', 'value': 'h6'}
                                    ],
                                    value=['h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
                                    labelStyle={'display': 'inline-block'}
                                       
                                ),
                            html.Br(), 
                             html.Br(),         
                            ],
                            md=12), 
                            
                            dbc.Col([
                                html.H6("Vertical visibility Chart"),
                                dcc.Graph(id="vertical-vis-plot"),
                            ],
                            md=12),                                         
                            dbc.Col([
                                html.H6("Horizontal visibility Chart"),
                                dcc.Graph(id="horizontal-vis-plot"),
                            ],
                            md=12),
                            dbc.Col([
                                 html.Img(src='../static/images/logo-dici.png'),
                                  html.Img(src='../static/images/logo-mintic.png'),
                                  html.Img(src='../static/images/logo-c-o.png'),
                                  html.Img(src='./static/images/logo-softbank.png'),
                            ],
                            md=12),
                            
                    ],       
                    md=6,
                    style={"background-color": "#F4F4F4", "height": "100vh", "padding": "0.% 0",  "overflow": "scroll" ,  "top": "70px"},
                ),        
            ]  
        )   
    ],
    className="mt-4",
      style={"background-color": "#F4F4F4", "height": "100%", "padding": "0.5%"},
    )