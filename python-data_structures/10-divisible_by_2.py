#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = my_list.copy()
    for index in range(len(my_list)):
        if my_list[index] % 2 == 1:
            newList[index] = False
        else:
            newList[index] = True
    return newList
