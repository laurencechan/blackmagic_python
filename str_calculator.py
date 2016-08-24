# coding=utf-8
import re


class Str_calculator():
    def __init__(self):
        pass

    @classmethod
    def jiajian(self, ss=''):
        num_list_str = re.split('[+-]', ss)
        num_list = []
        for i in num_list_str:
            if i[0] == '0':
                num_list.append(-int(i))
            else:
                num_list.append(int(i))
        fuhao_list = []
        for i in range(len(ss)):
            if ss[i].isdigit() == False:
                fuhao_list.append(ss[i])
        sum_plus = num_list[0]
        for i in range(len(fuhao_list)):
            if fuhao_list[i] == '+':
                sum_plus += num_list[i + 1]
            elif fuhao_list[i] == '-':
                sum_plus += (-num_list[i + 1])
        if sum_plus < 0:
            sum_plus = '0' + str(-sum_plus)
        else:
            sum_plus = str(sum_plus)
        # print sum_plus
        return sum_plus

        # return num_list,fuhao_list

    @classmethod
    def jiajian_jisuan(self, num_list=[], fuhao_list=[]):
        sum_plus = num_list[0]
        for i in range(len(fuhao_list)):
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
        num_str_list = re.split('[*/]', ss)
        num_list = []
        for i in num_str_list:
            if i[0] == '0':
                num_list.append(-int(i))
            else:
                num_list.append(int(i))
        fuhao_list = []
        for i in ss:
            if i.isdigit() == False:
                fuhao_list.append(i)
        result = 0
        while len(fuhao_list) > 0:
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
        if '*' not in ss and '/' not in ss:
            result = Str_calculator.jiajian(ss)
        elif '+' not in ss and '-' not in ss:
            result = Str_calculator.lianxu_chengchu(ss)
        else:
            tt = len(ss)
            fuhao_list = []
            for i in range(tt):
                if ss[i] == "+" or ss[i] == "-":
                    fuhao_list.append(ss[i])
            chengchu_list = re.split('[+-]', ss)
            for i in range(len(chengchu_list)):
                if '*' in chengchu_list[i] or '/' in chengchu_list[i]:
                    chengchu_list[i] = Str_calculator.lianxu_chengchu(chengchu_list[i])
            jiajian_list = []
            for i in chengchu_list:
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
        while "(" in ss:
            reg = '(\([\d]+[\*|\-|\+|\/\d+]+\))'
            regkuo = re.compile(reg)
            list_kuo = re.findall(regkuo, ss)
            for i in list_kuo:
                result = Str_calculator.jisuan(i[1:-1])
                ss = ss.replace(i, result)
        final = Str_calculator.jisuan(ss)
        if final[0] == '0' and final[1] != '.':
            final = final.replace(final[0], '-')
        print final


if __name__ == '__main__':
    Str_calculator.calculator()
    # Str_calculator.jisuan('12/4+3-6*07*5+62-6*5/4')
    # Str_calculator.jiajian('6+6')
    # Str_calculator.lianxu_chengchu('(6+6)/4+3-6*(5+6-6*3)*5+62-6*5/4')
    pass
