#!/usr/bin/python3
""" This module defines a lockbox function """


def canUnlockAll(boxes):
    """ This function determines if all the boxes can be opened """
    lst = []
    # append the indexes of each element to 'lst'
    for b in range(1, len(boxes) + 1):
        lst.append(b)
    # check if each element is present in the list
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            if boxes[i][j] in lst:
                lst.remove(boxes[i][j])

    if lst == []:
        return True
    return False
