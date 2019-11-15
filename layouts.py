import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import dash_table as dt
import pandas as pd
from app import app

PAGE_SIZE = 5

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df_table = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)
df_table['index'] = range(1, len(df_table) + 1)

fig = go.Figure(data=go.Scattergeo(
        locationmode = 'USA-states',
        lon = df['long'],
        lat = df['lat'],
        text = df['text'],
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'Blues',
            cmin = 0,
            color = df['cnt'],
            cmax = df['cnt'].max(),
            colorbar_title="Incoming flights<br>February 2011"
        )))

fig.update_layout(
        title = 'Most trafficked US airports<br>(Hover for airport names)',
        geo = dict(
            scope='usa',
            projection_type='albers usa',
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )

body = html.Div(
    [        
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Img(src=app.get_asset_url('data-analytics.png')),
                        html.H2("Tráfico Aéreo"),
                        html.P(
                            """\
                            Lorem ipsum dolor sit amet, consectetur adipiscing
                            elit. Phasellus diam quam, pulvinar in pulvinar vel,
                            tristique nec diam. Nam porta diam id risus
                            volutpat, id hendrerit velit iaculis.
                            """
                        ),
                        dbc.Label("Aeropuerto 01"),
                        dbc.Select(
                            id="select",
                            options=[
                                {"label": "Airport 1", "value": "1"},
                                {"label": "Airport 2", "value": "2"},
                                {"label": "Airport 3", "value": "3"},
                            ]),                        
                        dbc.Row([
                            dbc.Label("Integrated by:"),
                        ]),
                        dbc.Row([
                            html.Img(src=app.get_asset_url('integrated-dicisfot.png')),
                        ]),                        
                    ],
                    md=3,
                ),
                dbc.Col(
                    [
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Mapa"),
                                dcc.Graph(id='graph', figure=fig)                                
                            ],
                            md=6),
                            dbc.Col([
                                dbc.Label("Tabla"),
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
                                html.H2("Graph"),
                                dcc.Graph(
                                    figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                                ),                                
                            ],
                            md=6),
                            dbc.Col([
                                html.H2("Graph"),
                                dcc.Graph(
                                    figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                                ),
                            ],
                            md=6)
                        ])
                    ],
                    md=9,
                ),
            ]
        )
    ],
    className="mt-4",
)