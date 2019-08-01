# 统计三国演义的英雄和武器出现的次数

# 读取人物名称
# f = open("sanguo_name.text")
# data = f.read()
# print(data.split('|'))

# 读取兵器的名称
# f2 = open("sanguo_wuqi.text")
# data2 = f2.read()
# print(data2)
# i = 1
# for line in f2.readlines():
#     # print(line)
#     if i % 2 == 1:
#         # print(line)
#         print(line.strip('\n'))
#     i += 1


# 读三国  有一些文件打不开，报一个编码错误 要使用 open('name', encoding='GB18030') 做string匹配时，文件中的内容
# 可能存在换行，导致匹配不准确，需要用replace去除\n

# f3 = open("sanguo_quan.text")
# print(f3.read())


# 下面我们来简单实现以下，主角英雄出现的次数
import re

def find_num( hero ):
    with open('sanguo_quan.text') as f:
        data = f.read().replace('\n','')
        name_num = re.findall(hero, data)
        print("主角 %s 出现的次数是 %s" %(hero, len(name_num)))
    return len(name_num)

# name_dic = {}
# with open('sanguo_name.text') as f:
#     for line in f:
#         names = line.split('|')
#         for hero in names:
#             name_num = find_num(hero)
#             name_dic[hero] = name_num
# print(name_dic)

name_dic = {}
with open('sanguo_name.text') as f:
    names = f.read().split('|')
    for hero in names:
        name_num = find_num(hero)
        name_dic[hero] = name_num
print(name_dic)


# 作业，1、创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和

# def sum(a, b):
#     return a + b

# a = int(input("请输入数字a: "))
# b = int(input("请输入数字b: "))
# print(sum(a,b))

def sum():
    sum = 0
    num_str = input("请输入多个整数，并且用逗号分隔: ")
    num_list = num_str.split(',')
    for i in range(len(num_list)):
        sum += int(num_list[i])

    return sum

print(sum())







