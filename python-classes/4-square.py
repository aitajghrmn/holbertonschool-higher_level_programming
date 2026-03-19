#!/usr/bin/python3
"""
Module with Square class
"""


class Square:
    """
    Square class that contains private size attribute
    """
    def __init__(self, size=0):
        """
        initilaize method
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns current square area
        """
        return self.__size * self.__size
