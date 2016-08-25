# coding=utf-8

from turtle import Turtle


class Turtle_draw(Turtle):  # 继承
    pass
    # 一个神奇的自动绘图方法

    @staticmethod
    def t_draw():
        t = Turtle_draw()
        t.setpos(-200, 0)  # 绘图起始点
        for i in range(36):  # 画9笔
            t.forward(500)   # 朝坐标系正方向前进500的距离
            t.right(190)  # 在完成上一步动作停留处向于上一部动作方向成190夹角的方向再前进500的距离，不断重复


if __name__ == '__main__':
    Turtle_draw.t_draw()
    pass
