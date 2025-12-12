from . import blsc
from . import bls2
from . import lz4f
from . import zstd


def get_extensions():
    return blsc.get_extensions() + bls2.get_extensions() + lz4f.get_extensions() + zstd.get_extensions()
