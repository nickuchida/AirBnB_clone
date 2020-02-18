#!/usr/bin/python3
'''Module for FileStorage'''
import json
import models
from models.base_model import BaseModel
from models.user import User
from pathlib import Path
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''Class FileStorage'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''Sets in __objects the obj with key <obj class name>.id'''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file (path: __file_path)'''
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as new_file:
            json.dump(new_dict, new_file)

    def reload(self):
        '''Deserializes the JSON file to __objects'''
        try:
            with open(self.__file_path, 'r') as my_json:
                self.__objects = json.load(my_json)
            for key, value in self.__objects.items():
                self.__objects[key] = BaseModel(**value)
        except:
            pass
