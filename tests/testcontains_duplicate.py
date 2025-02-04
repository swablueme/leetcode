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

    @ parameterized.expand([([1, 2, 3, 3], True),
                           ([1, 2, 3, 4], False)])
    def test_script(self, nums, verdict):
        print("hello3", nums, verdict)
        assert hasDuplicate(nums) == verdict


if __name__ == '__main__':
    # # find all tests in this module
    # import __main__
    # suite = unittest.TestLoader().loadTestsFromModule(__main__)
    # with io.StringIO() as buf:
    #     # run the tests
    #     with contextlib.redirect_stdout(buf):
    #         unittest.TextTestRunner(stream=buf).run(suite)
    #     # process (in this case: print) the results
    #     print('*** CAPTURED TEXT***:\n%s' % buf.getvalue())
    unittest.main(verbosity=3)
