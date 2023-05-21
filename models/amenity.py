#!/usr/bin/python3
"""Defines Class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines User Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
