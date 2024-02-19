#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
this modul is about storage of objects
the file storage
"""

import json
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.base_model import BaseModel
from models.place import Place
from os import path
from models.city import City



class FileStorage:
    """fileStorage
    the filestorage class with
    2 Attributes:
        __file_path (str)
        __objects (dict)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all function
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """the new function
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def reload(self):
        """the reload fucntion 
        deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists 
        ;otherwise, do nothing. If the file doesnt 
        exist, no exception should be raised)
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as dossier:
                store = json.loads(dossier.read())
                for y, z in store.items():
                    self.__objects[y] = eval(z['__class__'])(**z)

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        store = {}
        for i, v in self.__objects.items():
            store[i] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as dossier:
            dossier.write(json.dumps(store))
