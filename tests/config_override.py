import contextlib
import io
import pathlib
from unittest import mock
import sys
import os
import unittest

[sys.path.append(x[0]) for x in os.walk(os.path.dirname(
    os.path.realpath(__file__)) + "\\..\\main")]

# sys.path.append(os.path.dirname(
#     os.path.realpath(__file__)) + "\\..")  # noqa
