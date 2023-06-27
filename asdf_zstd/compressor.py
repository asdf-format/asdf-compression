from asdf.extension import Compressor


class ZstdCompressor(Compressor):
    label = 'zstd'

    def compress(self, data, **kwargs):
        import zstandard

        level = kwargs.get("level", 3)
        threads = kwargs.get("threads", -1)
        compressor = zstandard.ZstdCompressor(level=level, threads=threads)
        yield compressor.compress(data)

    def decompress(self, data, out, **kwargs):
        import zstandard

        decompressor = zstandard.ZstdDecompressor(**kwargs)
        dobj = decompressor.decompressobj()
        nbytes = 0
        for block in data:
            decomp = dobj.decompress(block)
            n = len(decomp)
            out[i : i + n] = decomp
            nbytes += n
        return nbytes
