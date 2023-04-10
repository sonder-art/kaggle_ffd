# Script con funciones para obtener todos los primary keys (profile_url) apartir de las tablas

from typing import List, Union
import pandas as pd

def extract_primary_key(data:Union[pd.DataFrame, List[pd.DataFrame], str, List[str]]) -> pd.DataFrame:
    ''' Puede recibir un dataframe o una lista de dataframes y devuelve un dataframe (name, profile_url) de todas las tablas sin duplicados'''
    pass
    