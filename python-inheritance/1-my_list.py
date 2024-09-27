#!/usr/bin/python3
"""
This module defines a class `MyList` that inherits from `list`.
"""


class MyList(list):
    """
    A subclass of the built-in list that adds
    a method to print the list sorted.
    """

    def __init__(self):
        """
        Initialize the MyList instance by calling
        the parent class `list` initializer.
        """
        super().__init__()

    def print_sorted(self):
        """
        Print the list in ascending sorted order
        without modifying the original list.
        """
        print(sorted(self))
