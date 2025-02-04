import config_override  # noqa
from unittest import mock
import unittest
from parameterized import parameterized
import contextlib
import io

from concatenation_of_array import *  # noqa


class TestConcatenationOfArray(unittest.TestCase):
    @parameterized.expand([([1, 2, 1], [1, 2, 1, 1, 2, 1]),
                           ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1])])
    def test_script(self, nums, verdict):
        self.assertEqual(getConcatenation(nums), verdict)


if __name__ == '__main__':
    unittest.main(verbosity=3)
