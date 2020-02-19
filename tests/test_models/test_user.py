#!/usr/bin/python3
'''user unittests'''
from models.user import User

def testuser1(self):
    newuser = User()
    self.assertEqual(newuser.password = '')
    self.assertEqual(newuser.first_name = '')
    self.assertEqual(newuser.last_name = '')
    self.assertEqual(newuser.email = '')

def testuser2(self):
    user2 = User(
        first_name = 'Air'
        last_name = 'BnB'
        password = 'airbnb'
        email = 'airbnb@gmail.com')
    self.assertEqual(user2.first_name = 'Air')
    self.assertEqual(user2.last_name = 'BnB')
    self.assertEqual(user2.password = 'airbnb')
    self.assertEqual(user2.email = 'airbnb@gmail.com')

def testuser3(self):
    user3 = User(
        first_name = 'Air'
        last_name = 'BnB'
        password = 'airbnb'
        email = 'airbnb@gmail.com')
    user33 = User(
        first_name = 'Air')
    self.assertIn('first_name', self.user3.__dict__.keys())
    self.assertIn('last_name', self.user3.__dict__.keys())
    self.assertIn('password', self.user3.__dict__.keys())
    self.assertIn('email', self.user3.__dict__.keys())
    self.assertNotIn('last_name', self.user33.__dict__.keys())
    self.assertNotIn('password', self.user33.__dict__.keys())
    self.assertNotIn('email', self.user33.__dict__.keys())
