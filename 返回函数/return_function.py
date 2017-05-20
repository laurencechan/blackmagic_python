# coding=utf-8

def lazy_sum(*args):
    """

    :param args:
    :return:
    """

    def sum():
        ax = 0
        for i in args:
            ax += i
        return ax

    return sum


if __name__ == '__main__':
    ss = lazy_sum(1, 2, 3, 4, 5, 6, 7)
    print ss
    print ss()
    pass
