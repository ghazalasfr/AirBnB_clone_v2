#!/usr/bin/python3
"""place class model"""
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity, place_amenity
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models


class Place(BaseModel, Base):
    """place class

    Attributes:
        __tablename__ (str): ...
        city_id (sqlalchemy String): ...
        user_id (sqlalchemy String): ...
        name (sqlalchemy String): ...
        description (sqlalchemy String): ...
        number_rooms (sqlalchemy Integer): ...
        number_bathrooms (sqlalchemy Integer): ...
        max_guest (sqlalchemy Integer): ...
        price_by_night (sqlalchemy Integer): ...
        latitude (sqlalchemy Float): ...
        longitude (sqlalchemy Float): ...
        reviews (sqlalchemy relationship): ...
        amenities (sqlalchemy relationship): ...
        amenity_ids (list): ...

    """

    __tablename__ = "places"

    if getenv('HBNB_TYPE_STORAGE') == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(128))
        number_rooms = Column(Integer, default=0)
        number_bathrooms = Column(Integer, default=0)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Integer, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship('Amenity', secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)
        amenity_ids = []
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """reviews definition
            """

            review_list = []

            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)

            return review_list

        @property
        def amenities(self):
            """amenties definition
            """

            listes = []

            for x in models.storage.all(Amenity).values():
                if x.id in self.amenity_ids:
                    listes.append(x)

            return listes

        @amenities.setter
        def amenities(self, value):
            """Adding amenites
            """

            if type(value) == Amenity:
                self.amenity_ids.append(value.id)

