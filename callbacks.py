import sys
import plotly.graph_objects as go
import dash_core_components as dcc
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output, State

from constants import vars_list_dt
from app import app
from logic import create_plot_data
from db_connector import get_data
import dash_table


# mapbox_access_token = open(".mapbox_token").read()
mapbox_access_token = 'pk.eyJ1IjoiYWNjaGF2ZXphIiwiYSI6ImNrMzY5cjd5djFoNDIzbHBvOTAyOG44ejUifQ.9DNyjQ1Zs94d9EmzkmbVuQ'
df = get_data()

# fig = go.Figure(data=go.Scattergeo(
#         locationmode = 'USA-states',
#         lon = df['long'],
#         lat = df['lat'],
#         text = df['text'],
#         mode = 'markers',
#         marker = dict(
#             size = 8,
#             opacity = 0.8,
#             reversescale = True,
#             autocolorscale = False,
#             symbol = 'square',
#             line = dict(
#                 width=1,
#                 color='rgba(79, 199, 218)'
#             ),
#             colorscale = 'purples',
#             cmin = 0,
#             color = df['cnt'],
#             cmax = df['cnt'].max(),
#             colorbar_title="Incoming flights<br>February 2011"
#         )))

# fig.update_layout(
#         geo = dict(
#             scope='usa',
#             projection_type='albers usa',
#             showland = True,
#             landcolor = "rgb(250, 250, 250)",
#             subunitcolor = "rgb(217, 217, 217)",
#             countrycolor = "rgb(217, 217, 217)",
#             countrywidth = 0.5,
#             subunitwidth = 0.5,            
#         ),
#     )

# @app.callback(
#     Output('datatable-paging', 'data'),
#     [Input('datatable-paging', "page_current"),
#      Input('datatable-paging', "page_size")])
# def update_table(page_current,page_size):
#     return df_table.iloc[
#         page_current*page_size:(page_current+ 1)*page_size
#     ].to_dict('records')

@app.callback(    
    Output('map-div', 'children'),
    [Input('select-airport','value')])
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

#########
### Call Back for the data table

@app.callback(
    Output('table-div', 'children'),
    [ 
    Input('select-airport', 'value'),
    Input('select-columns', 'value')
    ]
)

def update_table(airport,columns):
    vars_list_dt2 = [a for a in vars_list_dt if a['id'] in columns]
    dff = df.copy()
    if airport:
        dff = dff[dff['station']==airport]
    if columns:
        dff = dff[columns]

    children=[dash_table.DataTable(
                    id='table',
                    columns=vars_list_dt2,
                    data=dff.to_dict('records'),
                    style_cell={'width': '50px'},
                    style_table={
                        'maxHeight': '450px',
                        'overflowY': 'scroll'
                    })
                ]
    return children

#########
### Call Back for the models prediction

#################
### Horizontal Visibility

@app.callback(
    Output('horizontal-vis-plot', 'figure'),
    [ 
    Input('select-airport', 'value'),
    Input('btnProyection','n_clicks')
    ]
)

def update_hvis_plot(station,n_clicks):
    dff = create_plot_data(df=df,station=station,variable='vsby')
    lim = get_treshold(station=station,variable='vsby')
    limit = pd.DataFrame({'day_hour':dff['day_hour'],'limit':lim})
    plot_data = []
    
    if(n_clicks==0):
        
        print('es mi primer no debo pintar prediccion desde dropdown soloo historico')

        data = dff[dff.type=="Current"]
        plot_data.append(
        go.Scatter(x=data['day_hour'],y=data['vsby'],name='Current',mode='lines+markers')  
        )  

        plot_data.append(
        go.Scatter(x=limit['day_hour'],y=limit['limit'],name='Limit',mode='markers')  
        )
    else:
        print('solo pintar prediccion')
        
        for key, data in dff.groupby('type'):
            plot_data.append(
                go.Scatter(x=data['day_hour'],y=data['vsby'],name=key,mode='lines+markers')
            )

        plot_data.append(
        go.Scatter(x=limit['day_hour'],y=limit['limit'],name='Limit',mode='markers')  
        )
      
    layout = go.Layout(title="Horizontal Visibility Prediction",
                       yaxis={"title":"Horizontal Visibility (Miles)"},
                       xaxis={"title":"Date"})   
    return {
        "data":plot_data,
        "layout": layout
    }

def get_treshold(station, variable):
    tresh = pd.read_csv('dash/treshold.csv')
    ## Info is in meters convert horizontal to miles and vertical to feet
    tresh['value'] = np.where(tresh['variable']=='vsby',tresh['value']/1609.344,tresh['value']*3.28084)
    x = tresh.loc[(tresh['station']==station) & (tresh['variable']==variable),'value'].values[0]
    return x

### Vertical Visibility
#################
### Vertical Visibility

@app.callback(
    Output('btnProyection','n_clicks'),
    [ 
    Input('select-airport', 'value'),
    ]
)

def resetButton(reset):
    return 0



@app.callback(
    Output('vertical-vis-plot', 'figure'),
    [ 
    Input('select-airport', 'value'),
    Input('btnProyection','n_clicks')
    ]
)


def update_vvis_plot(station,n_clicks):
    dff = create_plot_data(df=df,station=station,variable='skyl1')
    lim = get_treshold(station=station,variable='skyl1')
    limit = pd.DataFrame({'day_hour':dff['day_hour'],'limit':lim})
    plot_data = []

    if(n_clicks==0):
        
        print('es mi primer no debo pintar prediccion desde dropdown soloo historico')

        data = dff[dff.type=="Current"]
        plot_data.append(
            go.Scatter(x=data['day_hour'],y=data['skyl1'],name='Current',mode='lines+markers')
        )
        plot_data.append(
        go.Scatter(x=limit['day_hour'],y=limit['limit'],name='Limit',mode='markers')  
        )
        
    else:
        print('solo pintar prediccion')
        for key, data in dff.groupby('type'):
            plot_data.append(
                go.Scatter(x=data['day_hour'],y=data['skyl1'],name=key,mode='lines+markers')
            )

        plot_data.append(
        go.Scatter(x=limit['day_hour'],y=limit['limit'],name='Limit',mode='markers')  
        )

    layout = go.Layout(title="Vertical Visibility Prediction",
                       yaxis={"title":"Vertical Visibility (Feet)"},
                       xaxis={"title":"Date"})   

    return {
        "data":plot_data,
        "layout": layout
    }

###button callback
@app.callback([Output('checklist-horizontal1', 'labelClassName'),
               Output('checklist-horizontal2', 'labelClassName'),
               Output('checklist-horizontal3', 'labelClassName'),
               Output('checklist-horizontal4', 'labelClassName'),
               Output('checklist-horizontal5', 'labelClassName'),
               Output('checklist-horizontal6', 'labelClassName'),
               Output('checklist-vertical1', 'labelClassName'),
               Output('checklist-vertical2', 'labelClassName'),
               Output('checklist-vertical3', 'labelClassName'),
               Output('checklist-vertical4', 'labelClassName'),
               Output('checklist-vertical5', 'labelClassName'),
               Output('checklist-vertical6', 'labelClassName')],               
              [Input('btnProyection','n_clicks')],
              [State('select-airport', 'value')])

def update_checklist(n_clicks, ddl_value):        
    # dff_v = create_plot_data(df=df,station=ddl_value,variable='skyl1')
    # data_pred_v = dff_v[dff_v.type=="Prediction"]    
    # lim_v = get_treshold(station=ddl_value,variable='skyl1')
    # limit_v = pd.DataFrame({'day_hour':dff_v['day_hour'],'limit':lim_v})
    # plot_styles = []
    # data_pred_v = dff_v[dff_v.type=="Prediction"]    
    # for key,data in data_pred_v.items():
    #     if key == 'skyl1':
    #         print(data)
    #         if data[0] > limit_v['limit']:
    #             print('entre')
    #             plot_styles.append('start-checklist')
    #         else:
    #             plot_styles.append('stop-checklist')

    # dff_h = create_plot_data(df=df,station=ddl_value,variable='vsby')
    # lim_h = get_treshold(station=ddl_value,variable='vsby')
    # limit_h = pd.DataFrame({'day_hour':dff_h['day_hour'],'limit':lim_h})
    # plot_styles = []
    # data_pred_h = dff_h[dff_h.type=="Prediction"]
    # for key,data in data_pred_h.items():
    #     if data['vsby'] > limit_h['limit']:
    #         plot_styles.append('start-checklist')
    #     else:
    #         plot_styles.append('stop-checklist')
        
    # return plot_styles[0],plot_styles[1], plot_styles[2], plot_styles[3] ,plot_styles[4] , plot_styles[5], plot_styles[6] ,plot_styles[7] ,plot_styles[8] ,plot_styles[9], plot_styles[10], plot_styles[11], plot_styles[12]
    return 'start-checklist','stop-checklist','start-checklist','stop-checklist','start-checklist','stop-checklist','start-checklist','stop-checklist','start-checklist','stop-checklist','start-checklist','stop-checklist'