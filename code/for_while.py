# while 语句
# 计算1到100的和
n = 100
sum = 0
number = 1
while number <= n:
    sum += number
    number += 1

# print("1 到 %d 之和为: %d" % (n,sum))

# while循环语句
# import time
# num = 5
# while True:
#     num = num + 1
    
#     if num == 10:
#         continue
#     print(num)
#     time.sleep(1)

    

# for循环 语句
# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")

# for循环 语句
# range函数     range(参数) 一个参数：从0开始  range(1，13) 两个参数：从1开始带13，但是不包含13
chinese_zodiac2 = '候鸡狗猪鼠牛虎兔龙蛇马羊'
# for year in range(2000, 2020):
#     print('%s 年的生肖是 %s' %(year, chinese_zodiac2[year % 12]))
    
# for year in range(2000, 2020):
#     print('%a 年的生肖是 %a' %(year, year + 1))

 #'%s的生肖是%s' %(year...) 这里的 %( ) 结构叫做字符串格式化，用 %( )里面的每个变量按照 %s 的格式进行输出


tuple_a = ('z', 'd', 'd')
tuple_b = ((1, 2), (3, 4))
list_a = [[1, 2], 2, 3]
# for one in list_a:
#     print(one)
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, ' 是质数')


# 使用for语句输出1-100之间的所有偶数
for num in range(1, 100):
    if num % 2 == 0:
        print(num)


# 使用while语句输出1-100之间能够被3整除的数字
a = 0
while a < 100:
    if a % 3 == 0:
        print(a)
    a = a + 1
