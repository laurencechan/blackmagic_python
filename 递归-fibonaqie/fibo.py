# coding=utf-8

def fib(n):
    if n<=2:
        return 1
    else:
        return  fib(n-1)+fib(n-2)



if __name__ == '__main__':
    aa = fib(20)
    print aa
    pass