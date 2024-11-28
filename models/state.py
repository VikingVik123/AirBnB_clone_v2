#!/usr/bin/python3
"""
The state class
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """
        Getter attribute for cities
        """
        from models import storage
        cities_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list

