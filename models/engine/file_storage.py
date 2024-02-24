#!/usr/bin/python3
"""filestorage model"""
import json


class FileStorage:
    """file storage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Return all"""
        objs = {}
        if cls:
            class_name = cls.__name__
            for key, val in self.__objects.items():
                # print(val.__class__.__name__, class_name)
                if val.__class__.__name__ == class_name:
                    objs[key] = val
            return objs
        return self.__objects

    def new(self, obj):
        """Add new one"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Save def"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def reload(self):
        """Loads models"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    # print(classes[val['__class__']](**val))
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj"""
        if obj:
            class_name = f"{obj.__class__.__name__}.{obj.id}"
            del FileStorage.__objects[class_name]

