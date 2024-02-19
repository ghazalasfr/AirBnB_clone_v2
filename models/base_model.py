#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Base Model Module

the class BaseModel that defines all common
attributes/methods for other classes

"""

import models
import uuid
from datetime import datetime



class BaseModel:
    """Base Model Class

    This is the Base Model that take care of the
    initialization, serialization and deserialization
    of the future instances.

    Public instance attributes:
    id: string 
    created_at: datetime
    updated_at: datetime
    __str__: should print
    Public instance methods:
    save(self)
    to_dict(self)

    """

    def __init__(self, *args, **kwargs):
        """the init function

        the default values of a Base Model

        """
        if kwargs:
            for arg, y in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    y = datetime.strptime(y, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    setattr(self, arg, y)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the object class"""
        return '[{0}] ({1}) {2}'.format(
                self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """Updates function
        Updates the public instance

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """the to dict function
        Returns a new dictionary

        """
        informations = self.__dict__.copy()
        informations['__class__'] = self.__class__.__name__
        informations['created_at'] = self.created_at.isoformat()
        informations['updated_at'] = self.updated_at.isoformat()

        return informations
