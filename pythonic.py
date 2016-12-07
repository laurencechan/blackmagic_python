# coding=utf-8

with open(r'E:\python\blackmagic_python\doc\test.txt') as myfile:
    for line in myfile:
        print line.decode(encoding='utf-8', errors='strict').lower()

if __name__ == '__main__':
    pass
