#!/usr/bin/python3
"""
defines state class that inherits from BaseModel
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    the state of the application
    """
    name = ""
