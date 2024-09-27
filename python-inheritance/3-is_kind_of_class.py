#!/usr/bin/python3
"""
This module defines a single function `is_kind_of_class`.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if
    the object is an instance of a class
    that inherited from, the specified class.

    Parameters:
    -----------
    obj : any type
        The object to be checked.
    a_class : type
        The class to check against.

    Returns:
    --------
    bool:
        True if the object is an instance of the class or
        a class that inherited from `a_class`.
        False otherwise.
    """
    return isinstance(obj, a_class)
