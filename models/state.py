#!/usr/bin/python3
"""Defines Class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """defines User State"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
