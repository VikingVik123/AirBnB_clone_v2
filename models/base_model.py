#!/usr/bin/python3
""" 
Module that defines a base class for all models in our hbnb clone
"""
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, create_engine,String
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()
class BaseModel:
    """ Base class for all hbnb models"""

    id = Column(String(120), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)


    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""

        self.id = kwargs.get("id", str(uuid.uuid4()))
        self.created_at = kwargs.get("created_at", datetime.now())
        self.updated_at = kwargs.get("updated_at", datetime.now())

        if isinstance(self.created_at, str):
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
        if isinstance(self.updated_at, str):
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")

        for key, value in kwargs.items():
            if key not in {"__class__", "id", "created_at", "updated_at"}:
                setattr(self, key, value)


    def __str__(self):
        """
        Returns a string representation of the instance
        """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        Updates updated_at with current time when instance is changed
        """
        from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Convert instance into dict format
        """
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = type(self).__name__

        # Handle missing timestamps defensively
        if not self.created_at:
            self.created_at = datetime.now()
        if not self.updated_at:
            self.updated_at = datetime.now()

        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        # Remove SQLAlchemy internal state if present
        dictionary.pop('_sa_instance_state', None)

        return dictionary


    def delete(self):
        """
        Delete the current instance from the storage
        """
        models.storage.delete(self)

