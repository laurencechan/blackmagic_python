# coding=utf-8

#
class Testsetandget():
    def __init__(self):
        pass

    kk = {}
    def __getitem__(self, key):
        return self.kk[key]

    def __setitem__(self, key, value):
        self.kk[key] = value

    @staticmethod
    def func():
        print "Hello World"

def ams(x, y):
    print x * 2 + y


if __name__ == '__main__':
    # ams(3, 6)
    a = Testsetandget()
    # a.func()
    a['first'] = 1
    print a['first']
    pass
