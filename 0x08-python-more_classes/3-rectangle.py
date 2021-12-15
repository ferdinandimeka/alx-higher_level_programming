#!/usr/bin/python3
"""
a python code the defines a class rectangle
"""


class Rectangle:
    """
    initializing the rectangle attributes
    args: width=0, height=0
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """setting the width attribute"""
    @property
    def width(self):
        """property setter returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width if value > 0"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """setting the height attributes"""
    @property
    def height(self):
        """this property returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height if the value is > 0"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returning the area"""
        return self.__width * self.__height

    def perimeter(self):
        """getting the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns rectangle with #'s"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            r = "\n".join(["#"*self.width for rows in range(self.height)])
            return r
