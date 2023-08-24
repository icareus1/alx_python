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
    
    if __name__== '__main__':
        id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
        name = Column(String, nullable=False)
        engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{db_name}')
        Base.metadata.create_all(engine)