#!/usr/bin/python3
"""
This module defines a single function `is_same_class`.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Parameters:
    -----------
    obj : any type
        The object to be checked.
    a_class : type
        The class to check against.

    Returns:
    --------
    bool:
        True if the object is exactly an
        instance of `a_class`, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
