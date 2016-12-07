# coding=utf-8

import copy,datetime

L1 = [1, 2, [3, 4]]
L2 = copy.copy(L1)
print "第一步：\n", L1, '\n', L2
L2[2][0] = 50
print "第二步：\n", L1, '\n', L2

print "深度复制："
L1 = [1, 2, [3, 4]]
L2 = copy.deepcopy(L1)
print "第三步：\n", L1, '\n', L2
L2[2][0] = 50
print "第四步：\n", L1, '\n', L2


class CopyObj(object):
    def __repr__(self):
        return "CopyObj"

    def __str__(self):
        return "我是中国人"

    def __copy__(self):
        return "Hello"

t1 = datetime.datetime.now()

if __name__ == '__main__':
    obj = CopyObj()
    obj1 = copy.copy(obj)
    print CopyObj
    print obj
    print obj1
    print "%s" % obj
    print "%r" % obj
    print repr(t1)
    pass
