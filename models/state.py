#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy.orm import relationship
from models.city import City
import models

storage_type = getenv('HBNB_TYPE_STORAGE')
class State(BaseModel, Base):
    """ State class """
    if storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("city", cascade='all, delete', backref='state')
    else:
        nam = ''

        @property
        def cities(self):
            'getter atrribute cities'
            rlist = []
            dicCity = models.storage.all(City)
            for city in models.storage.all(City).values:
                if city.state_if == self.id:
                    rlist.append(city)
            return rlist
