"""
Using SQLAlchemy, create a State class that inherits from
Base class, links to the MySQL table states and create rows
"""


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    A class state inheriting Base that is used
    to create a table and insert values in it
    """
