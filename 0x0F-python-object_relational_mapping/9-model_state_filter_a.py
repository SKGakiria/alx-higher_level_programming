#!/usr/bin/python3
"""Script listing all State objects that contain the letter a
from 'hbtn_0e_6_usa'."""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Function that connects to MySQL server."""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by(
             State.id).all()
    if states is not None:
        for state in states:
            print('{0}: {1}'.format(state.id, state.name))
