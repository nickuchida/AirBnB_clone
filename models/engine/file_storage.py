#!/usr/bin/env python3
import json
import models
from models.base_model import BaseModel
from models.user import User
from pathlib import Path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as new_file:
            json.dump(new_dict, new_file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as my_json:
                self.__objects = json.load(my_json)
            for key, value in self.__objects.items():
                self.__objects[key] = BaseModel(**value)
        except:
            pass
