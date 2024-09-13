#!/usr/bin/python3
def max_integer(my_list=[]):
    result = 0
    if len(my_list) == 0:
        return None
    for index in range(len(my_list)):
        if my_list[index] > result:
            result = my_list[index]
    return result
