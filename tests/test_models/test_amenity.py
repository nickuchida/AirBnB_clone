#!/usr/bin/python3
'''unittest for amenity'''
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    '''tests amenity class'''

    def setUp(self):
        self.a = Amenity()
        self.b = Amenity()
        self.b.name = 'air conditioning'

    def testempty(self):
        self.assertEqual(self.a.name, '')

    def testsub(self):
        self.assertTrue(issubclass(self.a.__class__, BaseModel), True)

    def testname(self):
        '''tests for keys in dictionary'''
        self.assertEqual(self.b.name, 'air conditioning')
        self.assertIn('name', self.b.__dict__.keys())
        self.assertNotIn('name', self.a.__dict__.keys())
        self.assertTrue(hasattr(self.b, 'name'))

    def testcreateupdate(self):
        '''tests create/update times'''
        self.assertTrue(hasattr(self.a, "created_at"))
        self.assertTrue(hasattr(self.a, "id"))
        self.assertTrue(hasattr(self.b, "created_at"))
        self.assertTrue(hasattr(self.a, "updated_at"))
        self.assertTrue(hasattr(self.b, "updated_at"))

if __name__ == "__main__":
    unittest.main()
