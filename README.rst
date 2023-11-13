ASDF support for various compression algorithms
-----------------------------------------------

.. image:: https://github.com/asdf-format/asdf-compression/workflows/CI/badge.svg
    :target: https://github.com/asdf-format/asdf-compression/actions
    :alt: CI Status

This packages includes a plugin for the Python library
`asdf <https://asdf.readthedocs.io/en/latest/>`__ to add support
for reading and writing various compression algorithms including:

* `Blosc <https://www.blosc.org/python-blosc/reference.html>`__
* `LZ4 Frame <https://python-lz4.readthedocs.io/en/stable/lz4.frame.html>`__
* `Zstandard <http://facebook.github.io/zstd/>`__


Installation
------------

This plugin is not yet stable and released on PyPi.

To install all compression algorithms supported by asdf-compression, install
using the ``all`` optional parameters.

.. code-block:: console

    $ pip install "asdf-compression[all] @ git+https://github.com/asdf-format/asdf-compression"

Or alternatively by cloning and installing this repository.

.. code-block:: console

    $ git clone https://github.com/asdf-format/asdf-compression
    $ cd asdf-compression
    $ pip install ".[all]"

If only a specific algorithm is needed, just that algorithm can be installed.

.. code-block:: console
    $ pip install ".[zstd]"

Or a subset can be selected

.. code-block:: console
    $ pip install ".[zstd,blsc]"

Usage
-----

When installed ``asdf-compression`` will register any supported and available
compression algorithms with asdf using the
`Compressor <https://asdf.readthedocs.io/en/latest/asdf/extending/compressors.html>`__
interface.

The following example shows saving an array with ``zstandard`` compression provided
via ``asdf-compression``.

.. code-block:: python

    import asdf, numpy as np

    af = asdf.AsdfFile({"arr": np.arange(42)})
    af.set_array_compression(af["arr"], "zstd")
    af.write_to("test.asdf")


Testing
-------

`pytest <https://docs.pytest.org>`__ is used for testing.
Tests can be run (from the source checkout of this repository):

.. code-block:: console

    $ pytest


Contributing
------------

We welcome feedback and contributions to this project.
