"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calculator


class CalculatorTest(SimpleTestCase):
    """ Test the calculator module """

    def test_add_numbers(self):
        """ Test adding two numbers """
        result = calculator.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract_numbers(self):
        """ Test subtracting two numbers """
        result = calculator.subtract(2, 1)
        self.assertEqual(result, 1)
