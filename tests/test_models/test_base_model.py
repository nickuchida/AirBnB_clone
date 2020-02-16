#!/usr/bin/python3
"""Unittest for Class BaseModel"""

import unittest
import json
from models import base_model
from models.base_model import BaseModel
from datetime import datetime

class TestBase(unittest.TestCase):
    """Testing Class BaseModel"""

    def setUp(self):
        """Set up for prior to each test"""
        self.a = BaseModel()
        self.a.name = "Nick"
        self.a.my_number = 54

    def tearDown(self):
        """Tears down after each test"""
        self.a = None

    def test_id(self):
        """Tests to make sure uuid works"""
        b = BaseModel()
        self.assertNotEqual(self.a.id, b.id)
        self.assertEqual(type(self.a.id), type(b.id))
        self.assertTrue(self.a.id != b.id)
        self.assertFalse(self.a.id == b.id)

    def test_type(self):
        """Tests for type"""
        self.assertIsInstance(self.a, BaseModel)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.__class__, type)
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.my_number, int)
        self.assertEqual(type(self.a.created_at), datetime)
        self.assertEqual(type(self.a.updated_at), datetime)

    def test_attributes(self):
        """Tests to make sure assigning values works"""
        self.assertTrue(hasattr(self.a, "id"))
        self.assertTrue(hasattr(self.a, "__class__"))
        self.assertTrue(hasattr(self.a, "created_at"))
        self.assertTrue(hasattr(self.a, "updated_at"))
        self.assertTrue(hasattr(self.a, "name"))
        self.assertEqual(self.a.name, "Nick")
        self.assertNotEqual(self.a.name, "Christine")
        self.assertTrue(hasattr(self.a, "my_number"))
        self.assertEqual(self.a.my_number, 54)
        self.assertNotEqual(self.a.my_number, "29")
        self.assertEqual(type(self.a.id), str)
        self.assertEqual(type(self.a), BaseModel)

    def test_str(self):
        """Tests output syntax"""
        str1 = "[BaseModel] ({}) {}".format(self.a.id, self.a.__dict__)
        self.assertEqual(str1, str(self.a))

if __name__ == '__main__':
    unittest.main()
