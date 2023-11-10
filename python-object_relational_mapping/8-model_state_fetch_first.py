#!/usr/bin/python3
"""Nameless module to suck data out from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    row = session.query(State).limit(1).one()

    if row is not None:
        print("{0}: {1}".format(row.id, row.name))
    else:
        print("Nothing")
