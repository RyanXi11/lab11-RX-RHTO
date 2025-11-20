import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5, 10), 15)
        self.assertEqual(add(-5, 10), 5)
        self.assertEqual(add(-5, 0), -5)


    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(10, -5), 15)

    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0, 10,), 0)
        self.assertEqual(mul(10, 10,), 100)
        self.assertEqual(mul(1, 5), 5)

    def test_divide(self): # 3 assertions
        self.assertRaises(ZeroDivisionError, div, 0, 10)
        self.assertEqual(div(10, 10,), 1)
        self.assertEqual(div(10, 0), 0)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(ZeroDivisionError, div(0, 5))

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in
        self.assertRaises(ValueError, log, 5, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hyp(5, 12), 13)
        self.assertEqual(hyp(3, 4, ), 5)
        self.assertEqual(hyp(6, 8,), 10)



    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
        self.assertRaises(ValueError,square_root, -10)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)

# Do not touch this
if __name__ == "__main__":
    unittest.main()