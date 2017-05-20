# coding=utf-8

import os

def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print sChildPath

def fib(n):
    """

    :rtype: object
    :param n: 
    :return: 
    """
    if n<=2:
        return 1
    else:
        return  fib(n-1)+fib(n-2)



if __name__ == '__main__':
    # print_directory_contents("f:/")
    aa = fib(20)
    print aa
    pass