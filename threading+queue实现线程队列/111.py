import threading
class A(threading.Thread):
    name = "laurencechan"
    def run(self):
        return 'hello laurencechan'



if __name__ == '__main__':
    print [A() for i in range(5)]
    pass