# 存储星座的信息
zodiac_name = (
    u'摩羯座', u'水平座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
    u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座'
)

# 存储星座的开始时间和结束时间 (月份加日期)
zodiac_days = (
    (1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
    (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23)
)

# 定义输入的月份和日期
(month, day) = (2, 15)
# a = ((2, 15), (3, 5))
# print(zodiac_days + a)

zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# print(zodiac_day)
zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_len)
# print(zodiac_name[zodiac_len])

# 定义一个列表
a_list = ['ab', 'cd', 1]
b_list = [2]

a_list.append('werw')
a_list.remove(1)
# print('ab' in a_list)
# print('ab' in b_list)
# print(a_list[1:2])

# 定义一个元组
a_tuple = ('xq', 'yw', 'fsfs')
b_tuple = ('a', 1)
# print(a_tuple * 2)
# print(a_tuple[1:2])
# print('ab' in a_tuple)
# print(a_tuple + b_tuple)

# 1. 定义一个含有5个数字的列表
list1 = [5, 6, 7, 8, 9]
# 使用type( )可以查看变量的类型
# print(type(list1))   <class 'list'>
# print(type(a_tuple)) <class 'tuple'>

# 1. 定义一个任意元组，对元组使用append() 查看错误信息
tuple1 = ('x', 'y', 3, 4, 5)
# 3. 定义一个新的元组，和 1. 的元组连接成一个新的元组
tuple2 = ('a', 'b', 'c')
# print(tuple1 + tuple2)

print(len(tuple1))
print(tuple1.__len__())
