import importlib


def _module_available(name):
    """
    Check that a module exists (but don't import it)

    Parameters
    ----------

    name : str
        Name of the module

    Returns
    -------

    exists : bool
        True if the module was found
    """
    return importlib.util.find_spec(name) is not None
