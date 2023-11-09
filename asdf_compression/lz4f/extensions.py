import asdf

from asdf_compression._utils import _module_available

from .compressor import LZ4FrameCompressor


class LZ4FrameExtension(asdf.extension.Extension):
    extension_uri = "asdf://asdf-format.org/compression/extensions/lz4f-1.0.0"
    compressors = [LZ4FrameCompressor()]


def get_extensions():
    if _module_available("lz4"):
        return [LZ4FrameExtension()]
    return []
