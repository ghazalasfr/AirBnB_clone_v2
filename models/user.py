#!/usr/bin/python3
"""
 User class model 
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class with :
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
