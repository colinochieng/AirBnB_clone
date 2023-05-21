#!/usr/bin/python3
"""
Test Review Class
"""
from models.review import Review
from tests.test_models import test_base_model
import unittest


class TestReview(test_base_model.TestBaseModel):
    """
    instantiate TestReview
    """
    def setUp(self):
        self.my_model = Review()
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
        self.assertIs(type(self.my_model.place_id), str)
        self.assertIs(type(self.my_model.user_id), str)
        self.assertIs(type(self.my_model.text), str)

    def tearDown(self):
        return super().tearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestReview))
    runner = unittest.TextTestRunner()
    runner.run(suite)
