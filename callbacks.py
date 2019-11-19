import sys
import plotly.graph_objects as go
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output, State

from app import app

# mapbox_access_token = open(".mapbox_token").read()
mapbox_access_token = 'pk.eyJ1IjoiYWNjaGF2ZXphIiwiYSI6ImNrMzY5cjd5djFoNDIzbHBvOTAyOG44ejUifQ.9DNyjQ1Zs94d9EmzkmbVuQ'

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
                color='rgba(79, 199, 218)'
            ),
            colorscale = 'purples',
            cmin = 0,
            color = df['cnt'],
            cmax = df['cnt'].max(),
            colorbar_title="Incoming flights<br>February 2011"
        )))

fig.update_layout(
        geo = dict(
            scope='usa',
            projection_type='albers usa',
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5,            
        ),
    )

@app.callback(
    Output('datatable-paging', 'data'),
    [Input('datatable-paging', "page_current"),
     Input('datatable-paging', "page_size")])
def update_table(page_current,page_size):
    return df_table.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')

@app.callback(    
    Output('map-div', 'children'),
    [Input('airport-select','value')])
def update_map(airport_id):
    print('cambio de mapa')    

    fig = go.Figure(go.Scattermapbox(
            lat=['4.4528825',
                    '5.2067919',
                    '4.6931832',
                    '7.1156792',
                    '3.5411098',
                    '7.9169411',
                    '10.446381',
                    '4.8151963',
                    '12.5861164',
                    '11.116147',
                    '8.8251965'],
            lon =['-75.7684869',
                    '-74.8877517',
                    '-74.1460662',
                    '-73.1721692',
                    '-76.3867725',
                    '-72.5126214',
                    '-75.5174062',
                    '-75.7384446',
                    '-81.7043465',
                    '-74.2343331',
                    '-75.8262014'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=14,
                symbol='airport'
            ),
            text=['Armenia', 'Mariquita', 'Bogotá', 'Bucaramanga', 'Cali', 'Cucuta', 'Cartagena', 'Pereira', 'San Andres', 'Santa Marta', 'Monteria'],
            showlegend=False
        ))

    fig.update_layout(
        hovermode='closest',
        mapbox=go.layout.Mapbox(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=5.2067919,
                lon=-74.8877517
            ),
            pitch=0,
            zoom=5            
        )
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":15})    
    return dcc.Graph(id='graph', figure=fig)

