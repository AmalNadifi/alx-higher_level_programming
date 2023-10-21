#!/usr/bin/python3
""" The following script prints the State object
 with the name passed as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ This is to access the database and get the states from
    the database

    Args:
        argv[1]: Database username
        argv[2]: Database password
        argv[3]: Database name
        argv[4]: Name of the state to retrieve from the database.
    """

    # Creating a database engine based on the command line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                          sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create tables defined in model_state using SQLAlchemy Base class
    Base.metadata.create_all(engine)

    # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for the State obj with the provided name
    state_instance = session.query(State).filter(
                            State.name == (sys.argv[4]).first())

    # Checking if a matching state was found and print its ID
    if state_instance is not None:
        print('{0}'.format(state_instance.id))
    else:
        print("Not found")
