#!/usr/bin/python3
"""base model class"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """basemodel definition with attribues
    """

    id = Column(String(60), primary_x=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """init function
        Args:
        args: ...
        kwargs: ...
        Attributes:
        id: ...
        created_at: ....
        updated date
        """
        if kwargs:
            for x, y in kwargs.items():
                if x == "created_at" or x == "updated_at":
                    y = datetime.strptime(y, "%Y-%m-%dT%H:%M:%S.%f")
                if x != "__class__":
                    setattr(self, x, y)
                if 'id' not in kwargs:
                    self.id = str(uuid.uuid4())
                if 'created_at' not in kwargs:
                    self.created_at = datetime.now()

                if 'created_at' in kwargs and 'updated_at' not in kwargs:
                    self.updated_at = self.created_at
                else:
                    self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """str return string
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """save functio for updating
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        if my_dict['_sa_instance_state']:
            my_dict.pop('_sa_instance_state')

        return my_dict

    def delete(self):
        """delete function definition
        """

        models.storage.delete(self)
