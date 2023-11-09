from . import blsc
from . import lz4f
from . import zstd


def get_extensions():
    return blsc.get_extensions() + lz4f.get_extensions() + zstd.get_extensions()
