# 列表推导式

# 问题：给列表和字典赋值

# 1、正常的列表赋值
lista = []
for i in range(1, 11):
    if i % 2 == 0:
        lista.append(i*i)

print(lista)

# 2、利用推导式列表赋值
listb = [i*i for i in range(1, 11) if i % 2 == 0]

print(listb)

# 存储生肖的信息
chinese_zodiac = '候鸡狗猪鼠牛虎兔龙蛇马羊'

# 1、正常的字典赋值
cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

print(cz_num)

# 1、利用推导式字典赋值
cz_num2 = {}
cz_num2 = { i:0 for i in chinese_zodiac }
print(cz_num2)
