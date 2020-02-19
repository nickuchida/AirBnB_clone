#!/usr/bin/python3
'''unittest for review'''
import unittest
from datetime import datetime
from models.review import Review
from base_model import BaseModel

class TestReview(unittest.TestCase):
    '''tests review class'''

    def setUp(self):
        self.a = Review()
        self.a.save()
        self.b = Review()
        self.b.place_id = 'Place'
        self.b.user_id = 'User'
        self.b.text = 'place text'
        self.b.save()

    def test_empty(self):
        self.assertEqual(self.a.place_id, '')
        self.assertEqual(self.a.user_id, '')
        self.assertEqual(self.a.text, '')

    def test_review(self):
        self.assertEqual(self.b.place_id, 'Place')
        self.assertEqual(self.b.user_id, 'User')
        self.assertEqual(self.b.text, 'place text')

    def test_type(self):
        """Tests types"""
        self.assertEqual(issubclass(type(self.b), BaseModel), True)
        self.assertIsInstance(self.b.place_id, str)
        self.assertIsInstance(self.b.user_id, str)
        self.assertIsInstance(self.b.text, str)

    def test_createupdate(self):
        self.assertTrue(hasattr(self.a, "created_at"))
        self.assertTrue(hasattr(self.b, "created_at"))
        self.assertTrue(hasattr(self.a, "updated_at"))
        self.assertTrue(hasattr(self.b, "updated_at"))

if __name__ == "__main__":
    unittest.main()
