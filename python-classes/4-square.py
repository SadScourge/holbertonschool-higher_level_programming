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

    @property
    def size(self):
        """
        Getter for the size of the square.

        Returns:
        --------
        int:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square with validation.

        Parameters:
        -----------
        value : int
            The new size of the square.

        Raises:
        -------
        TypeError:
            If value is not an integer.
        ValueError:
            If value is negative.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
