#!/usr/bin/python3
'''user unittests'''
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    def setup(self):
        '''sets up test'''
        self.a = User()
        self.a.save()
        self.b = User()
        self.b.first_name = 'Air'
        self.b.last_name = 'BnB'
        self.b.email = 'airbnb@gmail.com'

    def testempty(self):
        '''tests empty user'''
        self.assertEqual(self.a.password='')
        self.assertEqual(self.a.first_name='')
        self.assertEqual(self.a.last_name='')
        self.assertEqual(self.a.email='')

    def testequal(self):
        '''tests attributes of user'''
        self.assertEqual(self.b.first_name='Air')
        self.assertEqual(self.b.last_name='BnB')
        self.assertEqual(self.b.password='airbnb')
        self.assertEqual(self.b.email='airbnb@gmail.com')

    def testInDict(self):
        '''tests if keys are in dictionary'''
        self.assertIn('first_name', self.b.__dict__.keys())
        self.assertIn('last_name', self.b.__dict__.keys())
        self.assertIn('password', self.b.__dict__.keys())
        self.assertIn('email', self.b.__dict__.keys())
        self.assertNotIn('last_name', self.b.__dict__.keys())
        self.assertNotIn('password', self.b.__dict__.keys())
        self.assertNotIn('email', self.b.__dict__.keys())

    def test_type(self):
        """Tests types"""
        self.assertEqual(issubclass(type(self.a), BaseModel), True)
        self.assertIsInstance(self.b.first_name, str)
        self.assertIsInstance(self.b.last_name, str)
        self.assertIsInstance(self.b.password, str)
        self.assertIsInstance(self.b.email, str)

    def test_createupdate(self):
        '''tests creating and saving times'''
        self.a.save()
        self.assertTrue(hasattr(self.a, "created_at"))
        self.assertTrue(hasattr(self.b, "created_at"))
        self.assertTrue(hasattr(self.a, "updated_at"))
        self.assertTrue(hasattr(self.b, "updated_at"))
        self.assertTrue(self.a.updated_at != self.b.updated_at)


if __name__ == "__main__":
    unittest.main()
