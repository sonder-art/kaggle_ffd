# Funciones para Crear engines, conexiones, sesiones e inspecciones con SQL alchemy

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

# Variables de entorno
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')

def start_engine(echo:bool=False):
    db_string = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    engine = create_engine(db_string, echo=echo)
    return engine


def connect_engine(echo:bool=False):
    engine = start_engine(echo)
    # Crear una sesion con sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def inspect_engine(echo:bool=False):
    engine = start_engine(echo)
    inspector = inspect(engine)
    return inspector 

