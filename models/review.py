#!/usr/bin/python3

"""
defines review class that inherits from basemodel
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    review class
    """
    place_id = ""
    user_id = ""
    text = ""
