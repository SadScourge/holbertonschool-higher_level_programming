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

    def __init__(self, size=0):
        """
        Initialize the square with a size and a position.

        Parameters:
        -----------
        size : int, optional
            The size of the square (default is 0).

        Raises:
        -------
        TypeError:
            If size is not an integer or position is not
            a tuple of 2 positive integers.
        ValueError:
            If size is negative.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
        --------
        int:
            The area of the square (size^2).
        """
        return self.__size ** 2
