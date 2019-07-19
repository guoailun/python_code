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
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
print(zodiac_day)