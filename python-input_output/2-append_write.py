#!/usr/bin/python3
'''
Docstring for python-input_output.2-append_write
'''


def append_write(filename="", text=""):
    '''
    Docstring for append_write

    :param filename: Description
    :param text: Description
    '''
    with open(filename, 'a', encoding='UTF-8') as f:
        f.write(text)
        return len(text)
