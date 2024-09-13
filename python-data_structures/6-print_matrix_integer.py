#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for index1 in range(len(matrix)):
        for index2 in range(len(matrix[0])):
            print("{}".format(matrix[index1][index2]), end="")
            if index2 != len(matrix[0]):
                print(" ", end="")
        if index1 != len(matrix):
            print("\n", end="")
