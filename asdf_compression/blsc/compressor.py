from asdf.extension import Compressor


class BloscCompressor(Compressor):
    label = b"blsc"

    def compress(self, data, **kwargs):
        import blosc

        # Type size, necessary for shuffle filter efficiency
        # TODO: This should be the type size of the data actually stored, not just "byte" or "uint8"
        typesize = data.itemsize

        yield blosc.compress(data, typesize=typesize, **kwargs)

    def decompress(self, data, out, **kwargs):
        import blosc

        # TODO: call `self._api.decompress_ptr` instead to avoid copying the output
        out[:] = blosc.decompress(b"".join(data), **kwargs)
        return out.nbytes
