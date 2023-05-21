#!/usr/bin/python3
"""
Test Place Class
"""
from models.place import Place
from tests.test_models import test_base_model
import unittest


class TestPlace(test_base_model.TestBaseModel):
    """
    instantiate TestPlace
    """
    def setUp(self):
        self.my_model = Place()
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
        self.assertIs(type(self.my_model.city_id), str)
        self.assertIs(type(self.my_model.user_id), str)
        self.assertIs(type(self.my_model.name), str)
        self.assertIs(type(self.my_model.description), str)
        self.assertIs(type(self.my_model.number_rooms), int)
        self.assertIs(type(self.my_model.number_bathrooms), int)
        self.assertIs(type(self.my_model.max_guest), int)
        self.assertIs(type(self.my_model.price_by_night), int)
        self.assertIs(type(self.my_model.latitude), float)
        self.assertIs(type(self.my_model.longitude), float)
        self.assertIs(type(self.my_model.amenity_ids), list)

    def tearDown(self):
        return super().tearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestPlace))
    runner = unittest.TextTestRunner()
    runner.run(suite)
