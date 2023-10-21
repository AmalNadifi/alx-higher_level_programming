#!/usr/bin/python3
""" The following script lists all City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    """ This is to access the database and retrieve all the
    City objects

    Args:
        argv[1]: Database username
        argv[2]: Database password
        argv[3]: Database name
    """

    # Creating a database engine based on the command line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                          sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create tables defined in model_state using SQLAlchemy Base class
    Base.metadata.create_all(engine)

    # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to retrieve all State objects
    # and their associated City objects, ordered by State and City IDs.
    ST = session.query(State).join(City).order_by(City.id).all()

    # Loop through State objects and print their details
    # along with associated City objects.
    for state in ST:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
