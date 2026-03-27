#!/usr/bin/python3
'''
Docstring for python-serialization.task_00_basic_serialization
'''
import json


def serialize_and_save_to_file(data, filename):
    '''
    Docstring for serialize_and_save_to_file

    :param data: Description
    :param filename: Description
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(data))

def load_and_deserialize(filename):
    '''
    Docstring for load_and_deserialize

    :param filename: Description
    '''
    with open(filename, 'r') as f:
        return json.loads(f.read())
