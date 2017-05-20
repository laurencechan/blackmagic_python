import Queue
import threading
import time

queue = Queue.Queue()


class ThreadNum(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            num = self.queue.get()
            print "I'm num %s" % num
            time.sleep(1)
            self.queue.task_done()

start = time.time()
def main():
    for i in range(10):
        t = ThreadNum(queue)
        t.setDaemon(True)
        t.start()
    for num in range(10):
        queue.put(num)
    queue.join()



if __name__ == '__main__':
    # print queue
    main()
    print "Elapsed Time:%s" % (time.time() - start)

    pass
