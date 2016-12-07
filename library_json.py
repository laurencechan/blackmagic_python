# coding=utf-8

import json

# obj = [[1, 2, 3], 123, 123.123, 'abc', {'key1': (1, 2, 3), 'key2': (4, 5, 6)}]
# encodedjson = json.dumps(obj)
#
# decodejson = json.loads(encodedjson)
#
data1 = {'b': 789, 'c': 456, 'a': 123}
data2 = {'a': 123, 'b': 789, 'c': 456}
data3 = {"a": 123, "c": 456, "b": 789}
d1 = json.dumps(data1, sort_keys=True, indent=True)
# d1_1 = json.dump(data1, fp=True)
d2 = json.dumps(data2)
d2_1 = json.dumps(data2, skipkeys=False)
d3 = json.dumps(data2, sort_keys=True)
#
# data = {'b': 789, 'c': 456, 'a': 123}
# print d1
# f = open('./tt.txt', 'a')

if __name__ == '__main__':
    # json.dump(encodedjson, f)
    # print 'DATA:', repr(data)
    # print 'repr(data)             :', len(repr(data))
    # print 'dumps(data)            :', len(json.dumps(data))
    # print 'dumps(data, indent=2)  :', len(json.dumps(data, indent=4))
    # print 'dumps(data, separators):', len(json.dumps(data, separators=(',', ':')))
    print "d1:", d1, '\n', '\n', "d2:", d2, '\n', "data3:", data3, "\n", "d2_1:", d2_1, "\n", d3
    # print d1 == d2
    # print d1 == d3
    # print data3 == d2
    # print type(data3), type(d2)
    # print len(data3), len(d2)
    # print "the original list:\n", obj
    # print "length of obj:\n", len(repr(obj))
    # print repr(obj)
    # print "repr(obj),replace whiteblank with *:\n", repr(obj).replace(" ", "*")
    # print "json encoded,replace whiteblank with *:\n", encodedjson.replace(" ", "*")
    # print 'the type of decodeed obj from json:', type(decodejson)
    # print 'the obj is:\n', decodejson
    # print 'length of decoded obj is:', len(repr(decodejson))
    pass
