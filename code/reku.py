# 日常应用比较广泛的模块
# 1、文字处理的 re

# match 匹配字符串的开头, 只返回一个
# search 匹配字符串, 只返回一个
# findall
# 在string中查找所有 匹配成功的组, 即用括号括起来的部分。返回list对象，每个list item是由每个匹配的所有组组成的list。

# finditer
# 在string中查找所有 匹配成功的字符串, 返回iterator，每个item是一个Match object。

# 正则表达式库 re
import re


# 做单个字符的匹配
p = re.compile('a')  # 定义一个要匹配的字符串
# print(p.match('ab'))
# print(p.search('abcsas'))
# print(p.findall('abcsas'))
# print(p.finditer('abcsas'))


print("====================")

p1 = re.compile('ca*t')
# print(p1.match('cat'))


print("*********************")

# p2 = re.compile('..t')
p2 = re.compile('jpg$')

# print(p2.match('abt'))


# =======================
# p3 = re.compile('...') # 匹配三个任意字符 .{3}
# print(p3.match('cat'))
# p3 = re.compile('....-..-..')  # r'(\d+)-(\d+)-(\d+)' 加r是为了让特殊的转义字符不转义
# print(p3.match('2018-05-10'))
# p3 = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p3.match('2018-05-10').group(1))

# year, month, day = p3.match('2018-05-10').groups()
# print()


# print('\nX\n')
# print(r'\nX\n')

# search
phone = '123-456-789 # 这是电话号码'
p4 = re.sub(r'#.*$', '', phone)
pb = re.sub(r'\D', '', p4)

print(p4, pb)
