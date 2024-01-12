#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """ File storage class """

    # Class variable to store the objects
    _objects = {}

    # Class variable to store the path of the JSON file
    _file_path = "file.json"

    # Dictionary to map class names to class objects
    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        # Add other classes as needed
    }

    def all(self):
        """ Returns the dictionary __objects """
        return self._objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self._objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        for key, value in self._objects.items():
            new_dict[key] = value.to_dict()
        with open(self._file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self._file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = self.CLASSES[class_name]
                    obj = cls(**value)
                    self._objects[key] = obj
        except FileNotFoundError:
            pass

