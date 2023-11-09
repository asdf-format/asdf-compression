import asdf

from asdf_compression._utils import _module_available

from .compressor import BloscCompressor


class BloscExtension(asdf.extension.Extension):
    extension_uri = "asdf://asdf-format.org/compression/extensions/blsc-1.0.0"
    compressors = [BloscCompressor()]


def get_extensions():
    if _module_available("blosc"):
        return [BloscExtension()]
    return []
