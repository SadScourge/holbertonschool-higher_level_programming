#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    -----------
    number_of_instances : int
        Class variable to count the number of Rectangle instances.
    print_symbol : str
        Symbol used for string representation of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1
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
            A string representation of the rectangle using the print_symbol.
            If width or height is 0, return an empty string.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        string = ""
        for indexI in range(self.__height):
            string += str(self.print_symbol) * self.__width
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

    def __del__(self):
        """
        Destructor method to decrease instance count and print a message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with the larger area.

        Parameters:
        -----------
        rect_1 : Rectangle
            The first rectangle.
        rect_2 : Rectangle
            The second rectangle.

        Returns:
        --------
        Rectangle:
            The rectangle with the larger or equal area.

        Raises:
        -------
        TypeError:
            If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new square (a rectangle with equal width and height).

        Parameters:
        -----------
        size : int, optional
            The size of the square's sides (default is 0).

        Returns:
        --------
        Rectangle:
            A new rectangle object with equal width and height.
        """
        return Rectangle(size, size)
