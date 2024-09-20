#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    A class to represent a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle with width and height.

        Parameters:
        -----------
        width : int, optional
            The width of the rectangle (default is 0).
        height : int, optional
            The height of the rectangle (default is 0).

        Raises:
        -------
        TypeError:
            If width or height is not an integer.
        ValueError:
            If width or height is negative.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
        --------
        int:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Parameters:
        -----------
        value : int
            The new width of the rectangle.

        Raises:
        -------
        TypeError:
            If the width is not an integer.
        ValueError:
            If the width is negative.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
        --------
        int:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Parameters:
        -----------
        value : int
            The new height of the rectangle.

        Raises:
        -------
        TypeError:
            If the height is not an integer.
        ValueError:
            If the height is negative.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        --------
        int:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
        --------
        int:
            The perimeter of the rectangle, or 0 if either width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        --------
        str:
            A string representation of the rectangle using #.
            If width or height is 0, return an empty string.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        string = ""
        for indexI in range(self.__height):
            string += "#" * self.__width
            if indexI != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """
        Return a formal string representation of the rectangle.

        Returns:
        --------
        str:
            A string that can recreate the rectangle using its dimensions.
        """
        return f"Rectangle({self.__width}, {self.__height})"
