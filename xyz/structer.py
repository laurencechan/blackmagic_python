# coding=utf-8

with open("aaa.xyz", "r") as f:
    a = f.readlines()
    list_a = a[2:]
    for i in list_a:
        l = i.strip(" ")



if __name__ == '__main__':
    pass