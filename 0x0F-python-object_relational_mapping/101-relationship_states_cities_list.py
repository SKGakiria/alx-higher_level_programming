#!/usr/bin/python3
"""Script listing all State objects, and corresponding City objects,
contained in the database 'hbtn_0e_101_usa'."""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Function that connects to MySQL server."""

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    obj_res = session.query(State).outerjoin(City).order_by(
              State.id, City.id).all()

    for state in obj_res:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.commit()

    session.close()
