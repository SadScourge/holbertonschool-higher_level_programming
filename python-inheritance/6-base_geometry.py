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
