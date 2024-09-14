import unittest

from crypto_api.math_lib.multiplicative_group import MultiplicativeGroup


class MultiplicativeGroupTests(unittest.TestCase):
    TEST_PRIME = 7

    def setUp(self):
        self.group = MultiplicativeGroup(MultiplicativeGroupTests.TEST_PRIME)

    def test_valid_initialization(self):
        self.assertEqual(MultiplicativeGroupTests.TEST_PRIME, self.group.modulo)
        self.assertEqual(6, self.group.order)

    def test_valid_mul_mod(self):
        self.assertEqual(5, self.group.mul_mod(3, 4))
        self.assertEqual(1, self.group.mul_mod(6, 6))
        self.assertEqual(0, self.group.mul_mod(2, 7))
        self.assertEqual(2, self.group.mul_mod(10, 3))
        self.assertEqual(2, self.group.mul_mod(5, 6))
        self.assertEqual(1, self.group.mul_mod(3, 5))

    def test_valid_pow_mod(self):
        self.assertEqual(1, self.group.pow_mod(2, 3))
        self.assertEqual(2, self.group.pow_mod(3, 2))
        self.assertEqual(1, self.group.pow_mod(5, 0))
        self.assertEqual(0, self.group.pow_mod(0, 5))
        self.assertEqual(2, self.group.pow_mod(2, 4))
        self.assertEqual(4, self.group.pow_mod(3, 4))

    def test_valid_mul_invert_mod(self):
        self.assertEqual(1, self.group.mul_invert_mod(1))
        self.assertEqual(4, self.group.mul_invert_mod(2))
        self.assertEqual(5, self.group.mul_invert_mod(3))
        self.assertEqual(2, self.group.mul_invert_mod(11))
        self.assertEqual(3, self.group.mul_invert_mod(12))
        self.assertEqual(6, self.group.mul_invert_mod(13))

    def test_valid_wrapping(self):
        self.assertEqual(4, self.group.wrapping(12345))
        self.assertEqual(3, self.group.wrapping(-12345))
        self.assertEqual(3, self.group.wrapping(3))
        self.assertEqual(0, self.group.wrapping(7))
        self.assertEqual(4, self.group.wrapping(-3))
        self.assertEqual(1, self.group.wrapping(-13))

    def test_valid_random_element(self):
        for _ in range(100):
            random_element = self.group.random_element()
            self.assertGreaterEqual(random_element, 0)
            self.assertLess(random_element, self.group.modulo)


if __name__ == '__main__':
    unittest.main()
