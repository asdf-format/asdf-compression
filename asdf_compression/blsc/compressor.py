from asdf.extension import Compressor


class BloscCompressor(Compressor):
    label = b"blsc"

    def compress(self, data, **kwargs):
        import blosc

        yield blosc.compress(data, **kwargs)

    def decompress(self, data, out, **kwargs):
        import blosc

        out[:] = blosc.decompress(b"".join(data), **kwargs)
        return out.nbytes
