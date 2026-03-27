#!/usr/bin/python3
'''
Docstring for python-input_output.1-write_file
'''


def write_file(filename="", text=""):
    '''
    Docstring for write_file

    :param filename: Description
    :param text: Description
    '''
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(text)
        return len(text)
