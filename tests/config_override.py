import contextlib
import io
import pathlib
from unittest import mock
import sys
import os
import unittest

sys.path.append(os.path.dirname(
    os.path.realpath(__file__)) + "\\..\\main")  # noqa


# import __main__
# suite = unittest.TestLoader().loadTestsFromModule(__main__)
# buf = io.StringIO()
# # run the tests
# with contextlib.redirect_stdout(buf):
#     unittest.TextTestRunner(stream=buf).run(
#         suite)
