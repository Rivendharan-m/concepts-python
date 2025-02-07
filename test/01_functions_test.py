import unittest 
import pytest

from helper.helper_function import HelperFunction   

def test_user_sum():
    assert HelperFunction.user_sum(2, 3) == 5
    assert HelperFunction.user_sum(2.5, 3.5) == 6
    assert HelperFunction.user_sum(-2, -3) == 5
    
def test_mulitply():
    assert HelperFunction.user_multiply(2, 3) == 6
    assert HelperFunction.user_multiply(5, -10) == -50

def test_bad_type():
    with pytest.raises(TypeError):
        HelperFunction.user_sum("a", 2)
        HelperFunction.user_multiply("a", "b")


class TestFunctions(unittest.TestCase):
    """
    Class : Contains the test function based on unittest.TestCase syntax
    info: Class structure is required for unittest based test function
    """
    
    def test_user_sum_unittest_syntax(self):
        self.assertEqual(HelperFunction.user_sum(2, 3), 5)
        self.assertEqual(HelperFunction.user_sum(2.5, 3.5), 6)
        self.assertEqual(HelperFunction.user_sum(-2, -3), 5)
        
    def test_user_multiply_unittest_syntax(self):
        self.assertEqual(HelperFunction.user_multiply(2, 3), 6)
        self.assertEqual(HelperFunction.user_multiply(5, -10), -50)
    
    def test_bad_data_type_unittest_syntax(self):
        with self.assertRaises(TypeError):
            HelperFunction.user_sum('a', 2)
            HelperFunction.user_multiply('ab', 'a')