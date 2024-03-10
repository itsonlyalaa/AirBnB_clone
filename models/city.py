#!/usr/bin/python3
"""
defines the city class that inherits from basemodel
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class
    """
    state_id = ""
    name = ""
