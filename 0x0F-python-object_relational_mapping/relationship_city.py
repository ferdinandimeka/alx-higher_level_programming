#!/usr/bin/python3
""" Definition of the City class """

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """ Class City """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
