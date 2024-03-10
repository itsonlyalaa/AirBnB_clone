#!/usr/bin/python3

"""
a module that defines user class that inherits from basemodel
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    user class that contains users info
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
