"""
Using SQLAlchemy, create a State class that inherits from
Base class, links to the MySQL table states and create rows
"""


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class representing the 'states' table in the database.
    
    Attributes:
        id (int): An auto-generated unique integer.
        name (str): the name of the state.
    """
    __tableau__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
