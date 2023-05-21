#!/usr/bin/python3
"""
Test User Class
"""
from models.user import User
from tests.test_models import test_base_model
import unittest


class TestUser(test_base_model.TestBaseModel):
    """
    instantiate TestUser
    """
    def setUp(self):
        self.my_model = User()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_init(self):
        return super().test_init()

    def test_str(self):
        return super().test_str()

    def test_save(self):
        return super().test_save()

    def test_to_dict(self):
        return super().test_to_dict()

    def test_cls_att(self):
        """
        test if string
        """
        self.assertIs(type(self.my_model.email), str)
        self.assertIs(type(self.my_model.password), str)
        self.assertIs(type(self.my_model.first_name), str)
        self.assertIs(type(self.my_model.last_name), str)

    def tearDown(self):
        return super().tearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestUser))
    runner = unittest.TextTestRunner()
    runner.run(suite)
