#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """ This function calculates the fewest number of operations
    needed to result in exactly n H characters in the file """
    def is_prime(num):
        """ This function checks if the argument is a prime number """
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def copy_paste(lst, counter):
        """ This function copies and pastes """
        lst += lst
        counter += 2
        return {'lst': lst, 'counter': counter}

    def paste(lst, lst2, counter):
        """ This function pastes """
        lst += lst2
        counter += 1
        return {'lst': lst, 'counter': counter}

    if (n < 3) and (n != 2):
        return 0
    elif is_prime(n):
        return n
    elif (n % 2 == 0) and n < 4:
        return 2
    else:
        if n % 2 == 0:
            lst = ['H', 'H', 'H', 'H']
            lst2 = ['H', 'H']
            counter = 4
        else:
            lst = ['H', 'H', 'H']
            lst2 = ['H']
            counter = 3

        while True:
            if len(lst) == n:
                return counter
            elif len(lst) > n:
                return counter
            if (len(lst + lst) <= n) and (n % len(lst + lst) == 0):
                values = copy_paste(lst, counter)
                lst2 = lst
                lst = values['lst']
                counter = values['counter']
            else:
                values = paste(lst, lst2, counter)
                lst = values['lst']
                counter = values['counter']
