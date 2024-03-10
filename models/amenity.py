#!/usr/bin/python3
"""
defines amenity class that inherits from basemodel
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    amenities that are provided by the place owner
    """
    name = ""
