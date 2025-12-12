import asdf

from asdf_compression._utils import _module_available

from .compressor import Blosc2Compressor


class Blosc2Extension(asdf.extension.Extension):
    extension_uri = "asdf://asdf-format.org/compression/extensions/bls2-1.0.0"
    compressors = [Blosc2Compressor()]


def get_extensions():
    if _module_available("blosc2"):
        return [Blosc2Extension()]
    return []
