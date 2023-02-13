import unittest
from models.city import City
from models.base_model import BaseModel

"""
Test module for City.
"""
class TestCity(unittest.TestCase):
    """
    Test cases for City
    """
    def test_city_inherits_from_base_model(self):
        """
        test city inherits from BaseModel
        """
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_has_state_id(self):
        """
        Test it has state
        """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))

    def test_city_has_name(self):
        """
        Test it has name
        """
        city = City()
        self.assertTrue(hasattr(city, "name"))

    def test_city_state_id_is_empty_string(self):
        """
        Test it's empty
        """
        city = City()
        self.assertEqual(city.state_id, "")

    def test_city_name_is_empty_string(self):
        """
        Test name is empty.
        """
        city = City()
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()

