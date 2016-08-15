# coding=utf-8
import re


class Str_calculator():
    def __init__(self):
        pass

    @classmethod
    def jiajian(self, ss=''):
        if '*' not in ss and '/' not in ss:
            # for i in range(len(ss)):
            num_list = re.split('[+-]', ss)
            print num_list

    @classmethod
    def calculator(self):
        ss = raw_input()
        while "(" in ss:
            reg = '(\([\d]+[\*|\-|\+|\/\d+]+\))'
            regkuo = re.compile(reg)
            list_kuo = re.findall(regkuo, ss)
            for i in list_kuo:
                result = str(eval(i))
                ss = ss.replace(i, result)
        print eval(ss)


if __name__ == '__main__':
    # Str_calculator.calculator()
    Str_calculator.jiajian('6+6+4-9')

    pass
