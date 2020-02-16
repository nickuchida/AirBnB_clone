#!/usr/bin/env python3
import json
import models

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)

    def save(self):
        new_dict = {}
        for key, value in self.__objects:
            new_dict[id] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as new_file:
            json.dump(new_dict, new_file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'w') as loads:
                obj = json.loads(__file_path)
        except:
            pass
