import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import base64

import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)

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


body = dbc.Container(
    [        
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Img(src='/assets/data-analytics.png'),
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
                        dbc.Input(placeholder="Filter 01", type="text"),
                        dbc.Input(placeholder="Filter 02", type="text"),
                        dbc.Input(placeholder="Filter 03", type="text"),
                        dbc.Label("Integrated by:"),
                        html.Img(src=app.get_asset_url('integrated-dicisfot.png')),
                    ],
                    md=3,
                ),
                dbc.Col(
                    [
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Mapa"),
                                dcc.Graph(id='graph', figure=fig)                                
                            ])
                        ]),
                        dbc.Row([
                            dbc.Col([
                                html.H2("Graph"),
                                dcc.Graph(
                                    figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                                ),
                                
                            ]),
                            dbc.Col([
                                html.H2("Graph"),
                                dcc.Graph(
                                    figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                                ),
                            ])
                        ])
                    ],
                    md=9,
                ),
            ]
        )
    ],
    className="mt-4",
)

app.layout = html.Div([body])

if __name__ == "__main__":
    app.run_server(port=5000)
