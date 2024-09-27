#!/usr/bin/python3
"""
This module defines the BaseGeometry, Rectangle, and Square classes.
"""


class BaseGeometry:
    """
    Base class for geometry objects.
    """

    def area(self):
        """
        Calculate the area of the geometry object.

        Raises:
        -------
        Exception:
            If the area method is not implemented in a derived class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Parameters:
        -----------
        name : str
            The name of the parameter being validated.
        value : int
            The value to validate.

        Raises:
        -------
        TypeError:
            If the value is not an integer.
        ValueError:
            If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class to represent a rectangle, inherits from BaseGeometry.

    Attributes:
    -----------
    __width : int
        The width of the rectangle.
    __height : int
        The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        Parameters:
        -----------
        width : int
            The width of the rectangle.
        height : int
            The height of the rectangle.

        Raises:
        -------
        TypeError, ValueError:
            If the width or height is invalid (checked by integer_validator).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
        --------
        str:
            The formatted string "[Rectangle] width/height".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        --------
        int:
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    A class to represent a square, inherits from Rectangle.

    Attributes:
    -----------
    __size : int
        The size of the square (equal width and height).
    """

    def __init__(self, size):
        """
        Initialize a square with the given size.

        Parameters:
        -----------
        size : int
            The size of the square.

        Raises:
        -------
        TypeError, ValueError:
            If the size is invalid (checked by integer_validator).
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
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

    def __str__(self):
        """
        Return the string representation of the square.

        Returns:
        --------
        str:
            The formatted string "[Square] size/size".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
