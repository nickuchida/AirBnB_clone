#!/usr/bin/python3
"""
Module that defines all common attributes/methods
"""

from datetime import datetime
from models.engine.file_storage import FileStorage
from FileStorage import storage
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
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            self.save()

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
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing keys/values of __dict__ of the instance
        """
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
