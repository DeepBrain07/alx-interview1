#!/usr/bin/python3
""" This module defines a lockbox function """


def canUnlockAll(boxes):
    """ This function determines if all the boxes can be opened """
    lockedBoxes = []
    for k in range(1, len(boxes)):
        lockedBoxes.append(k)
    unlockedKeys = boxes[0]
    keys = unlockedKeys
    for i in range(1, len(boxes)):
        for j in unlockedKeys:
            if j == i or j in lockedBoxes:
                lockedBoxes.remove(i)
                unlockedKeys = unlockedKeys + boxes[i]
                break
        keys = keys + boxes[i]
    if lockedBoxes == []:
        return True
    return False
