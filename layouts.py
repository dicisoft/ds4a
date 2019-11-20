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
                        html.H2("Air Traffic"),
                        html.P(
                            """\
                            Lorem ipsum dolor sit amet, consectetur adipiscing
                            elit. Phasellus diam quam, pulvinar in pulvinar vel,
                            tristique nec diam. Nam porta diam id risus
                            volutpat, id hendrerit velit iaculis.
                            """
                        ),
                        html.H3("Select Airport:"),
                        html.Div(),
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
                        dbc.Row([
                            html.H6("Integrated by:"),
                            html.Br(),
                        ]),
                        dbc.Row([
                            html.Br(),
                            html.Img(src='../static/images/logo-dici.png'),
                            html.Img(src='../static/images/logo-mintic.png'),
                            html.Img(src='../static/images/logo-c-o.png'),
                            html.Img(src='../static/images/logo-softbank.png')

                        ]),
                   
                    ],
                    md=3,
                        style={"background-color": "#FFFFFF", "height": "100vh", "padding": "3%"},
                ),
                dbc.Col(
                    [
                        dbc.Row([
                            dbc.Col([
                                 html.Img(src='../static/images/plain-icon.png'),
                                dbc.Label("Map"),
                                html.Div(id='map-div')                                
                            ],     
                            md=6),
                            dbc.Col([
                                html.Img(src='../static/images/plain-icon.png'),
                                dbc.Label("Grid"),
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

                            md=6)
                        ]),
                        dbc.Row([
                            dbc.Col([
                                  html.Img(src='../static/images/plain-icon-horizontal.png'),
                                html.Label("Vertical visibility Chart"),
                                dcc.Graph(
                                    figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                                ),
                            ],

                            md=6),
                            dbc.Col([
                                  html.Img(src='../static/images/plain-icon-vertical.png'),
                                html.Label("Horizontalvisibility Chart"),
                                dcc.Graph(
                                    figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                                ),
                            ],

                            md=6)
                        ])
                    ],
                    md=9,
                    style={"background-color": "#F4F4F4", "height": "100%", "padding": "0.5% 0.5%"},
                ),
            ]
        )
    ],
    className="mt-4",
    )

    # 4.4528825,-75.7684869;
