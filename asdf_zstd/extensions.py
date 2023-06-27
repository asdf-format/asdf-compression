import asdf

from .compression import ZstdCompressor


class ZstdExtension(asdf.extension.Extension):
    extension_uri = "asdf://stsci.edu/example-project/tags/zstd-1.0.0"
    compressors = [ZstdCompressor()]


def get_extensions():
    return [ZstdExtension()]
