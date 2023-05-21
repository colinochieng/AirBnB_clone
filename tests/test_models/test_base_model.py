#!/usr/bin/python3
"""
Test BaseModel Class
"""
import unittest
import uuid
import re
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import os


class TestBaseModel(unittest.TestCase):
    """
    subdirectory of testcase
    """
    def setUp(self):
        """
        instantiate a new class
        """
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_init(self):
        """
        test if all init instances meet the required format
        """
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(len(self.my_model.id), 36)
        self.assertTrue(type(self.my_model.id) == str)

    def test_str(self):
        """
        test string representation
        """
        string = self.my_model.__str__()
        pattern = r'\[(\w+)\].+?\((.*?)\).+?({[^{}]*\})'
        regex = re.compile(pattern)
        match = regex.search(string)
        match = match.group()
        self.assertEqual(string, match)

    def test_save(self):
        """
        tests BaseModel.save()
        """
        search_key = f'{self.my_model.__class__.__name__}.{self.my_model.id}'
        file_s = os.path.getsize('file.json')
        self.my_model.save()
        self.assertIsNotNone(self.my_model.updated_at.isoformat())
        self.assertIn(search_key, storage._FileStorage__objects)
        self.assertTrue(os.path.isfile('file.json'))
        self.assertGreater(os.path.getsize('file.json'), file_s)
        with open('file.json', 'r', encoding='utf-8') as file:
            data = file.read()
            self.assertIn('"id": "{}"'.format(self.my_model.id), data)

    def test_to_dict(self):
        """
        test resturn value from to dict
        """
        my_di = self.my_model.to_dict()
        self.assertGreaterEqual(len(my_di), 4)
        self.assertEqual(type(my_di['updated_at']), str)
        self.assertEqual(type(my_di['updated_at']), str)
        self.assertIn('__class__', my_di)
        self.assertEqual(my_di['__class__'], self.my_model.__class__.__name__)

    def tearDown(self):
        """
        Delete the instance
        """
        search_key = f'{self.my_model.__class__.__name__}.{self.my_model.id}'
        del storage._FileStorage__objects[search_key]
        self.my_model.save()
        del self.my_model


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestBaseModel))
    runner = unittest.TextTestRunner
    runner.run(suite)
