#!/usr/bin/python3
"""
Module Db_storage
"""
import os
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.state import State
from sqlalchemy.orm.scoping import scoped_session

classes = {'User': User,'State': State }

class DBStorage:
    '''
    defines Dbstoraage for db in msql
    '''
    __engine = None
    __session = None
    def __init__(self):
        self.__engine
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__class__.__engine=create_engine('mysql+mysqldb://{}:{}@{}'
                                    .format(user, pwd, host,db),pool_pre_ping=True )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self,cls=None):
        """query all objects depending on the class name"""
        obj_dict = {}
        if cls is not None:
            a_query = self.__class__.__session.query(DBStorage.classes[cls])
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
            return obj_dict

        for c in DBStorage.classes.values():
            a_query = self.__class__.__session.query(c)
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
        return obj_dict
    def new(self, obj):
        '''
        add the obj to the current db session
        '''
        self.__session.add(obj)
    def save(self):
        '''
        commit all changes to current db session
        '''
        self.__session.commit()
        self.__session.close_all()
    def delete(self, obj=None):
        '''delete from the curent db session'''
        if obj is not None:
            for clas in self.__session.query(obj).all():
                self.__session.delete(obj)
            self.__session.commit()
    def reload(self):
        '''
        create all tables in db
        '''
        Base.metadata.create_all(self.__engine)
        self.__class__.__session = scoped_session(
            sessionmaker
            (
                bind=self.__session,
                expire_on_commit=False
            )
            )
    def close(self):
        '''clsoe on the class session'''
        self.__class__.__session.close()
