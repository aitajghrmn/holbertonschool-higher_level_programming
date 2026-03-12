#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if search == i:
            new_list.append(replace)
            continue
        new_list.append(i)
    return new_list
