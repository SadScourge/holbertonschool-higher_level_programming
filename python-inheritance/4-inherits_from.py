#!/usr/bin/python3
"""
This module defines a single function `inherits_from`.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class.

    Parameters:
    -----------
    obj : any type
        The object to be checked.
    a_class : type
        The class to check against.

    Returns:
    --------
    bool:
        True if the object is an instance of a
        class that inherited from `a_class`.
        False otherwise.

    Notes:
    ------
    The function excludes the `bool` class from inheritance checks.
    """
    if a_class != bool:
        return issubclass(type(obj), a_class)
