#!/usr/bin/python3
'''unittest for review'''

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    '''tests review class'''

def test_empty(self):
    empty = Reivew()
    self.assertEqual(new.place_id, '')
    self.assertEqual(new.user_id, '')
    self.assertEqual(new.text, '')

def test_review(self):
    newreview = Review(place_id='Place',
                       user_id='User',
                       text='place text')
    self.assertEqual(newreview.place_id, 'Place')
    self.assertEqual(newreview.user_id, 'User')
    self.assertEqual(newreview.text, 'place text')
