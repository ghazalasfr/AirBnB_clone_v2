#!/usr/bin/python3
"""class storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """filestorage class:
        __file_path: ...
        __objects: ...
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """all objects 

        """

        if cls:
            returntype = dict()

            for x, y in self.__objects.items():
                if y.__class__ == cls:
                    returntype[x] = y

            return returntype

        return self.__objects

    def new(self, obj):
        """new objects
        """
        if obj:
            x = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[x] = obj

    def save(self):
        """save file path to JSON file path
        """
        my_dict = {}
        for x, val in self.__objects.items():
            my_dict[x] = val.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """reload function definition
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for x, val in (json.load(f)).items():
                    val = eval(val["__class__"])(**val)
                    self.__objects[x] = val
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects 
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)

            if self.__objects[key]:
                del self.__objects[key]
                self.save()

    def close(self):
        """close function 
        """
        self.reload()

