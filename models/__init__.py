#!/bin/usr/python3

"""
unique `FileStorage` instance for the HBNB application

"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
