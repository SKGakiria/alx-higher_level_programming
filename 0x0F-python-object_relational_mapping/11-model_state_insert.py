#!/usr/bin/python3
"""Script adds the State object “Louisiana” to the database 'hbtn_0e_6_usa'.
"""

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

    new_name = "Louisiana"
    new_state = State(name=new_name)
    session.add(new_state)
    session.commit()

    print('{0}'.format(new_state.id))
    session.close()
