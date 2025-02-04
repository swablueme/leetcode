import config_override  # noqa
from unittest import mock
import unittest
from parameterized import parameterized
import contextlib
import io

from climbing_stairs import *  # noqa
from deepdiff import DeepDiff


class TestingClimbingStairs(unittest.TestCase):
    @parameterized.expand([(2, [(2,), (1, 1)]),
                           (3, [(2, 1), (1, 2), (1, 1, 1)])])
    def test_script(self, nums, verdict):
        valueFound = DeepDiff(climbStairs(nums), verdict, ignore_order=True)
        self.assertEqual(valueFound, {})


if __name__ == '__main__':
    unittest.main(verbosity=3)
