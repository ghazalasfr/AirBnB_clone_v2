#!/usr/bin/python3
"""user class"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ user class

    Attributes:
        __tablename__: .....
        email: (sqlalchemy String): ...
        password (sqlalchemy String): ...
        first_name (sqlalchemy String): ...
        last_name (sqlalchemy String): ...
        places (sqlalchemy relationship): ...
        reviews (sqlalchemy relationship): ...

    """

    __tablename__ = "users"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
