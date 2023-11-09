from . import blsc
from . import lz4
from . import zstd


def get_extensions():
    return blsc.get_extensions() + lz4.get_extensions() + zstd.get_extensions()
