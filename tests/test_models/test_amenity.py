#!/usr/bin/python3
"""
Unit test module for the Amenity class.
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """
    Test class for the Amenity model.
    """
    def test_amenity_inherits_from_base_model(self):
        """
        Test that the Amenity model inherits from BaseModel.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_has_name(self):
        """
        Test that the Amenity model has a name attribute.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_amenity_name_is_empty_string(self):
        """
        Test that the name attribute of the Amenity model is an empty string.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()
