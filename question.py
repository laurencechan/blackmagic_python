# coding=utf-8
import time


def search(sequence, num):
    if len(sequence) == 1:
         if sequence[0] == num:
             print 'search number %s success' % num
    else:
        middle = len(sequence) // 2
        if num > sequence[middle]:
            return search(sequence[middle:], num)
        else:
            return search(sequence[0:middle], num)



if __name__ == '__main__':
    search([1, 2, 3, 4, 5, 6], 5)
    pass
