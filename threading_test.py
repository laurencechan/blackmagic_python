# coding=utf-8
import threading
from time import ctime, sleep

loops = [4, 2]


class Multithreading():
    """threading相比thread的优点在于threading支持守护线程。在thread模块中则不支持守护线程，即当主线程退出
    时，所有的子线程不论它们是否还在工作，都会被强行退出"""

    def __init__(self):
        pass

    @staticmethod
    def loop(nloop, nsec):
        # 这个方法可以改造成你自己的计算方法
        print 'start loop%s at:' % nloop, ctime()
        sleep(4)
        print 'loop%s done at:' % nloop, ctime()

    @staticmethod
    def main():
        print 'starting at:', ctime()
        threads = []
        nloops = range(len(loops))  # 如果需要同时有30个线程运行 可以写成 range(30)

        # 创建线程
        for i in nloops:  # 同理，如果运行30个线程，此处写成range(30)
            t = threading.Thread(target=Multithreading.loop, args=(i, loops[i]))
            threads.append(t)

        # 开始线程
        for i in nloops:
            threads[i].start()

        # 等待所有线程结束
        for i in nloops:
            threads[i].join()

        print 'all end:', ctime()


if __name__ == '__main__':
    Multithreading.main()
    pass

