# coding=utf-8

import threadpool
import time, random


def threadpool_test(arg):
    time.sleep(0.01)
    return arg


def print_result(request, result):
    print "结果 %s %r" % (request.requestID, result)


if __name__ == '__main__':
    data = ['test_%d' % i for i in range(20)]
    pool = threadpool.ThreadPool(5)
    requests = threadpool.makeRequests(threadpool_test, data, print_result)
    for req in requests:
        pool.putRequest(req)
    pool.wait()
    print '结束！'
