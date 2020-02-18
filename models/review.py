#!/usr/bin/python3
'''review module'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Review of airbnb'''
    place_id = ""
    user_id = ""
    text = ""
