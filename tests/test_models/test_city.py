#!/usr/bin/python3
'''unittest for review'''

import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    '''tests review class'''

    def setUp(self):
        """Sets up prior to each test"""
        self.a = City()
        self.a.name = "San Francisco"
        self.a.save()
        self.b = City()
        self.b.name = "Las Vegas"
        self.b.save()

    def test_assign(self):
        """Tests to ensure assigning is accurate"""
        self.assertEqual(self.a.name, "San Francisco")
        self.assertEqual(self.b.name, "Las Vegas")
        self.assertTrue(self.a != self.b)
        self.assertTrue(hasattr(self.a, "name"))
        self.assertTrue(hasattr(self.b, "name"))

    def test_inherit(self):
        """Tests if inherits"""
        self.assertEqual('name' in City.__dict__, True)
        self.assertEqual(issubclass(type(self.a), BaseModel), True)
        self.assertEqual('name' in City.__dict__, True)
        self.assertEqual(issubclass(type(self.b), BaseModel), True)

    def test_type(self):
        """Tests types"""
        self.assertEqual(issubclass(type(self.a), BaseModel), True)
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.b.name, str)

    def test_create_update(self):
        """Tests if creating and saving works"""
        self.a.save()
        self.assertTrue(hasattr(self.a, "created_at"))
        self.assertTrue(hasattr(self.b, "created_at"))
        self.assertTrue(hasattr(self.a, "updated_at"))
        self.assertTrue(hasattr(self.b, "updated_at"))
        self.assertTrue(self.a.updated_at != self.b.updated_at)

if __name__ == "__main__":
    unittest.main()
