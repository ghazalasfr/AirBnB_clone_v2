#!/usr/bin/python3
"""init model

"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


storage_type = os.environ.get("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
