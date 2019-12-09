import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import dash_table as dt
import pandas as pd
from app import app

PAGE_SIZE = 11

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df_table = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)
df_table['index'] = range(1, len(df_table) + 1)



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
                    
                    md=3,
                        style={"background-color": "#FFFFFF", "height": "100vh", "padding": "3%"},
                ),
                dbc.Col(
                    [
                       
                            dbc.Col([
                                
                                
                                html.H6("Map"),
                                  dbc.Select(
                            id="airport-select",
                            options=[
                                {"label": "Armenia", "value": "SKAR"},#Armenia
                                {"label": "Mariquita", "value": "SKQU"},#Mariquita
                                {"label": "Bogota", "value": "SKBO"},#Bogota
                                {"label": "Bucaramanga", "value": "SKBG"},#Bucaramanga
                                {"label": "Cali", "value": "SKCL"},#Cali
                                {"label": "Cucuta", "value": "SKCC"},#Cucuta
                                {"label": "Cartagena", "value": "SKCG"},#cartagena
                                {"label": "Pereira", "value": "SKPE"},#pereira
                                {"label": "San Andres", "value": "SKSP"},#San Andres
                                {"label": "Santa Marta", "value": "SKSM"},#Santa Marta
                                {"label": "Monteria", "value": "SKMR"},#Monteria
                            ],
                            value='SKAR'),
                                     html.Br(),
                                html.Br(),
                                html.Div(id='map-div')                                
                            ],     
                            md=12),
                            dbc.Col([
                                html.H6("Grid"),
                                dt.DataTable(
                                    id='datatable-paging',
                                    columns=[
                                        {"name": i, "id": i} for i in sorted(df.columns)
                                    ],
                                    page_current=0,
                                    page_size=PAGE_SIZE,
                                    page_action='custom'
                                )
                            ],
                            md=12)
                    ],
                    md=4,
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
),      html.Br(), 
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
) ,
                                html.Br(),         
                            ],
                            md=12), 
                            
                      dbc.Col([
                                html.H6("Vertical visibility Chart"),
                                dcc.Graph(
                                    figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                                ),
                            ],

                            md=12),
              
                           
                            dbc.Col([
                                html.H6("Horizontalvisibility Chart"),
                                dcc.Graph(
                                    figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                                ),
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