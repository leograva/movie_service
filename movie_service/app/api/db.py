from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database
import os

DATABASE_URI = 'postgresql://postgres:postgres@localhost/movie_db'
#

engine = create_engine(DATABASE_URI)
metadata = MetaData()

movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts', ARRAY(String))
)

database = Database(DATABASE_URI)