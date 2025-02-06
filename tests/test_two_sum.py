import config_override  # noqa
from unittest import mock
import unittest
from parameterized import parameterized
import contextlib
import io

from two_sum import *  # noqa


class TestTwoSum(unittest.TestCase):
    @parameterized.expand([([3, 4, 5, 6], 7, [0, 1]),
                           ([4, 5, 6], 10, [0, 2]),
                           ([5, 5], 10, [0, 1])])
    def test_script(self, *args):
        self.assertEqual(twoSum(*args[:-1]), args[-1])


if __name__ == '__main__':
    unittest.main(verbosity=3)
