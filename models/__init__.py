#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.db_storage import DBStorage
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    from models.engine import db_storage
    storage = db_storage.DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()