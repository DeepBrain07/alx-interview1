#!/usr/bin/python3
""" This module defines a function that
    rotates a 2D nxn matrix
"""


def rotate_2d_matrix(matrix):
    """ This function rotates a 2D nxn matrix
    """
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list(x for x in range(len(matrix[i]))))

    ver_idx = -1
    for _list in matrix:
        hor_lst = _list
        counter = 0
        for lst in new_matrix:
            lst[ver_idx] = hor_lst[counter]
            counter += 1
        ver_idx -= 1
    for j in range(len(matrix)):
        for i in range(len(matrix)):
            matrix[j][i] = new_matrix[j][i]
