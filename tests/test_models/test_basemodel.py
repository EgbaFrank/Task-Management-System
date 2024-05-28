#!/usr/bin/env python3
"""
This module contains the implementation basemodel testcases
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Test cases for the BaseModel"""

    def setUp(self):
        """Set up test environment"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def test_docstring(self):
        """Tests for doctstring"""
        self.assertIsNotNone(BaseModel.__module__.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)

    def test_init(self):
        """Test init success cases"""
        # Test cases for the ID attribute
        self.assertIsNotNone(self.base1.id)
        self.assertIsNotNone(self.base2.id)
        self.assertIsInstance(self.base1.id, str)
        self.assertNotEqual(self.base1.id, self.base2.id)

        # Test cases for the updated_at/created_at attributes
        self.assertIsNotNone(self.base1.created_at)
        self.assertIsNotNone(self.base2.created_at)
        self.assertIsNotNone(self.base1.updated_at)
        self.assertIsNotNone(self.base2.updated_at)
        self.assertIsInstance(self.base1.created_at, datetime)
        self.assertIsInstance(self.base2.updated_at, datetime)

    def test_update(self):
        # Test cases for instance re-creation
        dict_val = self.base2.to_dict()
        self.base3 = BaseModel(**dict_val)

        self.assertIsNotNone(self.base3.id)
        self.assertIsNotNone(self.base3.created_at)
        self.assertIsNotNone(self.base3.updated_at)
        self.assertNotEqual(self.base3.__class__, "BaseModel")
        self.assertIsInstance(self.base3.created_at, datetime)
        self.assertIsInstance(self.base3.updated_at, datetime)

    def test_empty_dict(self):
        # Test case for empty dict
        self.base4 = BaseModel(**{})

        self.assertIsNotNone(self.base4.id)
        self.assertIsNotNone(self.base4.created_at)
        self.assertIsNotNone(self.base4.updated_at)
        self.assertNotEqual(self.base4.__class__, "BaseModel")
        self.assertIsInstance(self.base4.created_at, datetime)
        self.assertIsInstance(self.base4.updated_at, datetime)

    def test_str(self):
        """Test the str speacial method"""
        exp_str = f"[BaseModel] ({self.base1.id}) {self.base1.__dict__}"
        self.assertEqual(str(self.base1), exp_str)

    def test_save(self):
        """Tests the save method"""
        before_save = self.base1.updated_at
        self.base1.save()

        self.assertNotEqual(before_save, self.base1.updated_at)
        self.assertGreater(self.base1.updated_at, before_save)

    def test_to_dict(self):
        """Test cases for the to_dict method"""
        isofmt1 = self.base1.created_at.isoformat()
        isofmt2 = self.base1.updated_at.isoformat()
        dict_return = self.base1.to_dict()

        self.assertIsInstance(dict_return, dict)

        self.assertIn("id", dict_return)
        self.assertIn("__class__", dict_return)
        self.assertIn("created_at", dict_return)
        self.assertIn("updated_at", dict_return)

        self.assertEqual(dict_return["created_at"], isofmt1)
        self.assertEqual(dict_return["updated_at"], isofmt2)
        self.assertIsInstance(dict_return["created_at"], str)
        self.assertIsInstance(dict_return["updated_at"], str)
        self.assertEqual(dict_return["__class__"], "BaseModel")
