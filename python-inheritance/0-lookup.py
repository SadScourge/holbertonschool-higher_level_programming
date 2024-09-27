#!/usr/bin/python3
"""
This module defines a single function `lookup`.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Parameters:
    -----------
    obj : any type
        The object to retrieve attributes and methods from.

    Returns:
    --------
    list:
        A list of strings representing the attributes
        and methods of the object.
    """
    return dir(obj)
