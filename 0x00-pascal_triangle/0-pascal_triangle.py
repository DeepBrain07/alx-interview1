#!/usr/bin/python3
def pascal_triangle(n):
    # check if n <= 0
    if n <= 0:
        return []

    LST = []
    lst = [0, 1, 0]
    LST.append([1])
    for _ in range(n - 1):
        new_lst = [0]
        for j in range(len(lst)):
            if j == len(lst) - 1:
                new_lst.append(lst[j])
                lst = new_lst
                LST.append(new_lst[1:-1])
            else:
                new_lst.append(lst[j] + lst[j+1])
    return LST
