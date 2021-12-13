#!/usr/bin/python3
""" Module that defines a rectangle """


class Rectangle:
    def __init__ (self, width=0, height=0):
        """ initializes  the data for the rectangle """

        self.width = width
        self.height = height

    @property
    def height(self):
        """ Retrieves the width """
        return self.__height

    @property
    def width(self):
        """ Retrieves the height """
        return self.__width

    @width.setter
    def height(self, value):
        """ Defines the width of the rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @height.setter
    def width(self, value):
        """ Defines the height of the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value



