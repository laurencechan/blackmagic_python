# coding=utf-8

class Choice():
    def __init__(self):
        pass

    @staticmethod
    def chc():
        ipt = int(raw_input())
        return ipt

    @staticmethod
    def input():
        print "please make your choice:"
        ipt = Choice.chc()
        if ipt == 1:
            Choice.method1()
        elif ipt == 2:
            Choice.method2()
        else:
            Choice.method3()

    @staticmethod
    def method1():
        print "Processing task A!!"

    @staticmethod
    def method2():
        print "processing task B!!"

    @staticmethod
    def method3():
        print "processing task C!!"


if __name__ == '__main__':
    Choice.input()
    # Choice.method1()
    pass
