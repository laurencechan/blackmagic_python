# coding=utf-8
import functools
import time


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print 'calling decorated functionddddddddddddddddddddddddddddddd...'
        return func()
    return wrapper


@my_decorator
def example():
    """Docstrings"""
    print 'called example function'


if __name__ == '__main__':
    example()
    # print example.__name__, example.__doc__
