# coding=utf-8

from collections import namedtuple, deque
import sys, time


class Collections():
    pass

    def __init__(self):
        pass

    @classmethod
    def named_tuple(self):
        # 将多个结构相同的元组变成字典
        websites = [
            ('Sohu', 'http://www.sohu.com', u'张朝阳'),
            ('Sina', 'http://www.sina.com', u'王志东'),
            ('163', 'http://www.163.com', u'丁磊')
        ]

        Website = namedtuple('Website', ['name', 'url', 'Founder'])  # 指定新构造的字典的名称和key值
        for website in websites:
            website = Website._make(website)
            print website

    @classmethod
    def double_ended_queue(cls):
        # 实现一个小小的动画效果
        fancy_loading = deque('&&&-----------------')
        while True:
            # yy = '\r%s' % ''.join(fancy_loading)
            print '\r%s' % ''.join(fancy_loading)  # 打印的结果连在一起r为换行
            fancy_loading.rotate(3)  # rotate是将deque类型的末尾项移到头部，3表示末尾3项
            # sys.stdout.flush()
            time.sleep(0.2)


if __name__ == '__main__':
    # Collections.named_tuple()
    Collections.double_ended_queue()
    pass
