#!/usr/bin/python3
"""
Unit test module for the Review class.
"""

import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """
    Test class for the Review model.
    """

    def test_review_inherits_from_base_model(self):
        """
        Test that the Review model inherits from BaseModel.
        """
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_has_place_id(self):
        """
        Test that the Review model has a place_id attribute.
        """
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))

    def test_review_has_user_id(self):
        """
        Test that the Review model has a user_id attribute.
        """
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))

    def test_review_has_text(self):
        """
        Test that the Review model has a text attribute.
        """
        review = Review()
        self.assertTrue(hasattr(review, "text"))

    def test_review_place_id_is_empty_string(self):
        """
        Test that the place_id attribute of the Review model is an empty string.
        """
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_review_user_id_is_empty_string(self):
        """
        Test that the user_id attribute of the Review model is an empty string.
        """
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_review_text_is_empty_string(self):
        """
        Test that the text attribute of the Review model is an empty string.
        """
        review = Review()
        self.assertEqual(review.text, "")

if __name__ == '__main__':
        unittest.main()
