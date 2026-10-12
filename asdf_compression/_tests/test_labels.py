"""Mostly copied from `asdf/asdf/_tests/test_compression.py`"""

import io
import os

import asdf
import numpy as np
import pytest
from asdf._tests import _helpers as helpers
from asdf.generic_io import OutputStream

RNG = np.random.default_rng(0)  # init random number generator with seed 0


def _get_large_tree():
    x = RNG.normal(size=(128, 128))
    return {"science_data": x}


def _roundtrip(tmp_path, tree, compression=None, write_options=None, read_options=None):
    read_options = {} if read_options is None else read_options
    write_options = {} if write_options is None else write_options.copy()
    write_options.update(all_array_compression=compression)

    tmpfile = os.path.join(str(tmp_path), "test.asdf")

    ff = asdf.AsdfFile(tree)
    ff.write_to(tmpfile, **write_options)

    with asdf.open(tmpfile, mode="rw") as ff:
        ff.update(**write_options)

    with asdf.open(tmpfile, **read_options) as ff:
        helpers.assert_tree_match(tree, ff.tree)

    # Also test saving to a buffer
    buff = io.BytesIO()

    ff = asdf.AsdfFile(tree)
    ff.write_to(buff, **write_options)

    buff.seek(0)
    with asdf.open(buff, **read_options) as ff:
        helpers.assert_tree_match(tree, ff.tree)

    # Test saving to a non-seekable buffer
    buff = io.BytesIO()

    ff = asdf.AsdfFile(tree)
    ff.write_to(OutputStream(buff), **write_options)

    buff.seek(0)
    with asdf.open(buff, **read_options) as ff:
        helpers.assert_tree_match(tree, ff.tree)

    return tmpfile


@pytest.mark.parametrize("label", ["blsc", "lz4f", "zstd", "bls2"])
def test_label(tmp_path, label):
    tree = _get_large_tree()
    _roundtrip(tmp_path, tree, label)
