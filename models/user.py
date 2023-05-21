#!/usr/bin/python3
"""
A module for class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class Defining User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
