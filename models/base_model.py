#!/usr/bin/python3

"""
defines BaseModel class
"""

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Base class that contains all methods or attributes in other classes
    """
    def __init__(self, *args, **kwargs):
        """
        instatiates a object with its attribute
        """
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            return
        if "id" not in kwargs:
            kwargs['id'] = str(uuid4())
            self.id = kwargs['id']
            
        for key, value in kwargs.items():
            if key == "__class__":
                continue
            
        if "created_ at" in kwargs:
            self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        
        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        
    def __str__(self):
        """
        returns string representation
        """
        frmt = "[{}] ({}) {}"
        return frmt.format(type(self).__name__, self.id, self.__dict__)
        
    def save(self):
        """
        updates updated_at with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()
        
    def to_dict(self):
        """
        returns a dictionary containing all keys or values of __dict__
        """
        dct = {**self.__dict__}
        dct['__class__'] = type(self).__name__
        dct['created_at'] = dct['created_at'].isoformat()
        dct['updated_at'] = dct['updated_at'].isoformat()
        return dct
