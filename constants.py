stations = ['SKBO','SKBG','SKCL','SKCC','SKCG','SKPE','SKSP','SKSM','SKRG']

query = "SELECT * FROM dataclean where day_hour > now() - interval '1MONTH'"

air_names = {#'SKAR':'Aeropuerto Internacional el EdÃ©n (Armenia - QuindÃ­o)',
             'SKBG':'Aeropuerto Internacional Palonegro (Bucaramanga - Santander)',
             'SKBO':'Aeropuerto Internacional El Dorado (Bogotá¡ - Bogotá¡ D.C.)', 
             'SKCC':'Aeropuerto Internacional Camilo Daza (Cúcuta - Norte de Santander)', 
             'SKCG':'Aeropuerto Internacional Rafael Nuñez (Cartagena - Bolí­var)', 
             'SKCL':'Aeropuerto Internacional Alfonso Bonilla Aragon (Cali - Valle)', 
             #'SKMR':'Aeropuerto Internacional Los Garzones (MonterÃ­a - CÃ³rdoba)', 
             'SKPE':'Aeropuerto Internacional Matecaña (Pereira - Risaralda)',
             'SKSM': 'Aeropuerto Internacional Simón Bolivar (Santa Marta - Magdalena)',
             'SKSP':'Aeropuerto Internacional Gustavo Rojas Pinilla (San Andrés - Colombia)',
             'SKRG':'Aeropuerto Internacional José Marí­a Córdova (Medellí­n - Antioquia)',
             'SKBQ':'Aeropuerto Internacional Ernesto Cortissoz (Barranquilla - Atlantico)'}

################
#### Lista de diccionarios de Nombre De Variables Para el Dropdown

vars_list = [
    {'label':'Airport','value':'station_name'},
    {'label':'Date','value':'day_hour'},
    #{'label':'Longitude','value':'lon'},
    #{'label':'Latitude','value':'lat'},
    {'label':'Air Temperature (F)','value':'tmpf'},
    {'label':'Dew Point (F)','value':'dwpf'},
    {'label':'Relative Humidity %','value':'relh'},
    {'label':'Wind Direction (Degrees From North)','value':'drct'},
    {'label':'Wind Speed (Knots)','value':'sknt'},
    {'label':'Pressure in Altimeter','value':'alti'},
    {'label':'Horizontal Visibility','value':'vsby'},
    {'label':'Vertical Visibility','value':'skyl1'},
    {'label':'Apparent Temperature (Wind Chill or Heat Index in F)','value':'feel'},
    
]

################
#### Lista de diccionarios de Nombre De Variables Para el la Tabla 

vars_list_dt = [
    {'name':'Airport','id':'station_name'},
    {'name':'Date','id':'day_hour'},
    #{'name':'Longitude','id':'lon'},
    #{'name':'Latitude','id':'lat'},
    {'name':'Air Temperature (F)','id':'tmpf'},
    {'name':'Dew Point (F)','id':'dwpf'},
    {'name':'Relative Humidity %','id':'relh'},
    {'name':'Wind Direction (Degrees From North)','id':'drct'},
    {'name':'Wind Speed (Knots)','id':'sknt'},
    {'name':'Pressure in Altimeter','id':'alti'},
    {'name':'Horizontal Visibility','id':'vsby'},
    {'name':'Vertical Visibility','id':'skyl1'},
    {'name':'Apparent Temperature (Wind Chill or Heat Index in F)','id':'feel'},
    
] 