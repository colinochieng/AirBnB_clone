#!/usr/bin/python3
"""
Test State Class
"""
from models.state import State
from tests.test_models import test_base_model
import unittest


class TestState(test_base_model.TestBaseModel):
    """
    instantiate TestState
    """
    def setUp(self):
        self.my_model = State()
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
        self.assertIs(type(self.my_model.name), str)
        self.assertIsNotNone(self.my_model.name)

    def tearDown(self):
        return super().tearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestState))
    runner = unittest.TextTestRunner()
    runner.run(suite)
