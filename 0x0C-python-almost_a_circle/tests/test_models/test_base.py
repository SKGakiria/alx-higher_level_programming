#!/usr/bin/python3
"""
The models/base.py
Defines unittest for the Base class.
"""
import unittest
import os
from models import base
from models.base import Base
from models. rectangle import Rectangle


class TestBase_instantiation(unittest.TestCase):
    """Tests instantiation of the Base class."""

    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b1.id, b3.id - 2)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_id_public(self):
        b = Base(12)
        b.id = 16
        self.assertEqual(16, b.id)

    def test_dict_id(self):
        self.assertEqual({1: "a", 2: "b"}, Base({1: "a", 2: "b"}).id)

    def test_str_id(self):
        self.assertEqual("String", Base("String").id)

    def test_float_id(self):
        self.assertEqual(4.5, Base(4.5).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3, 4}, Base({1, 2, 3, 4}).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3, 4], Base([1, 2, 3, 4]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2, 3, 4), Base((1, 2, 3, 4)).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
