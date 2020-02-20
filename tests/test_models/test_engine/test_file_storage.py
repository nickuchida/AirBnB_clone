#!/usr/bin/python3
"""Unittest for Class BaseModel"""

import unittest
import json
from models import base_model
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from datetime import datetime
import os

class TestFileStorage(unittest.TestCase):
    """Testing for class FileStorage"""
    def setUp(self):
        self.u = User()
        self.u.first_name = "Nick"
        self.u.last_name = "Uchida"
        self.u.email = "me@me.com"
        self.u.password = "1234"
        self.x = User()
        self.x.first_name = "Christine"
        self.x.last_name = "Pang"
        self.x.email = "you@me.com"
        self.x.password = "4321"

    def test_att(self):
        """Tests if all attributes of FileStorage exist"""
        self.assertTrue(hasattr(self.u, "__class__"))
        self.assertTrue(hasattr(self.u, "created_at"))
        self.assertTrue(hasattr(self.u, "updated_at"))
        self.assertTrue(hasattr(self.u, "first_name"))
        self.assertTrue(hasattr(self.u, "last_name"))
        self.assertTrue(hasattr(self.u, "email"))
        self.assertTrue(hasattr(self.u, "password"))


    def test_assignment(self):
        """Tests if accurate assignment has happened"""
        self.assertEqual(self.u.first_name, "Nick")
        self.assertEqual(self.u.last_name, "Uchida")
        self.assertEqual(self.u.email, "me@me.com")
        self.assertEqual(self.u.password, "1234")
        self.assertNotEqual(self.u.first_name, self.x.first_name)
        self.assertNotEqual(self.u.last_name, self.x.last_name)
        self.assertNotEqual(self.u.email, self.x.email)
        self.assertNotEqual(self.u.password, self.x.password)


    def test_id(self):
        """Tests that each User is unique"""
        self.assertNotEqual(self.u.id, self.x.id)
        self.assertEqual(type(self.u.id), type(self.x.id))
        self.assertTrue(self.u.id != self.x.id)
        self.assertFalse(self.u.id == self.x.id)


    def test_inherit(self):
        """Tests if inheritance happened"""
        self.assertIsInstance(self.u, BaseModel)
        self.assertEqual(type(self.u), type(self.x))
        self.assertTrue(issubclass(self.u.__class__, BaseModel))


    def test_type(self):
        """Tests type"""
        self.assertIsInstance(self.u, BaseModel)
        self.assertIsInstance(self.u.id, str)
        self.assertIsInstance(self.u.__class__, type)
        self.assertIsInstance(self.u.first_name, str)
        self.assertIsInstance(self.u.last_name, str)
        self.assertIsInstance(self.u.email, str)
        self.assertIsInstance(self.u.password, str)
        self.assertEqual(type(self.u.created_at), datetime)
        self.assertEqual(type(self.u.updated_at), datetime)
        self.assertEqual(type(self.u.__dict__), dict)

    def test_all(self):
        """Tests the instance method of all"""
        f = FileStorage()
        fd = f.all()
        self.assertIsInstance(fd, dict)
        self.assertIsNotNone(fd)
        self.assertEqual(fd, f.all())
        self.assertEqual(f._FileStorage__objects, fd)
        self.assertIs(fd, f._FileStorage__objects)

    def test_new(self):
        """Tests the instance method of new"""
        f = FileStorage()
        fd = f.all()
        n = User()
        n.id = 1234
        n.name = "Nick"
        f.new(n)
        k = n.__class__.__name__ + "." + str(n.id)
        self.assertIsNotNone(fd[k])

    def test_file_path(self):
        f = FileStorage()
        fd = f.all()
        self.assertEqual(f._FileStorage__file_path, 'file.json')
        self.assertIsInstance(f._FileStorage__file_path, str)
        self.assertIsInstance(f._FileStorage__objects, dict)
        self.assertEqual(f._FileStorage__objects, fd)
        self.assertIsInstance(f, FileStorage)
