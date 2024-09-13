#!/usr/bin/python3
def max_integer(my_list=[]):
    result = 0
    if not my_list:
        return None
    for index in range(len(my_list)):
        if my_list[index] > result:
            result = my_list[index]
    return result
