import numpy as np

import struct

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


class LZ4BlockCompressor(Compressor):
    # eventually this should become `lz4` but currently asdf prevents
    # multiple extensions with the same label
    label = b"lz4b"

    def compress(self, data, **kwargs):
        import lz4.block

        kwargs["mode"] = kwargs.get("mode", "default")
        compression_block_size = kwargs.pop("compression_block_size", 1 << 22)

        nelem = compression_block_size // data.itemsize
        for i in range(0, len(data), nelem):
            _output = lz4.block.compress(data[i : i + nelem], **kwargs)
            header = struct.pack("!I", len(_output))
            yield header + _output

    def decompress(self, blocks, out, **kwargs):
        import lz4.block

        _size = 0
        _pos = 0
        _partial_len = b""
        _buffer = None
        bytesout = 0

        for block in blocks:
            cast = "c"
            blk = memoryview(block).cast(cast)  # don't copy on slice

            while len(blk):
                if not _size:
                    # Don't know the (compressed) length of this block yet
                    if len(_partial_len) + len(blk) < 4:
                        _partial_len += blk
                        break  # we've exhausted the block
                    if _partial_len:
                        # If we started to fill a len key, finish filling it
                        remaining = 4 - len(_partial_len)
                        if remaining:
                            _partial_len += blk[:remaining]
                            blk = blk[remaining:]
                        _size = struct.unpack("!I", _partial_len)[0]
                        _partial_len = b""
                    else:
                        # Otherwise just read the len key directly
                        _size = struct.unpack("!I", blk[:4])[0]
                        blk = blk[4:]

                if len(blk) < _size or _buffer is not None:
                    # If we have a partial block, or we're already filling a buffer, use the buffer
                    if _buffer is None:
                        _buffer = np.empty(
                            _size,
                            dtype=np.byte,
                        )  # use numpy instead of bytearray so we can avoid zero initialization
                        _pos = 0
                    newbytes = min(_size - _pos, len(blk))  # don't fill past the buffer len!
                    _buffer[_pos : _pos + newbytes] = np.frombuffer(blk[:newbytes], dtype=np.byte)
                    _pos += newbytes
                    blk = blk[newbytes:]

                    if _pos == _size:
                        _out = lz4.block.decompress(_buffer, return_bytearray=True, **kwargs)
                        out[bytesout : bytesout + len(_out)] = _out
                        bytesout += len(_out)
                        _buffer = None
                        _size = 0
                else:
                    # We have at least one full block
                    _out = lz4.block.decompress(memoryview(blk[:_size]), return_bytearray=True, **kwargs)
                    out[bytesout : bytesout + len(_out)] = _out
                    bytesout += len(_out)
                    blk = blk[_size:]
                    _size = 0

        return bytesout
