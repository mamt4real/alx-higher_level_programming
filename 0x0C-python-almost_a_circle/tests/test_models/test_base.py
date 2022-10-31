#!/usr/bin/python3

"""Defines Test Class for rectangle"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Testing a Base class"""

    def setUp(self):
        """Setup base cases"""
        Base.nb_objects = 0

    def test_default_init(self):
        """Test init method"""
        # test default id, x and y
        r1 = Base(10)
        r2 = Base()
        r3 = Base()
        self.assertEqual(r1.id, 10)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r3.id, r2.id + 1)


if __name__ == '__main__':
    unittest.main()
