#!/usr/bin/python3
"""
Module with Rectangle Class
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Init method with width height
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        method to calculate area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        method to calculate perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        '''
        str represtantion of rectangle
        '''
        str = ''
        if self.__width == 0 or self.__height == 0:
            return str
        for _ in range(self.__height):
            str += '#' * self.__width
            if _ == self.__height - 1:
                break
            str += '\n'
        return str

    def __repr__(self):
        '''
        repr of instance
        '''
        width = str(self.__width)
        height = str(self.__height)
        mystr = "Rectangle(" + width + ", " + height + ")"
        return mystr
