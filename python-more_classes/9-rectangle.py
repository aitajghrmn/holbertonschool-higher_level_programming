#!/usr/bin/python3
"""
Module with Rectangle Class
"""


class Rectangle:
    """
    Rectangle class
    """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
        mystr = ''
        if self.__width == 0 or self.__height == 0:
            return mystr
        for _ in range(self.__height):
            mystr += str(self.print_symbol) * self.__width
            if _ == self.__height - 1:
                break
            mystr += '\n'
        return mystr

    def __repr__(self):
        '''
        repr of instance
        '''
        width = str(self.__width)
        height = str(self.__height)
        mystr = "Rectangle(" + width + ", " + height + ")"
        return mystr

    def __del__(self):
        '''
        method that prints message when deleting an instance
        '''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        static method for comparing two instances
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        '''
        class method that creates square
        '''
        return Rectangle(size, size)
