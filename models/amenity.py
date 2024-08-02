#!/usr/bin/python3
""" Amenity Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Amenity class for HBNB project"""
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
    place_amenities = relationship("Place",
                                   secondary='place_amenity',
                                   back_populates="amenities")
