#!/usr/bin/python3
'''
module with class MyList
'''


class MyList(list):
    '''
    MyList class that inherits from list
    '''
    def print_sorted(self):
        copy = self.copy()
        copy.sort()
        print(copy)
