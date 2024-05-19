#!/usr/bin/python3
"""
Module base_model
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    A base class for all models in our AirBnB clone.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if hasattr(self, 'created_at') and type(self.created_at) is str:
                self.created_at = datetime.fromisoformat(self.created_at)
            if hasattr(self, 'updated_at') and type(self.updated_at) is str:
                self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Return the string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of the instance.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

