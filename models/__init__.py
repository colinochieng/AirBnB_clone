#!/usr/bin/python3
"""Module for Unique instance of file storage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
