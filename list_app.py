# coding=utf-8

class A(object):
    def go(self):
        print "go A go!"

    def stop(self):
        print "stop A stop!"

    def pause(self):
        raise Exception("Not Implemented")


class B(A):
    def go(self):
        super(B, self).go()
        print "go BB go!"


class C(A):
    def go(self):
        super(C, self).go()
        print "go C go!"

    def stop(self):
        super(C, self).stop()
        print "stop C stop!"


class D(C, B):
    def go(self):
        super(D, self).go()
        print "go D go!"

    def stop(self):
        super(D, self).stop()
        print "stop D stop!"

    def pause(self):
        print "wait D wait!"


class E(B, C):
    pass
a = A()
b = B()
c = C()
d = D()
e = E()


def addx(x):
    def adder(y):
        return x + y
    return adder

def foo():
    m = 0
    def foo1():
        m =1
        print m
    print m
    foo1()
    print m

if __name__ == '__main__':
    foo()
    # c = addx(8)
    # print type(c)
    # print c.__name__
    # print c(10)
    # print "----"
    # a.go()
    # print "----"
    # b.go()
    # print "----"
    # c.go()
    # print "----"
    # d.go()
    # print "----"
    # e.go()
    # print "----"
    # a.stop()
    # print "----"
    # b.stop()
    # print "----"
    # c.stop()
    # print "----"
    # d.stop()
    # print "----"
    # e.stop()
    # print "----"
    # a.pause()
    # print "----"
    # b.pause()
    # print "----"
    # c.pause()
    # print "----"
    # d.pause()
    # print "----"
    # e.pause()
    # print "----"


    pass
