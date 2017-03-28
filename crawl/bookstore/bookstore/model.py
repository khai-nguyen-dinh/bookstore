from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

from bookstore import settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_book_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

class Book(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "book"
    id = Column('id',autoincrement=True,primary_key=True)
    book_name = Column('book_name', String)
    author = Column('author', String)
    thumbnail = Column('thumbnail', String, nullable=True)
    description = Column('description', String, nullable=True)
    price = Column('price', String, nullable=True)
