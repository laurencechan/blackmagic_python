# coding=utf-8

class testsetandget:
    kk = {}
    def __getitem__(self, key):
        return self.kk[key]
    def __setitem__(self, key, value):
        self.kk[key] = value

if __name__ == '__main__':
    a = testsetandget()
    a['first'] = 1
    print a['first']
    pass
