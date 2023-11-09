import asdf

from asdf_compression._utils import _module_available

from .compressor import ZstdCompressor


class ZstdExtension(asdf.extension.Extension):
    extension_uri = "asdf://asdf-format.org/compression/extensions/zstd-1.0.0"
    compressors = [ZstdCompressor()]


def get_extensions():
    if _module_available("zstandard"):
        return [ZstdExtension()]
    return []
