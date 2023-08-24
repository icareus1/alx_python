"""
Using SQLAlchemy, create a State class that inherits from
Base class, links to the MySQL table states and create rows
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sys import argv

username = argv[1]
password = argv[2]
db_name = argv[3]

Base = declarative_base()

class State(Base):
    """
    A class state inheriting Base that is used
    to create a table and insert values in it
    """
    if __name__== '__main__':
        __tableau__ = 'states'
        id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
        name = Column(String(128), nullable=False)
        engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{db_name}')
        Base.metadata.create_all(engine)