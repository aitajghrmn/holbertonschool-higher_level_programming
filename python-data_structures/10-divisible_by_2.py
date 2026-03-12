#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    for i in my_list:
        bool_list.append(i % 2 == 0)
    return bool_list
