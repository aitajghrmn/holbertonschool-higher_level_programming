#!/usr/bin/python3
'''
Docstring for python-input_output.7-add_item
'''
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists('add_item.json'):
    if os.path.getsize('add_item.json') > 0:
        my_list = load_from_json_file('add_item.json')
else:
    my_list = []

for elem in range(1, len(sys.argv)):
    my_list.append(sys.argv[elem])

save_to_json_file(my_list, 'add_item.json')
