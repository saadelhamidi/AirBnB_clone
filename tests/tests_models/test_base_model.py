#!/usr/bin/python3
"""
Unittest for BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Tests for BaseModel class.
    """

    def test_init(self):
        """
        Test initialization of BaseModel.
        """
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """
        Test the __str__ method of BaseModel.
        """
        model = BaseModel()
        self.assertEqual(str(model), f"[BaseModel] ({model.id}) {model.__dict__}")

    def test_save(self):
        """
        Test the save method of BaseModel.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], "BaseModel")
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()

