#!/usr/bin/python3
"""
Test City Class
"""
from models.city import City
from tests.test_models import test_base_model
import unittest


class TestCity(test_base_model.TestBaseModel):
    """
    instantiate TestCity
    """
    def setUp(self):
        self.my_model = City()
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
        self.assertIs(type(self.my_model.state_id), str)

    def tearDown(self):
        return super().tearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestCity))
    runner = unittest.TextTestRunner
    runner.run(suite)
