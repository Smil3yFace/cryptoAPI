import unittest

from crypto_api.math_lib.misc import *


class TestModuleFunctions(unittest.TestCase):

    def test_factors(self):
        self.assertEqual([2, 2, 2], factors(8))
        self.assertEqual([2, 3, 5], factors(30))
        self.assertEqual([3, 3], factors(9))
        self.assertEqual([5], factors(5))
        self.assertEqual([7, 7], factors(49))
        self.assertEqual([11, 13], factors(143))

    def test_ext_factors(self):
        self.assertEqual(([2], [3]), ext_factors(8))
        self.assertEqual(([2, 3, 5], [1, 1, 1]), ext_factors(30))
        self.assertEqual(([3], [2]), ext_factors(9))
        self.assertEqual(([5], [1]), ext_factors(5))
        self.assertEqual(([7], [2]), ext_factors(49))
        self.assertEqual(([11, 13], [1, 1]), ext_factors(143))

    def test_valid_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(29))

    def test_invalid_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(18))
        self.assertFalse(is_prime(22))

    def test_valid_gen_prime(self):
        self.assertIn(gen_prime(2, 10), [2, 3, 5, 7])
        self.assertIn(gen_prime(10, 20), [11, 13, 17, 19])
        self.assertIn(gen_prime(20, 30), [23, 29])
        self.assertIn(gen_prime(20, 30), [23, 29])
        self.assertIn(gen_prime(20, 30), [23, 29])
        self.assertIn(gen_prime(20, 30), [23, 29])

    def test_invalid_gen_prime(self):
        # No primes in this range
        self.assertRaises(IndexError, gen_prime, 32, 35)

    def test_valid_is_generator_simple(self):
        self.assertTrue(is_generator_simple(2, 7))
        self.assertTrue(is_generator_simple(5, 11))


    def test_invalid_is_generator_simple(self):
        self.assertFalse(is_generator_simple(2, 4))
        self.assertFalse(is_generator_simple(3, 9))
        self.assertFalse(is_generator_simple(7, 15))
        self.assertFalse(is_generator_simple(11, 20))

    def test_phi(self):
        self.assertEqual(1, phi(([2], [1])))
        self.assertEqual(2, phi(([2, 3], [1, 1])))
        self.assertEqual(16, phi(([2, 5], [3, 1])))
        self.assertEqual(8, phi(([2, 3], [3, 1])))
        self.assertEqual(64, phi(([2, 3, 5], [4, 1, 1])))
        self.assertEqual(12, phi(([2, 3, 7], [1, 1, 1])))