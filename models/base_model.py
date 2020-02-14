#!/usr/bin/python3
"""
Module that defines all common attributes/methods
"""

from datetime import datetime
import json
import uuid


class BaseModel:
    """
    Class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Init of BaseModel, assigning each instance with unique id
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or "updated_at":
                    value = datetime.strptime(self.created_at or self.updated_at,
                                          '%m-%d-%Y')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns class name, id, and dict
        """
        syntax = "[{}] ({}) {}"
        return syntax.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing keys/values of __dict__ of the instance
        """
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
