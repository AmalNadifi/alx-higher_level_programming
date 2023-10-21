#!/usr/bin/python3
"""
This script introduces a City class and
a Base class for utilizing the SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """The following class is representing a City in the database.

    Attributes:
        __tablename__ (str): The name of the corresponding database table.
        id (int): The unique identifier for the city.
        name (str): The name of the City.
        state_id (int): The state to which belongs the city
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
