import config_override  # noqa
from unittest import mock
import unittest
from parameterized import parameterized
import contextlib
import io

from contains_duplicate import *  # noqa


class TestContainsDuplicates(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestContainsDuplicates, self).__init__(*args, **kwargs)

    @parameterized.expand([([1, 2, 3, 3], True),
                           ([1, 2, 3, 4], False)])
    def test_script(self, nums, verdict):
        print("hello3", nums, verdict)
        assert hasDuplicate(nums) == verdict


if __name__ == '__main__':
    unittest.main(verbosity=3)
