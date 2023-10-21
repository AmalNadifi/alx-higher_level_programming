#!/usr/bin/python3
"""
This script introduces a State class and
a Base class for utilizing the SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """The following class is representing a State in the database.

    Attributes:
        __tablename__ (str): The name of the corresponding database table.
        id (int): The unique identifier for the State.
        name (str): The name of the State.
        cities (obj): The cities belonging to the State
    """
    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
