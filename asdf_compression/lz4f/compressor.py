from asdf.extension import Compressor


class LZ4FrameCompressor(Compressor):
    label = b"lz4f"

    def compress(self, data, **kwargs):
        import lz4.frame

        yield lz4.frame.compress(data, **kwargs)

    def decompress(self, data, out, **kwargs):
        import lz4.frame

        decompressor = lz4.frame.LZ4FrameDecompressor(**kwargs)
        i = 0
        for block in data:
            decomp = decompressor.decompress(block)
            nbytes = len(decomp)
            # write all blocks of decompressed data contiguously into `out` array:
            out[i : i + nbytes] = decomp
            i += nbytes
        return i
