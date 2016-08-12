# coding=utf-8

from turtle import Turtle

class Turtle_draw(Turtle): # 继承
    pass

    @staticmethod
    def t_draw():
        t = Turtle_draw()
        t.setpos(-200,0)
        for i in range(36):
            t.forward(400)
            t.right(170)


if __name__ == '__main__':
    Turtle_draw.t_draw()
    pass