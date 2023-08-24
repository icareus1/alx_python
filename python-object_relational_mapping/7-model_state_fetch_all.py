"""
Using SQLAlchemy, lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    username = argv[0]
    password = argv[1]
    db_name = argv[2]

    path = (f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    engine = create_engine(path)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    states = sess.query(State).order_by(State.id).all()
    for state in states:
        print(f'{state.id}: {state.name}')
