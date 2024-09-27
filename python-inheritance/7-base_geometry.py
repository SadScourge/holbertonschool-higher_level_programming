#!/usr/bin/python3
"""
This module defines the BaseGeometry.
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
