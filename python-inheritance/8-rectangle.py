#!/usr/bin/python3
"""
This module defines the BaseGeometry and Rectangle.
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
