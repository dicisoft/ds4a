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
                        html.Img(src='../static/images/plain-icon.png'),
                        html.H1("Horizontal & Vertical"),
                        html.Strong("visibility"),
                        html.Br(),
                        html.H2("Air Traffic:"),
                        html.P(
                            """\
                            Lorem ipsum dolor sit amet, consectetur adipiscing
                            elit. Phasellus diam quam, pulvinar in pulvinar vel,
                            tristique nec diam. Nam porta diam id risus
                            volutpat, id hendrerit velit iaculis.
                            """
                        ),
                         html.Button('Documentation', className='button-dash'),
                        html.H3("Select Airport:"),
                        html.Div(),
                  
                        dbc.Row([
                            html.Br(),
                            html.Br(),
                            html.H6("Integrated by:"),
                            html.Br(),
                       
                        ]),
                        dbc.Row([
                            html.Br(),
                            html.Img(src='../static/images/logo-dici.png'),
                            html.Img(src='../static/images/logo-mintic.png'),
                            html.Img(src='../static/images/logo-c-o.png',),
                            html.Br(),


                        ]),
                   dbc.Row([
                           html.Img(src='../static/images/softbank-logo.svg', className='images_logo')
                        ]),
                   
                    ],
                    
                    md=2,
                        style={"background-color": "#FFFFFF", "height": "100vh", "padding": "3%"},
                ),
                dbc.Col(
                    [
                       
                            dbc.Col([

                                html.H6("Map"),
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
                    md=5,
                    style={"background-color": "#F4F4F4", "height": "100vh", "padding": "0.% 0",  "overflow": "scroll"},
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
                                            {'label': '+ 01', 'value': 'v1'},
                                            {'label': '+ 02', 'value': 'v2'},
                                            {'label': '+ 03', 'value': 'v3'},
                                            {'label': '+ 04', 'value': 'v4'},
                                            {'label': '+ 05', 'value': 'v5'},
                                            {'label': '+ 06', 'value': 'v6'}
                                        ],
                                        value=['v1', 'v2', 'v3', 'v4', 'v5', 'v6'],
                                        labelStyle={'display': 'inline-block',}
                                ),      
                                html.Br(), 
                                html.H6("Horizontal Visibility"),
                             dcc.Checklist(
                                    options=[
                                        {'label': '+ 01', 'value': 'h1'},
                                        {'label': '+ 02', 'value': 'h2'},
                                        {'label': '+ 03', 'value': 'h3'},
                                        {'label': '+ 04', 'value': 'h4'},
                                        {'label': '+ 05', 'value': 'h5'},
                                        {'label': '+ 06', 'value': 'h6'}
                                    ],
                                    value=['h1', 'h2', 'h3', 'h4', 'h5', 'h6'],
                                    labelStyle={'display': 'inline-block'}
                                ),
                            html.Br(),         
                            ],
                            md=12), 
                            
                            dbc.Col([
                                html.H6("Vertical visibility Chart"),
                                dcc.Graph(id="vertical-vis-plot"),
                            ],
                            md=12),                                         
                            dbc.Col([
                                html.H6("Horizontalvisibility Chart"),
                                dcc.Graph(id="horizontal-vis-plot"),
                            ],
                            md=12),
                    ],       
                    md=5,
                    style={"background-color": "#F4F4F4", "height": "100vh", "overflow": "scroll" },
                ),        
            ]  
        )   
    ],
    className="mt-4",
      style={"background-color": "#F4F4F4", "height": "100%", "padding": "0.5% 0.5%",},
    )