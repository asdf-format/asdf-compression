from asdf.extension import Compressor


class Blosc2Compressor(Compressor):
    label = b"bls2"

    def compress(self, data, **kwargs):
        import blosc2

        yield blosc2.compress(data, **kwargs)

    def decompress(self, data, out, **kwargs):
        import blosc2

        out[:] = blosc2.decompress(b"".join(data), **kwargs)
        return out.nbytes
