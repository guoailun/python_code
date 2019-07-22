# 先简单把一年看做一个生肖（1月到12月份归属为一个生肖）
# 记录生肖，根据用户输入的年份来判断生肖
chinese_zodiac = '鼠牛虎兔龙蛇马羊候鸡狗猪'
chinese_zodiac2 = '候鸡狗猪鼠牛虎兔龙蛇马羊'

year = 2019
# print(2019 % 12)
# print(chinese_zodiac2[2019 % 12])

# 序列的常规操作符
# in not in
print("1" in chinese_zodiac)
# + 
# print(chinese_zodiac + 1) # error
print(chinese_zodiac + "1")
# *
print("2" * 3)


# 字符串类型是属于序列的，可以通过下表访问
# chinese_zodiac[0]
# print(chinese_zodiac[0:4])
# print(chinese_zodiac[1:4])
# print(chinese_zodiac[11:15]) 输出最后一个
# print(chinese_zodiac[-0])  输出第一个

# print(chinese_zodiac[15]) error
# print(chinese_zodiac[1:10])
# print(chinese_zodiac[13:10])


# 如果变量只想要第一个，及第三个要怎么办？
# 作者回复: 我想你是想要知道如何同时取得一个字符串(序列)的第一个和第三个元素，在Python中有一种非常简便的实现方法：
# 假设有字符串：
# aString = ‘abcd’， 
# 将字符串同时赋予四个变量，既：
# x1, x2, x3, x4 = aString
# 那么 x1 就是字符串的第一个元素，x3 就是第三个元素了是不是很灵活,而且对序列类型都可以生效的
# 还有一种情况要在编程中考虑到，如果字符串中的元素比较多的时候，如：
# aString = ‘abcdefg’
# 不需要定义更多的变量来一一对应元素个数，可以使用 *(星号)来匹配，同样取出第一个第三个元素，使用
# x1, x2, x3, *x4 = aString # 注意x4变量前面的星号
# 使用x1, x3 变量依然可以取出第一个和第三个元素，而且这样编写程序适用范围更广泛哦