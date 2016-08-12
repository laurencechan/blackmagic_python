# coding=utf-8

from collections import namedtuple,deque
import sys,time


class Collections():
    pass

    def __init__(self):
        pass

    @classmethod
    def named_tuple(self):
        websites = [
            ('Sohu','http://www.sohu.com',u'张朝阳'),
            ('Sina','http://www.sina.com',u'王志东'),
            ('163','http://www.163.com',u'丁磊')
        ]

        Website = namedtuple('Website',['name','url','Founder'])
        for website in websites:
            website = Website._make(website)
            print website

    @classmethod
    def double_ended_queue(cls):
        fancy_loading = deque('&&&-----------------')
        while True:
            # yy = '\r%s' % ''.join(fancy_loading)
            print '\r%s' % ''.join(fancy_loading)
            fancy_loading.rotate(3)
            sys.stdout.flush()
            time.sleep(0.2)






if __name__ == '__main__':
    # Collections.named_tuple()
    Collections.double_ended_queue()
    pass
