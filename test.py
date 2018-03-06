import unittest
from doublenumber import doubleNum

class TestAdder(unittest.TestCase):

	def	test_doubling_func(self):
		self.assertEqual(10, doubleNum(5))
