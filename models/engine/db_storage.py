#!/usr/bin/python3
"""db model class"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

all_classes = {"State", "City", "Amenity", "User", "Place", "Review"}


class DBStorage:
    """dbstorage class

    Attributes:
        __engine: ....
        __session: ....
    """

    __engine = None
    __session = None

    def __init__(self):
        """init function
        """

        db_uri = "{0}+{1}://{2}:{3}@{4}:3306/{5}".format(
            'mysql', 'mysqldb', getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB'))

        self.__engine = create_engine(db_uri, pool_pre_ping=True)
        self.reload()

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all fucntion that list all
        """
        entities = dict()

        if cls:
            return self.get_data_from_table(cls, entities)

        for entity in all_classes:
            entities = self.get_data_from_table(eval(entity), entities)

        return entities

    def new(self, obj):
        """new for new session
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """save all function
        """

        self.__session.commit()

    def delete(self, obj=None):
        """delete function
        """

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload function
        """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def get_data_from_table(self, cls, structure):
        """get data from table
        """

        if type(structure) is dict:
            query = self.__session.query(cls)

            for _row in query.all():
                key = "{}.{}".format(cls.__name__, _row.id)
                structure[key] = _row

            return structure

    def close(self):
        """close function
        """
        self.__session.close()