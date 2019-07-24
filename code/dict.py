# 利用字典来记录用户输入的信息

# 存储生肖的信息
chinese_zodiac = '候鸡狗猪鼠牛虎兔龙蛇马羊'

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

# 声明字典
# 存储生肖的数量
cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

# 存储星座的数量
z_num = {}
for i in zodiac_name:
    z_num[i] = 0

while True:
    input_year = int(input("请输入年份: "))
    input_month = int(input("请输入月份: "))
    input_day = int(input("请输入日期: "))
    index_num = 0
    while zodiac_days[index_num] < (input_month, input_day):
        if input_month == 12 and input_day > 23:  # 增加判断，防止index溢出
            break
        index_num += 1
    
    # 统计生肖和星座
    cz_num[chinese_zodiac[input_year % 12]] += 1
    z_num[zodiac_name[index_num]] += 1

    # 输出生肖和星座的统计值
    print(cz_num)
    print(z_num)


    

# input_month = int(input("请输入月份: "))
# input_day = int(input("请输入日期: "))

# 使用while循环和if条件语句的嵌套来，根据用户输入的月份和日期来判断星座

# index_num = 0
# while zodiac_days[index_num] < (input_month, input_day):
#     if input_month == 12 and input_day > 23:  # 增加判断，防止index溢出
#         break
#     index_num += 1
# print(zodiac_name[index_num])
