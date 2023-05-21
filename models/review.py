#!/usr/bin/python3
"""Defines Class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """defines User Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
