# coding=utf-8
""" 实现一个python的字符串计算功能，直接输入一串带括号的四则运算式子，就能得出计算得到的结果，其实就是eval函数的功能，这里只是强行造出了这个轮子"""
import re


class Str_calculator():
    def __init__(self):
        pass

    @classmethod
    def jiajian(self, ss=''):
        # 不带括号的连续加减法计算
        num_list_str = re.split('[+-]', ss)  # 以‘+’和‘-’对传入的算式字符串进行分割
        num_list = []
        for i in num_list_str:  # 将得到的list中的字符串转成int类型
            if i[0] == '0':  # 如果数字字符串首位是‘0’ 则改数为负数：这个是在calculator方法中定义的
                num_list.append(-int(i))
            else:
                num_list.append(int(i))
        fuhao_list = []
        for i in range(len(ss)):  # 将运算符号按顺序放到另外一个列表 fuhao_list中
            if ss[i].isdigit() == False:
                fuhao_list.append(ss[i])
        sum_plus = num_list[0]  # 计算方法是用num_list的第一项去加后面的每一项，如果是碰到‘-’,则加对应数字的负数
        for i in range(len(fuhao_list)):
            if fuhao_list[i] == '+':
                sum_plus += num_list[i + 1]
            elif fuhao_list[i] == '-':
                sum_plus += (-num_list[i + 1])
        if sum_plus < 0:
            sum_plus = '0' + str(-sum_plus)  # 结果小于0的话 在前面添 0  以示区分，因为直接加‘-’的话会在split字符串时发生冲突
        else:
            sum_plus = str(sum_plus)
        # print sum_plus
        return sum_plus  # 得到str type的结果

        # return num_list,fuhao_list

    @classmethod
    def jiajian_jisuan(self, num_list=[], fuhao_list=[]):
        #  在jiajian方法中 前半部分定义的 当传入一个切割完毕得到的数字list和运算符list 即可得出计算结果，方便后面的调用
        sum_plus = num_list[0]
        for i in range(len(fuhao_list)):  # 计算方法跟jiajian方法中的一样
            if fuhao_list[i] == '+':
                sum_plus += num_list[i + 1]
            elif fuhao_list[i] == '-':
                sum_plus += (-num_list[i + 1])
        if sum_plus < 0:
            sum_plus = '0' + str(-sum_plus)
        else:
            sum_plus = str(sum_plus)
        return sum_plus

    @classmethod
    def lianxu_chengchu(self, ss=''):
        # 只有乘法和除法两种运算符号的无括号连续算式的计算
        num_str_list = re.split('[*/]', ss)  # 用*/进行分割
        num_list = []
        for i in num_str_list:  # 将str 类型的数字list 化为整型 list
            if i[0] == '0':
                num_list.append(-int(i))  # 首位为0的数字视为负数
            else:
                num_list.append(int(i))
        fuhao_list = []
        for i in ss:  # 将运算符号按运算顺序置于另一个列表
            if i.isdigit() == False:
                fuhao_list.append(i)
        result = 0
        while len(fuhao_list) > 0:  # 用另外一种方法计算 也可以用 jiajian方法的中方式去计算，两种不能的思路，都行得通
            if fuhao_list[0] == '*':
                result = num_list[0] * num_list[1]
                num_list[0] = result
            elif fuhao_list[0] == '/':
                if num_list[0] % num_list[1] != 0:
                    result = float(num_list[0]) / float(num_list[1])
                else:
                    result = num_list[0] / num_list[1]
                num_list[0] = result
            fuhao_list.remove(fuhao_list[0])
            num_list.remove(num_list[1])
        # print result
        return result

    @classmethod
    def jisuan(self, ss=''):
        # 将所有计算方式的可能性放到一起
        if '*' not in ss and '/' not in ss:  # 如果只有加减运算，则直接调用jiajian方法
            result = Str_calculator.jiajian(ss)
        elif '+' not in ss and '-' not in ss:  # 如果只有乘除运算，则直接调用lianxu_chengchu方法
            result = Str_calculator.lianxu_chengchu(ss)
        else:  # 至少包含加减中的一种和乘除中和一种的计算方法 （无括号）
            tt = len(ss)
            fuhao_list = []
            for i in range(tt):
                if ss[i] == "+" or ss[i] == "-":  # 将 “+”“-”符号按出现顺序置于fuhao_list中
                    fuhao_list.append(ss[i])
            chengchu_list = re.split('[+-]',
                                     ss)  # 将字符串用“+”“-”分割  如‘56+32+8*9/8+6*6/5’分割成['56','34','8*9/8','6*6/5'] 定义为chengchu_list
            for i in range(len(chengchu_list)):
                if '*' in chengchu_list[i] or '/' in chengchu_list[i]:  # 改list中的元素如果其中包含*或者/，则直接调用lianxu_chengchu方法
                    chengchu_list[i] = Str_calculator.lianxu_chengchu(chengchu_list[i])
            jiajian_list = []
            for i in chengchu_list:  # 计算完成后得到一个只含数字的list和只含加减号的list，调用jiajian_jisuan方法就可以算出结果
                if type(i) == str:
                    jiajian_list.append(int(i))
                elif type(i) != str:
                    jiajian_list.append(i)
            result = Str_calculator.jiajian_jisuan(jiajian_list, fuhao_list)
        # print result
        return result

    @classmethod
    def calculator(self):
        ss = raw_input()
        while "(" in ss:  # 当字符串中含有括号时
            reg = '(\([\d]+[\*|\-|\+|\/\d+]+\))'  # 用正则匹配所有的底层括号（该括号里面不再包含别的括号）
            regkuo = re.compile(reg)
            list_kuo = re.findall(regkuo, ss)
            for i in list_kuo:
                result = Str_calculator.jisuan(i[1:-1])  # 计算括号里的结果 i[1:-1]是对正则匹配到的带（）的字符串进行切片，只保留括号中的算式部分
                ss = ss.replace(i, result)  # 用计算结果代替原来的带括号的内容
        final = Str_calculator.jisuan(ss)  # 最后处理不带任何括号的混合运算
        if final[0] == '0' and final[1] != '.':  # 得到的结果如果为负数，就将首位的标志‘0’改为‘-’，以得到正确的可以看到的结果
            final = final.replace(final[0], '-')
        print final


if __name__ == '__main__':
    Str_calculator.calculator()  # test (6+6)/4+3-6*(5+6-6*3)*5+62-6*5/4   运行程序后，将算式输入控制台并回车
    # Str_calculator.jisuan('12/4+3-6*07*5+62-6*5/4')
    # Str_calculator.jiajian('6+6')
    # Str_calculator.lianxu_chengchu('(6+6)/4+3-6*(5+6-6*3)*5+62-6*5/4')
    pass
