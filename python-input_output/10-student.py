#!/usr/bin/python3
'''
Docstring for python-input_output.9-student
'''


class Student:
    '''
    Docstring for Student
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            if len(attrs) == 0:
                return {}
            return {key: self.__dict__[key] for key in
                    attrs if key in self.__dict__}
        return self.__dict__
