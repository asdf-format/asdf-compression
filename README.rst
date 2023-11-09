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

This plugin is not yet stable and released on PyPi

.. code-block:: console

    $ pip install git+https://github.com/braingram/asdf-compression

Or alternatively by cloning and installing this repository.

.. code-block:: console

    $ git clone https://github.com/braingram/asdf-compression
    $ cd asdf-compression
    $ pip install .


Usage
-----


Testing
-------

`pytest <https://docs.pytest.org>`__ is used for testing.
Tests can be run (from the source checkout of this repository):

.. code-block:: console

    $ pytest


Contributing
------------

We welcome feedback and contributions to this project.
