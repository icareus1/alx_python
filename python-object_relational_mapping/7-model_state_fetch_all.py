"""
Using SQLAlchemy, lists all State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    username = argv[0]
    password = argv[1]
    db_name = argv[2]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sess = Session()
    states = sess.query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')

    sess.close()
