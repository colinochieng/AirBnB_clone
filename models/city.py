#!/usr/bin/python3
"""Defines Class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines User City"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
