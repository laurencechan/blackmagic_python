# coding=utf-8

from itertools import *

# count
# def count(start=0, step=1):
#     n = start
#     while True:
#         yield n
#         n += step
#
#
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
# g = count(10)
# for i in izip(count(1), ['a', 'b', 'c', 'd']):
#     print
# i = int(raw_input())
# while i:
#     if i == 1:
#         print 1
#     elif i == 2:
#         print 2
#     elif i == 3:
#         print 3
#     elif i == 99:
#         break

for i in range(10):
    if i == 5:
        continue
    print i


if __name__ == '__main__':
    pass

    # print count(10, 1).next()
    # print count(10, 1).next()
    # print count(10, 1).next()
    # print count(10, 1).next()
    # print count(10, 1).next()
    # print count(10, 1).next()
    # print count(10, 1).next()
    # print count(10, 1).next()

    # print fib(6)
    # pass
