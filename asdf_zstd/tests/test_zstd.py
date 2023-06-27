from asdf.config import config_context
from asdf.testing.helpers import roundtrip_object
import numpy
import pytest


def test_zstd():
    arr = numpy.arange(42)
    with config_context() as cfg:
        cfg.all_array_compression = 'zstd'
        arr2 = roundtrip_object({'arr': arr})
        numpy.testing.assert_array_equal(arr2, arr)

