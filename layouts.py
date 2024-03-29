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
                        html.Img(src='../static/images/plain-icon-invert.png', className='inline-header'),
                        html.Strong("  VEMCA:", className='inline-header'),
                        html.H1("Visibility Estimation Model in Colombian Airports  " , className='inline-header'),
                       
                   dbc.Row([
                        ]),
                   
                    ],
                    
                 
                        style={"background-color": "#6B69A6", "height": "70px", "position": "fixed" , "z-index": "99999" , "top": "0" },
                ),
                dbc.Col(
                    [
                       
                            dbc.Col([

                                html.H6("Airport"),
                                html.Br(),
                                dcc.Dropdown(id='select-airport',
                                options=[{'label':label,'value':val} for label, val in zip(df['station_name'].unique(),df['station'].unique())],
                                value='SKBO'),
                                     html.Br(),
                                html.Div(id='map-div')                                
                            ],     
                            md=12),
                                dbc.Col([
                                html.H6("Horizontal visibility Chart"),
                                dcc.Graph(id="horizontal-vis-plot"),
                                html.Br(),
                            ],
                            md=12),
                    ],
                    md=6,
                    style={"background-color": "#F4F4F4", "height": "100%", "padding": "0", "top": "70px"},
                ),
                 dbc.Col(
                    [
                            dbc.Col([
                                html.H6("Options and Insights"),
                                html.Br(),
                                html.Button('Exploratory Data Analysis', className='button-dash-invert', id="btnDescriptive"),
                                html.Br(),
                                html.Button('Forecast', id='btnProyection', className='button-dash'),
                                html.Br(),                                
                                html.H6("Vertical visibility (feet), (Prediction for the next 6 hours)"),
                                
                      dbc.Col([
                                dcc.Checklist(id='checklist-vertical1',
                                        options=[
                                            {'label': '+1 Hour ', 'value': 'v1'}                                            
                                        ],
                                        value=['v1'],
                                        labelStyle={'display': 'inline-block',}
                                ),
                                dcc.Checklist(id='checklist-vertical2',
                                        options=[                                            
                                            {'label': '+2 Hour', 'value': 'v2'}                                            
                                        ],
                                        value=['v2'],
                                        labelStyle={'display': 'inline-block',}
                                ),
                                dcc.Checklist(id='checklist-vertical3',
                                        options=[                                            
                                            {'label': '+3 Hour', 'value': 'v3'}
                                        ],
                                        value=['v3'],
                                        labelStyle={'display': 'inline-block',}
                                ),
                                dcc.Checklist(id='checklist-vertical4',
                                        options=[                                            
                                            {'label': '+4 Hour ', 'value': 'v4'}                                            
                                        ],
                                        value=['v4'],
                                        labelStyle={'display': 'inline-block',}
                                ),
                                dcc.Checklist(id='checklist-vertical5',
                                        options=[                                            
                                            {'label': '+5 Hour', 'value': 'v5'}                                            
                                        ],
                                        value=['v5'],
                                        labelStyle={'display': 'inline-block',}
                                ),
                                dcc.Checklist(id='checklist-vertical6',
                                        options=[                                            
                                            {'label': '+6 Hour', 'value': 'v6'}
                                        ],
                                        value=['v6'],
                                        labelStyle={'display': 'inline-block'}
                                        
                           ),
                           ],
               
                            style={ "display": "flex" ,"justify-content" : "center", "padding" : "2%" },
                            
                            ),   
                                html.Br(), 
                                html.H6("Horizontal visibility (miles), (Prediction for the next 6 hours)"),
                                
                                        dbc.Col([
                                dcc.Checklist(id='checklist-horizontal1',
                                        options=[
                                            {'label': '+1 Hour', 'value': 'h1'}                                            
                                        ],
                                        value=['h1'],
                                        labelStyle={'display': 'inline-block',}
                                ),
                                dcc.Checklist(id='checklist-horizontal2',
                                        options=[                                            
                                            {'label': '+2 Hour', 'value': 'h2'}                                            
                                        ],
                                        value=['h2'],
                                        labelStyle={'display': 'inline-block',}
                                ),
                                dcc.Checklist(id='checklist-horizontal3',
                                        options=[                                            
                                            {'label': '+3 Hour', 'value': 'h3'}
                                        ],
                                        value=['h3'],
                                        labelStyle={'display': 'inline-block',}
                                ),
                                dcc.Checklist(id='checklist-horizontal4',
                                        options=[                                            
                                            {'label': '+4 Hour', 'value': 'h4'}                                            
                                        ],
                                        value=['h4'],
                                        labelStyle={'display': 'inline-block',}
                                ),
                                dcc.Checklist(id='checklist-horizontal5',
                                        options=[                                            
                                            {'label': '+5 Hour', 'value': 'h5'}                                            
                                        ],
                                        value=['h5'],
                                        labelStyle={'display': 'inline-block',}
                                ),
                                dcc.Checklist(id='checklist-horizontal6',
                                        options=[                                            
                                            {'label': '+6 Hour', 'value': 'h6'}
                                        ],
                                        value=['h6'],
                                        labelStyle={'display': 'inline-block',}
                                          ),
                           ],
               
                            style={ "display": "flex" ,"justify-content" : "center" , "padding" : "2%" },
                                ),
                                
                                
                            html.Br(),
                            html.Br(),
                            ],
                            md=12),                             
                            dbc.Col([
                                html.H6("Vertical visibility Chart"),
                                dcc.Graph(id="vertical-vis-plot"),
                                html.Br(),
                            ],
                            md=12),
                    ],       
                    md=6,
                    style={"background-color": "#F4F4F4", "padding": "0",  "top": "70px", "height": "100%",  "display": "inline-block" },
                ),        
            ]  
        ),
         dbc.Col([
                                html.H6("Table"),
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
                            md=12),
                                 dbc.Col([
                                 html.Br(),
                                 html.Img(src='../static/images/logo-dici.png'),
                                  html.Img(src='../static/images/logo-mintic.png'),
                                  html.Img(src='../static/images/logo-c-o.png'),
                                  html.Img(src='../static/images/logo-softbank.png'),
                                  html.Br(),
                                  html.Br(),
                            ],
                             ),
          
    ],
    
    className="mt-4",
      style={"background-color": "#F4F4F4", "height": "100%", "padding": "0.5%"},
    )