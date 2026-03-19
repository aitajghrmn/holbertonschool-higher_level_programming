#!/usr/bin/python3
'''
10-square module with class Square
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Square class that inherits from Rectangle
    '''
    def __init__(self, size):
        self.__size = self.integer_validator('size', size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
