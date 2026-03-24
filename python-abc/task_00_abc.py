#!/usr/bin/python3
'''
00_abc module with abstract class Animal
'''

from abc import ABC, abstractmethod


class Animal(ABC):
    '''
    Abstact class Animal
    '''
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    '''
    Dog class that inherits from Animal ABC
    '''
    def sound(self):
        return "Bark"

class Cat(Animal):
    '''
    Cat class that inherits from Animal ABC
    '''
    def sound(self):
        return "Meow"
