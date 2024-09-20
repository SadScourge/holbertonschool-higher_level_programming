#!/usr/bin/python3
"""
This module defines a Square class that models a square.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
    -----------
    __size : int
        The size of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a size and a position.

        Parameters:
        -----------
        size : int, optional
            The size of the square (default is 0).
        """
        self.__size = size
