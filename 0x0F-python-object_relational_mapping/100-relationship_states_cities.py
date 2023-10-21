#!/usr/bin/python3
""" The following script creates the State “California”
with the City “San Francisco” from the database hbtn_0e_6_usa
"""
import sys
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_city import City


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
                          sys.argv[1], sys.argv[2], sys.argv[3]),
                          pool_pre_ping=True)

    # Create tables defined in model_state using SQLAlchemy Base class
    Base.metadata.create_all(engine)

    # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating new state obj named California
    cali_state = State(name='California')

    # Creating new city obj named San Fransisco
    SF_city = City(name='San Fransisco')

    # Associating the 'San Francisco' City with the 'California' State
    cali_state.cities.append(SF_city)

    # Adding the california state to the database
    session.add(cali_state)

    # Committing the changes to the db
    session.commit()

    # Closing the database session
    session.close()
