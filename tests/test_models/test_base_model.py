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
        self.assertEqual(self.a.id == "", False)
        self.assertTrue(hasattr(self.a, "__class__"))
        self.assertTrue(hasattr(self.a, "__dict__"))
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

    def test_save(self):
        """Tests if save works"""
        self.a.save()
        self.assertFalse(self.a.created_at == self.a.updated_at)
        self.assertNotEqual(self.a.created_at, self.a.updated_at)

    def test_to_dict(self):
        da = self.a.to_dict()
        e = BaseModel()
        de = e.to_dict()
        self.assertEqual(self.a.__class__.__name__, "BaseModel")
        self.assertEqual(type(da), dict)
        self.assertIsInstance(da["created_at"], str)
        self.assertTrue("created_at" in self.a.to_dict(), True)
        self.assertIsInstance(da["updated_at"], str)
        self.assertTrue("updated_at" in self.a.to_dict(), True)
        self.assertFalse(da == de)



if __name__ == '__main__':
    unittest.main()
