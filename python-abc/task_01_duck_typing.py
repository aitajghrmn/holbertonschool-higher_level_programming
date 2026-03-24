#!/usr/bin/python3
'''
01_duck_typing module
'''

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    '''
    abstract class Shape
    '''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    '''
    Circle class inherits from shape
    '''
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * pi
    
    def perimeter(self):
        return 2 * pi * abs(self.radius)


class Rectangle(Shape):
    '''
    Rectangle class that inherits from Shape
    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    area = obj.area()
    perimeter = obj.perimeter()
    print(f"Area: {area}\nPerimeter: {perimeter}")
