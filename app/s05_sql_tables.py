# Schemas
# Definiciones de las tablas que vamos a crear e SQL alchemy, recuerda que son 5
# Recuerda que aqui solo se definen, tienes que importarlas

from sqlalchemy.orm import declarative_base

# define the students table
Base = declarative_base()

class Competitions(Base):
    pass

class Datasets(Base):
    pass

class Discussions(Base):
    pass

class Notebooks(Base):
    pass

class Main(Base):
    pass

class Rankings(Base):
    pass