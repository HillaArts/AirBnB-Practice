#!/usr/bin/python3
"""
Test cases for BaseModel class.
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance_creation(self):
        """Test the creation of a BaseModel instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_method(self):
        """Test the __str__ method of BaseModel."""
        my_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        """Test the save method of BaseModel."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        expected_dict = {
            'id': my_model.id,
            'created_at': my_model.created_at.isoformat(),
            'updated_at': my_model.updated_at.isoformat(),
            'name': 'My First Model',
            'my_number': 89,
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(my_model.to_dict(), expected_dict)

    def test_from_dict_method(self):
        """Test the from_dict method of BaseModel."""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        my_model_dict = my_model.to_dict()
        new_model = BaseModel(**my_model_dict)

        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(new_model.id, my_model.id)
        self.assertEqual(new_model.created_at, my_model.created_at)
        self.assertEqual(new_model.updated_at, my_model.updated_at)
        self.assertEqual(new_model.name, my_model.name)
        self.assertEqual(new_model.my_number, my_model.my_number)
        self.assertEqual(new_model.__class__.__name__, 'BaseModel')


if __name__ == "__main__":
    unittest.main()

