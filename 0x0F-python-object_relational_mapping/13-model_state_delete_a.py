#!/usr/bin/python3
""" The following script deletes all State objects
with the name with letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """ This is to access the database and delete state objects

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

    # Query the database to retrive all state obj whose names contain 'a'
    for inst in session.query(State).filter(State.name.like('%a%')):
        # DEleting each retrieved state obj
        session.delete(inst)

    # Committing the changes to the db
    session.commit()

    # Closing the database session
    session.close()
