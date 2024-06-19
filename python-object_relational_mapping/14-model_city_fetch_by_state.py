#!/usr/bin/python3
""" Next, write a script 14-model_city_fetch_by_state.py that
prints all City objects from the database hbtn_0e_14_usa: """

import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State.name).filter_by(id=city.state_id)\
                     .first()
        print("{}: ({}) {}".format(state_name[0], city.id, city.name))
