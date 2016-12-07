# coding=utf-8

from time import sleep, ctime
import thread, threading

loops = [4, 2]


class Single():
    """单线程"""

    def __init__(self):
        pass

    @staticmethod
    def loop0():
        print 'start loop 0 at:', ctime()
        sleep(4)
        print 'loop 0 done at:', ctime()

    @staticmethod
    def loop1():
        print 'start loop 1 at:', ctime()
        sleep(2)
        print 'loop 1 done at:', ctime()

    @staticmethod
    def main():
        print 'start:', ctime()
        Single.loop0()
        Single.loop1()
        print 'all end:', ctime()


class Multithread():
    """多线程，需要用sleep()让主线程停下来，等待双线程执行完"""

    def __init__(self):
        pass

    @staticmethod
    def loop0():
        print 'start loop 0 at:', ctime()
        sleep(4)
        print 'loop 0 done at:', ctime()

    @staticmethod
    def loop1():
        print 'start loop 1 at:', ctime()
        sleep(2)
        print 'loop 1 done at:', ctime()

    @staticmethod
    def main():
        print 'start:', ctime()
        thread.start_new_thread(Multithread.loop0, ())
        thread.start_new_thread(Multithread.loop1, ())
        sleep(6)
        print 'all end:', ctime()


class Mutithread_lock():
    """多线程，为每个线程上锁以暂停主线程，待所有线程运行完成，并解锁后，再执行主线程"""

    def __init__(self):
        pass

    @staticmethod
    def loop(nloop, nsec, lock):
        print 'start loop%s at:' % nloop, ctime()
        sleep(nsec)
        print 'loop%s done at:' % nloop, ctime()
        # 解锁
        lock.release()

    @staticmethod
    def main():
        print 'starting at:', ctime()
        locks = []
        nloops = range(len(loops))

        for i in range(2):
            lock = thread.allocate_lock()
            # 锁定
            lock.acquire()
            # 追加到locks[]数组中
            locks.append(lock)

        # 执行多线程
        for i in nloops:
            thread.start_new_thread(Mutithread_lock.loop, (i, loops[i], locks[i]))

        for i in nloops:
            while locks[i].locked():
                pass

        print 'all end:', ctime()


class Multithreading():
    """threading相比thread的优点在于threading支持守护线程。在thread模块中则不支持守护线程，即当主线程退出
    时，所有的子线程不论它们是否还在工作，都会被强行退出"""
    def __init__(self):
        pass

    @staticmethod
    def loop(nloop, nsec):
        print 'start loop%s at:' % nloop, ctime()
        sleep(nsec)
        print 'loop%s done at:' % nloop, ctime()

    @staticmethod
    def main():
        print 'starting at:', ctime()
        threads = []
        nloops = range(len(loops))

        # 创建线程
        for i in nloops:
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
    # Single.main()
    # Multithread.main()
    # Mutithread_lock.main()
    Multithreading.main()
