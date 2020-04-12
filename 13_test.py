import unittest

def compute_sum(val1, val2):
    return val1 + val2

def return_next_prev(val):
    return [val-1, val+1]

class TestSum(unittest.TestCase):

    def setUp(self):
        """Setup each test"""
        print("\nsetup test")

    def test_1(self):
        """First test point"""
        sum_1 = compute_sum(10, 5)
        self.assertEqual(sum_1, 15)
        self.assertNotEqual(sum_1, 25)
        sum_2 = compute_sum(5, 10)
        self.assertTrue(sum_1==sum_2)
        self.assertFalse(sum_1!=sum_2)

    def test_2(self):
        """Second test point"""
        l = return_next_prev(10)
        self.assertIn(9, l)
        self.assertIn(11, l)

unittest.main()

