import unittest

from crypto_api.math_lib.additive_group import AdditiveGroup


class AdditiveGroupTests(unittest.TestCase):
    TEST_PRIME = 7


    def setUp(self):
        self.group = AdditiveGroup(AdditiveGroupTests.TEST_PRIME)

    def test_valid_add_mod(self):
        self.assertEqual(5, self.group.add_mod(3, 2))
        self.assertEqual(6, self.group.add_mod(3, 3))
        self.assertEqual(0, self.group.add_mod(7, 0))
        self.assertEqual(4, self.group.add_mod(5, 6))
        self.assertEqual(5, self.group.add_mod(5, 7))
        self.assertEqual(2, self.group.add_mod(-6, 8))

    def test_valid_additive_inverse(self):
        self.assertEqual(4, self.group.additive_inverse(3))
        self.assertEqual(3, self.group.additive_inverse(4))
        self.assertEqual(0, self.group.additive_inverse(0))
        self.assertEqual(6, self.group.additive_inverse(1))
        self.assertEqual(2, self.group.additive_inverse(5))
        self.assertEqual(1, self.group.additive_inverse(6))

    def test_valid_sub_mod(self):
        self.assertEqual(1, self.group.sub_mod(3, 2))
        self.assertEqual(0, self.group.sub_mod(3, 3))
        self.assertEqual(4, self.group.sub_mod(0, 3))
        self.assertEqual(6, self.group.sub_mod(5, 6))
        self.assertEqual(5, self.group.sub_mod(5, 7))
        self.assertEqual(4, self.group.sub_mod(8, 4))

    def test_valid_pow_mod(self):
        self.assertEqual(0, self.group.pow_mod(3, 0))
        self.assertEqual(3, self.group.pow_mod(3, 1))
        self.assertEqual(6, self.group.pow_mod(3, 2))
        self.assertEqual(2, self.group.pow_mod(3, 3))
        self.assertEqual(5, self.group.pow_mod(3, 4))
        self.assertEqual(0, self.group.pow_mod(3, 7))

if __name__ == '__main__':
    unittest.main()
