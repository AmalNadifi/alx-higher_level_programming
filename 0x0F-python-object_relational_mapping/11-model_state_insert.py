#!/usr/bin/python3
""" The following script adds the State object
 “Louisiana” to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ This is to access the database and add a state to it

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

    # Creating a new state object named "louisiana"
    New_State = State(name='Louisiana')

    # Adding the new state to the database session
    session.add(New_State)

    # Query the database for the State obj with the 'Louisiana' name
    New = session.query(State).filter_by(
                            name='Louisiana').first()

    # Printing the new state's ID
    print(New.id)

    # Committing the changes to the db session
    session.commit()
