#!/usr/bin/python3
'''
Docstring for python-input_output.0-read_file
'''


def read_file(filename=""):
    '''
    Docstring for read_file
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
