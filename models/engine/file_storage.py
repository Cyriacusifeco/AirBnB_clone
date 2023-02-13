#!/usr/bin/python3
"""
A module that serializes instances to a
JSON file and deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    A class that serializes instances to a
    JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        A method that returns the __objects dictionary.

        """

        return FileStorage.__objects

    def new(self, obj):
        """
        A method that adds an object to the __objects dictionary.

        """

        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """
        A method that saves the objects stored in the
        __objects dictionary to the JSON file.

        """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:

            objects_dict = {
                key: obj.to_dict() for key,
                obj in FileStorage.__objects.items()}
            json.dump(objects_dict, f)

    def reload(self):
        """
        A method that reloads the objects from the JSON file and
        store them in the __objects dictionary.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:

                objects_dict = json.load(f)

                for key, obj_dict in objects_dict.items():
                    class_name, obj_id = key.split(".")
                    obj_dict['__class__'] = class_name
                    FileStorage.__objects[key] = eval(class_name)(**obj_dict)

        except FileNotFoundError:
            pass
