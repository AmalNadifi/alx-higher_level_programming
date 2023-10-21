#!/usr/bin/python3
""" The following script changes the name of a State object
 from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ This is to access the database and change the name of the given
    state

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

    # Query the database to retrive the state with id=2
    inst = session.query(State).filter(State.id == 2).first()

    # Updating the name of the state obj to New Mexico
    inst.name = "New Mexico"

    # Committing the changes to the db
    session.commit()

    # Closing the database session
    session.close()
