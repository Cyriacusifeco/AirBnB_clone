#!/usr/bin/python3

"""Module for test User class"""

import unittest
import json
import pep8
import datetime
from models.place import Place
from models.base_model import BaseModel
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test class for the Place class.
    """

    def test_place_inherits_from_base_model(self):
        """
        Tests if the Place class inherits from BaseModel.
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_place_has_city_id(self):
        """
        Tests if the Place class has an attribute "city_id".
        """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))

    def test_place_has_user_id(self):
        """
        Tests if the Place class has an attribute "user_id".
        """
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))

    def test_place_has_name(self):
        """
        Tests if the Place class has an attribute "name".
        """
        place = Place()
        self.assertTrue(hasattr(place, "name"))

    def test_place_has_description(self):
        """
        Tests if the Place class has an attribute "description".
        """
        place = Place()
        self.assertTrue(hasattr(place, "description"))

    def test_place_has_number_rooms(self):
        """
        Tests if the Place class has an attribute "number_rooms".
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))

    def test_place_has_number_bathrooms(self):
        """
        Tests if the Place class has an attribute "number_bathrooms".
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))

    def test_place_has_max_guest(self):
        """
        Tests if the Place class has an attribute "max_guest".
        """
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))

    def test_place_has_price_by_night(self):
        """
        Tests if the Place class has an attribute "price_by_night".
        """
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))

    def test_place_has_latitude(self):
        """
        Tests if the Place class has an attribute "latitude".
        """
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))

    def test_place_has_longitude(self):
        """
        Tests if the Place class has an attribute "longitude".
        """
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))

    def test_place_has_amenity_ids(self):
        """
        Tests if the Place class has an attribute "amenity_ids".
        """
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))

if __name__ == '__main__':
    unittest.main()

