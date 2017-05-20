# coding=utf-8

class A(object):
    def __init__(self):
        print(self.__class__.__mro__)

    def bark(self):
        print("I'm A")
        super(A, self).bark()

class B(object):
    def bark(self):
        print("I'm B")


class C(A, B):
    def bark(self):
        print("I'm C")
        super(C, self).bark()


if __name__ == '__main__':
    c = C()
    c.bark()

