#!/usr/bin/python3
'''
Docstring for python-serialization.task_01_pickle
'''
import pickle


class CustomObject:
    '''
    Docstring for CustomObject
    '''
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            f.write(pickle.dumps(self))

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                return pickle.loads(f.read())
        except (FileNotFoundError, EOFError):
            return None
