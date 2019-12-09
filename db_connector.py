from sqlalchemy import create_engine
import pandas as pd
from constants import stations, query

engine = create_engine('postgresql://ds4a:93532zxc@localhost:5432/airports')

def get_data():    
    df = pd.read_sql(query, engine.connect(), parse_dates=('day_hour',))
    df = df[df['station'].isin(stations)]    
    return df