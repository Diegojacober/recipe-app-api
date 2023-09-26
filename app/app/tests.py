"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """test the calc module."""

    def test_add_number(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        
        self.assertEqual(res, 11)