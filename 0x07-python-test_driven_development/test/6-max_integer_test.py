import unittest, sys
sys.path.append("..")
from 6-max_integer import max_integer

class TestMaxInteger(unitest.TestCase):

    def test_empty(self):
        self.assertEqual(max_integer([]), None)
