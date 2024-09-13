#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    #   for index in range(len(my_list) - 1, -1, -1):
    for index in reversed(my_list):
        print("{:d}".format(index))
