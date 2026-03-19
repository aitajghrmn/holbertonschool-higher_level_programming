#!/usr/bin/python3
'''
module with function is_same_class
'''


def is_same_class(obj, a_class):
    '''
    is_same_class function returns true if object is instance of given class
    '''
    if type(obj) is a_class:
        return True
    return False
