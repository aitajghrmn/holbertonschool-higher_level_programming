#!/usr/bin/python3
'''
module with function inherits_from
'''


def inherits_from(obj, a_class):
    '''
    is_kind_of_class function returns true if object is instance of given class
    '''
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
