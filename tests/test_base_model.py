#!/usr/bin/python3
"""Unittest for Class BaseModel"""

import unittest
import json
from models import base_model
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Testing Class BaseModel"""

    def test_id(self):
        """Tests id"""
        a = BaseModel()
        self.assert
