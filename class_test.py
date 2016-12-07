# coding=utf-8

class A():
    def func(self):
        print 'i am instance method'

    @staticmethod
    def func_static():
        print 'i am staticmethod'

    @classmethod
    def func_class(cls):
        print 'i am classmethod'


class B(A):
    def func(self, str_1):
        print '我是子类的func方法%s' % str_1


class Person():
    """"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class AA:
    w = 10

    def __init__(self):
        self.x = 11
        self.y = 12

    def add(self):
        return self.x + self.y


if __name__ == '__main__':
    a = AA()
    print a.add()
    AA.w = 20
    a.w = 13
    print AA.w, a.w
    a.t = 14
    a.q = 15
    print

    # person = Person("Laurence", "Chan")
    # print person.full_name
    # print person.first_name
    # print person.last_name

    # ryan = A()
    # laurence = B()
    # ryan.func()
    # ryan.func_static()
    # ryan.func_class()
    # # A.func()
    # print '-----------------------'
    # A.func_static()
    # A.func_class()
    # print '-----------------------'
    # laurence.func('lalala')

    pass
