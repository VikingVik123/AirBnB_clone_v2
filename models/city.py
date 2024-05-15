#!/usr/bin/python3
"""
The city class for hbnb
"""

from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel

class City(BaseModel):
    """ 
    The city class, contains state ID and name 
    """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

