#!/usr/bin/python3
""" The following script lists all State objects
 that contain the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ This is to access the database and get the states from
    the database
    """

    # Creating a database engine based on the command line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                          sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create tables defined in model_state using SQLAlchemy Base class
    Base.metadata.create_all(engine)

    # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for the State obj containing a
    state_instance = session.query(State).filter(State.name.contains('a'))

    # Iterating and printing the matching State objects with a
    for state_inst in state_instance:
        print(state_inst.id, state_inst.name, sep=": ")
