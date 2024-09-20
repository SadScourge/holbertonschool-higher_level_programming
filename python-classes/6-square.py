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
    __position : tuple
        The position of the square when printed.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a size and a position.

        Parameters:
        -----------
        size : int, optional
            The size of the square (default is 0).
        position : tuple, optional
            The position (x, y) where the square will
            be printed (default is (0, 0)).

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
        if type(position) is not tuple or len(position) != 2\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Getter for the position of the square.

        Returns:
        --------
        tuple:
            The position (x, y) of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square with validation.

        Parameters:
        -----------
        value : tuple
            The new position (x, y) of the square.

        Raises:
        -------
        TypeError:
            If position is not a tuple of 2 positive integers.
        """
        if type(value) is not tuple or len(value) != 2\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Print the square using the character '#'
        according to its size and position.

        If the size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical space (position[1] indicates the number of newlines)
        for indexIV in range(self.__position[1]):
            print()

        # Print each row of the square
        for indexI in range(self.__size):
            # Print horizontal space (position[0] indicates leading spaces)
            for indexII in range(self.__position[0]):
                print(" ", end="")
            # Print the square row
            for indexIII in range(self.__size):
                print("#", end="")
            print()
